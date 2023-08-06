import pytest
import requests

def getname(id):
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    data = res.json()
    return data['name']

@pytest.mark.parametrize('id, expected_name', [(1, 'Leanne Graham'), (4, 'Patricia Lebsack')])
def test_username(id, expected_name):
    assert getname(id) == expected_name
