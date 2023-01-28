import pytest
import logging
import random

LOG = logging.getLogger(__name__)



def get_currency_settings(application):

    # Settings API Client returns SettingOut model in a list -> [SettingOut]
    settings_data = application.cost_management.rest_client.settings_api.get_settings()[0]

    # Turn SettingOut into a dictionary, get "fields" values and iterate until currency option found
    currency_settings = [
        x
        for x in settings_data.to_dict()["fields"]
        if "api.settings.currency" and "select" in x.values()
    ][0]


    """
    # Using brackets vs .get() will cause KeyError if key doesn't exist, which we want
    """
    options = currency_settings["options"]

    initial_currency = currency_settings["initialValue"]

    return [currency["value"] for currency in options], initial_currency





def settings_rollback(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        application = kwargs["application"]
        LOG.info("Get original tag settings:")
        initial_tags = get_tag_settings(application)[1]
        LOG.info(f"Running the test: {func.__name__}")
        try:
            func(*args, **kwargs)
        except Exception as e:
            LOG.error(f"{e.__class__} during the test run")
            raise e
        finally:
            LOG.info("Reverting Cost Management settings to original values:")
            final_options = get_tag_settings(application)[0]
            tags_to_enable = [tag for tag in initial_tags if tag in final_options]
            application.cost_management.rest_client.settings_api.assign_settings(
                {
                    "api": {
                        "settings": {
                            "tag-management": {"enabled": tags_to_enable},
                            "cost_type": "unblended",
                            "currency": "USD",
                        }
                    }
                }
            )

    return wrapper


@settings_rollback
def test_api_settings_currency(application):
    """Verify that any currency listed in the currency options can be set as the initial currency

    metadata:
        requirements: cost_currency
    """

    """ get initial currency settings """
    currency_options_0, currency_initial_0 = get_currency_settings(application)

    """ Verify that any of currency options can be set as initial currency"""
    for currency in currency_options_0:
        LOG.info(f"Setting {currency} as the initial currency")
        application.cost_management.rest_client.settings_api.assign_settings(
            {"api": {"settings": {"currency": currency}}}
        )
        options, initial = get_currency_settings(application)
        assert sorted(options) == sorted(
            currency_options_0
        ), "Unexpected change of currency options"
        assert initial == currency, f"Unable to set {currency}"
    """ Verify that options in currency/ endpoint match options in settings page"""

    currency_report = call_api("/currency/?limit=100", application)
    currency_report_options = [currency.get("code") for currency in currency_report["data"]]
    assert sorted(currency_report_options) == sorted(
        currency_options_0
    ), "Currency options in /currency endpoint doesn't match settings page"

