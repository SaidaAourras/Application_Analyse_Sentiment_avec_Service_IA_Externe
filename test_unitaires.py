import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

fake_data = {'username':'newUser', 'password':'123456'}
@pytest.fixture()
def token():
    response = client.post('/login', json=fake_data)
    data = response.json()
    return data['access_token']

# print(token())

def test_predict_sentiment(token):
    response = client.post('/sentiment',json={'comment':'nice product'},headers={'Authorization':f'Bearer {token}'})
    assert response.status_code == 200