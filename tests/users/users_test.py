import requests
from src.baseclasses.response import Response
from src.pydantic_schemas.user import User

from configuration import SERVICE_URL2

#resp = requests.get(SERVICE_URL2)

def test_get_user_list(get_users, calculate):
    Response(get_users).assert_status_code(200).validate(User)
    print(get_users)
    print(calculate)
    print(calculate(1, 1))


def test_another():
    assert 1 == 1