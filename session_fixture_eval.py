import pytest
import logging
import random

LOG = logging.getLogger(__name__)


class HeavyFixture(object):
    def __init__(self, request, choices=["success", "fail"]):
        self.request = request
        self.result = random.choice(choices)
        if self.result == "success":
            pass
        else:
            raise ValueError

    def __enter__(self):
        return self.result

    def __exit__(self, exc_type, value, traceback):
        @self.request.addfinalizer
        def close():
            print("Cerramos contexto")


def evaluate_source_setup(request, setup_fixture):
    """
    Function to evaluate result of source_setup_fixture. If source setup
    fails, tests with ingest_heavy_source marker will error-out while other tests will xfail
    - source_setup_fixture[0]: result of setup True vs. False
    - source_setup_fixture[1:]: provs (if setup True) vs. captured setup error (if setup False)
    """

    if setup_fixture[0]:
        return (
            setup_fixture[1] if len(setup_fixture) == 2 else setup_fixture[1:]
        )

    else:
        marker = request.node.get_closest_marker("ingest_heavy_source")
        if marker is None:
            pytest.xfail("Heavy fixture failed")
        else:
            raise setup_fixture[1]


@pytest.fixture(scope="session")
def setup_heavy_fixture(request):
    """
    Fixture to add 1 OCP source

    source_name: test_cost_ocp_for_aws_single_last_month_cluster
    time_range: 1st previous month -> Today Current hour
    correlates with:  aws_source_static
    cost_model: test_cost_ocp_for_aws_single_last_month_cluster (default rates)
    usage_notes:

    """
    try:
        with HeavyFixture(request) as result:
            return True, result

    except ValueError as e:
        LOG.error(e)
        return False, e


@pytest.fixture(scope="function")
def heavy_fixture_evaluation(request, setup_heavy_fixture):
    """
    This fixture run with every test hat uses the fixture above,
    which is session scoped and evaluated only once
    This fixtures evaluates the result of the above setup, in a test basis
    if the setup failed:
        tests with cost_ingest_source marker will error-out
        tests using this fixture and without the marker will xfail
    """
    return evaluate_source_setup(request, setup_heavy_fixture)


@pytest.mark.ingest_heavy_source
def test_ingest_heavy_fixture(heavy_fixture_evaluation):
    """Test to ingest heavy fixture

    """
    assert heavy_fixture_evaluation


def test_anytest_using_fixture(heavy_fixture_evaluation):
    """Test to ingest heavy fixture

    """
    assert True