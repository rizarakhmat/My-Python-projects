import pytest
from examone_py import app

def test_ok(client):
    rv = client.get('/dice?k=2&n=6')
    assert rv.status_code == 200

def test_more6(client):
    rv = client.get('/dice?k=3&n=9')
    assert rv.status_code == 400

def test_ko(client):
    rv = client.get('/dice?k=0&n=-1')
    assert rv.status_code == 400
