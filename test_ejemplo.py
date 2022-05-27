import pytest
import sys

from ejemplo import Employee

@pytest.mark.parametrize(
    "e",
    [
        pytest.param(Employee(), id="esto testea AAAAA")
    ]
)
def test_some(e):
    print("Ejecuto el test")


@pytest.mark.parametrize(
    "e",
    [
        pytest.param(Employee(), id="esto testea BB")
    ]
)
def test_some_2(e):
    print("Ejecuto el test")

{
    "internal_id": "aaaaaa",
    "name": "david",
    "surname": "garcia",
    "birthdate": 14565783543
}

{
    "name": "David",
    "surname": "Garcia",
    "birthdate": "11/05/1993"
}

@dataclass
class UserData:
    internal_id: str
    name: str
    surname: str
    birthdate: int

    def to_api(self) -> UserDataApi:
        return UserDataApi(**asdict(self))

    def to_ui(self) -> UserDataUI:
        return UserDataUI(
            name=self.name.capitalize(),
            surname=self.surname,
            birthdate=from_ts_to_str(self.birthdate)
        )

@dataclass
class UserDataApi:
    internal_id: str
    name: str
    surname: str
    birthdate: int

@dataclass
class UserDataUI:
    name: str
    surname: str
    birthdate: str


user1 = UserData(
    internal_id= "aaaaaa",
    name= "david",
    surname= "garcia",
    birthdate= 14565783543
)

@pytest.mark.parametrize(
    "user_data",
    [
        (
            user1.to_api()
        )
    ]
)
def test_create_user_api():
    pass


@pytest.mark.parametrize(
    "user_data",
    [
        (
            user1.to_ui()
        )
    ]
)
def test_create_user_ui():
    pass

def test_create_api_check_web():
    create_user_api(user1.to_api())
    user_data = get_user_data_ui()
    assert user1.to_ui() == user_data

api_model = {}

cost_model = {"CPU": "Usage", "cost": {"currency": "USD" } }