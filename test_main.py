import json
import pytest
from flask import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from main import app, validate_amount, check_for_existing, update_categories_budgets

def test_validate_amount():
    assert validate_amount('200') == True
    assert validate_amount('300', '100', '500') == True
    assert validate_amount('500', '300', '500') == False
    assert validate_amount('abc') == False
    assert validate_amount('-50') == False

def test_check_for_existing():
    existing_list = [{'category': 'Food'}, {'category': 'Clothing'}, {'category': 'Entertainment'}]
    assert check_for_existing('Food', existing_list, 'category') == False
    assert check_for_existing('Transportation', existing_list, 'category') == True

def test_update_categories_budgets():
    categories = [{'category': 'Food', 'total_budget': 0, 'remaining_budget': 0}]
    budgets = [{'category': 'Food', 'amount': '100'}, {'category': 'Food', 'amount': '50'}]
    expenses = [{'category': 'Food', 'amount': '30'}, {'category': 'Food', 'amount': '20'}]
    result = update_categories_budgets(categories, budgets, expenses)
    assert result[0]['total_budget'] == 150
    assert result[0]['remaining_budget'] == 100

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index_get(client):
    rv = client.get('/')
    assert rv.status_code == 302

def test_categories_get(client):
    rv = client.get('/categories')
    assert rv.status_code == 302

def test_budget_detail_get(client):
    rv = client.get('/categories/Groceries')
    assert rv.status_code == 302


def test_transfer_get(client):
    rv = client.get('/transfer')
    assert rv.status_code == 302
