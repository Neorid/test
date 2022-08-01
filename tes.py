import pytest
import requests
# Самый прост позитивный кейс который проверяем что статус код = 200, и то что ответ world
class TestRegistration:
    def test_registration(self):
        body = {"req": "hello"}
        response = requests.post("http://my.domen/echo", json=body)
        assert response.status_code == 200
        assert response.json().get('resp') == 'world.'
        assert response.json().get('error') == {'error':None}
        print(response.text)