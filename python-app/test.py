import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_visitor(client):
    response = client.post('/visitors', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['message'] == 'Visitor added'

def test_get_visitors(client):
    response = client.get('/visitors')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Should return a list

def test_add_visitor_no_name(client):
    response = client.post('/visitors', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Name is required'
