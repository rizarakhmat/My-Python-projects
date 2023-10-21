import pytest
from math_py import app

def test_add(client):
    rv = client.get('/add?a=1&b=2')
    print(rv)
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 3}

def test_mul(client):
    rv = client.get('/mul?a=1&b=2')
    print(rv)
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}

def test_sub(client):
    rv = client.get('/sub?a=2&b=1')
    print(rv)
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 1}

def test_div(client):
    rv = client.get('/div?a=2&b=1')
    print(rv)
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}

def test_div(client):
    rv = client.get('/div?a=2&b=1')
    print(rv)
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}