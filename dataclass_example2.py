# EJERCICIO:
# TENEMOS UN DICCIONARIO QUE CONTIENE LAS EQUIVALENCIAS DE UN UN MODELO DE DATOS A OTRO
# MEJÓRALO CON DATACLASS
######################################################
# API to UI DATA MODEL WITH CONSTANTS
######################################################
from dataclasses import dataclass

NBA_DETAILS_MODEL = {
    "player": {
        "ui_name": "Player",
        "api_name": "player",
        "card_name": "Player Name",
    },
    "team": {
        "ui_name": "Team",
        "api_name": "team",
        "card_name": "Team Name",
    },
    "conference": {
        "ui_name": "Conference",
        "api_name": "conference",
        "card_name": "Conference name",
    },
}


def get_nba_details_cards(group_by):

    return [v["card_name"] for k, v in NBA_DETAILS_MODEL.items() if k != group_by]


def get_api_name_from_card(card_name):
    keys = [
        k
        for k, v in NBA_DETAILS_MODEL.items()
        if any(card_name in subelements for subelements in NBA_DETAILS_MODEL[k].values())
    ]
    if keys:
        return NBA_DETAILS_MODEL[keys[0]]["api_name"]
    return None


def get_ui_name_from_card(card_name):
    keys = [
        k
        for k, v in NBA_DETAILS_MODEL.items()
        if any(card_name in subelements for subelements in NBA_DETAILS_MODEL[k].values())
    ]
    if keys:
        return NBA_DETAILS_MODEL[keys[0]]["ui_name"]
    return None


######################################################
# API DATA MODEL WITH DATACLASS
######################################################


@dataclass
class NBAdetails:
    pass


@dataclass
class Player(NBAdetails):
    ui_name: str = "Player"
    api_name: str = "player"
    card_name: str = "Player Name"
    name: str = None


@dataclass
class Team(NBAdetails):
    ui_name: str = "Team"
    api_name: str = "team"
    card: str = "Team Name"
    name: str = None


@dataclass
class Conference(NBAdetails):
    ui_name: str = "Conference"
    api_name: str = "conference"
    card: str = "Conference Name"
    name: str = None


if __name__ == "__main__":

    """
    Con diccionarios:
    """
    for key in NBA_DETAILS_MODEL.keys():
        cards = get_nba_details_cards(key)

        for secondary_key in cards:

            api_call_key = get_api_name_from_card(secondary_key)
            ui_key = get_ui_name_from_card(secondary_key)
            print(f"En la API ordenamos por {key}, filtramos por {api_call_key}")
            print(f"En la UI ordenamos por {key}, filtramos por {ui_key}")
            print(f"\n")

    """
    Con dataclasses
    """
    print(f"\n\n")
    for key in Player(), Team(), Conference():
        iterate_list = [item for item in (Player(), Team(), Conference()) if item != key]

        for secondary_key in iterate_list:
            print(f"En la API ordenamos por {key.api_name}, filtramos por {secondary_key.api_name}")
            print(f"En la UI ordenamos por {key.ui_name}, filtramos por {secondary_key.ui_name}")
            print(f"\n")
