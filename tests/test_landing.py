import pytest
from app import app


def test_index_route():
    response = app.test_client().get('/basepath')

    assert response.status_code == 200
    assert response.data.decode('utf-8').__contains__('Hello from Flask!')
