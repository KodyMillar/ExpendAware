import pytest
import json
from main import app, update_categories_budgets

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"ExpendAware - Home" in response.data
    assert b"Total Budget:" in response.data
    assert b"Total Expenses:" in response.data

def test_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200

def test_expenses(client):
    response = client.get('/expenses')
    assert response.status_code == 200
    assert b"ExpendAware - Expense" in response.data
    assert b"Original Budget:" in response.data
    assert b"Remaining Budget:" in response.data

def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_transfer(client):
    response = client.get('/transfer')
    assert response.status_code == 200

def test_cost(client):
    response = client.get('/cost')
    assert response.status_code == 200

def test_history(client):
    response = client.get('/history')
    assert response.status_code == 200

def test_statistic(client):
    response = client.get('/statistic')
    assert response.status_code == 200

def test_update_categories_budgets():
    categories = [{"category": "Food", "total_budget": 0, "remaining_budget": 0}]
    budgets = [{"category": "Food", "amount": 100}]
    expenses = [{"category": "Food", "amount": 50}]
    updated_categories = update_categories_budgets(categories, budgets, expenses)
    assert updated_categories[0]['total_budget'] == 100
    assert updated_categories[0]['remaining_budget'] == 50
