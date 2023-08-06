import pytest
import requests

@pytest.fixture()
def username():
    res = requests.get('https://jsonplaceholder.typicode.com/users/1')
    data = res.json()
    return data['name']

def test_username(username):
    assert username == 'Leanne Graham'
