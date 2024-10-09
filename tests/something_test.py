import requests
from configuration import SERVICE_URL
from src.global_enums import GlobalErrorMassages

def test_get_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print(received_posts)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMassages.WRONG_ELEMENT_COUNT.value
