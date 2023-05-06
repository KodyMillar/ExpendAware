from flask import Flask, request, jsonify, render_template
import json
from datetime import datetime

app = Flask(__name__)


def update_categories_budgets(categories, budgets, expenses):
    for category in categories:
        category['total_budget'] = 0
        category['remaining_budget'] = 0
        for budget in budgets:
            if budget['category'] == category['category']:
                category['total_budget'] += int(budget['amount'])
                category['remaining_budget'] += int(budget['amount'])
        for expense in expenses:
            if expense['category'] == category['category']:
                category['remaining_budget'] -= int(expense['amount'])
    return categories

@app.route('/', methods=['GET', 'POST'])
def index():
    with open("expense.json", "r") as f:
        existing_expense = json.load(f)
    with open("category.json", "r") as f:
        existing_category = json.load(f)    
    with open("budget.json", "r") as f:
        existing_budget = json.load(f)

    # Initialize the variables with default values
    descr = ''
    amount = 0
    category = ''
    name = ''

    # Append the new data to the existing data
    if request.method == 'POST':
        if 'descr' in request.form and 'amount' in request.form and 'category' in request.form:
            descr = request.form['descr']
            amount = request.form['amount']
            category = request.form['category']
            new_expense = {
                "descr": descr,
                "amount": amount,
                "category": category
            }
            existing_expense.append(new_expense)
        elif 'name' in request.form and 'amount' in request.form and 'category' in request.form:
            name = request.form['name']
            amount = request.form['amount']
            category = request.form['category']
            new_budget = {
                'name': name,
                'amount': amount,
                'category': category
            }
            existing_budget.append(new_budget)
        elif 'category' in request.form:
            category = request.form['category']
            new_category = {
                'category': category
            }
            existing_category.append(new_category)

    # Write the entire data object back to the file
    with open("expense.json", "w") as f:
        json.dump(existing_expense, f)
    with open("category.json", "w") as f:
        json.dump(existing_category, f)
    with open("budget.json", "w") as f:
        json.dump(existing_budget, f)
    expenses = existing_expense
    categories = existing_category
    budgets = existing_budget

    #get total budget and total expenses
    total_budget = 0
    total_expenses = 0
    with open("category.json", "r") as file:
        categories = json.load(file)
    
    for category in categories:
        total_budget += category['total budget']

    categories = update_categories_budgets(categories, budgets, expenses)
    return render_template('index.html', expenses=expenses, categories=categories, budgets=budgets, total_budget=total_budget, total_expenses=total_expenses)
    

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    with open("category.json", "r") as file:
        category_list = json.load(file)
    categories = category_list
    total_budget_list = category_list

    with open("budget.json", "r") as file:
        budget_list = json.load(file)

    for category in total_budget_list:
        category["total budget"] = 0
        for budget in budget_list:
            if budget["category"] == category["category"]:
                category["total budget"] += int(budget["amount"])
    
    with open("category.json", "w") as file:
        json.dump(total_budget_list, file)
    
    current_date = datetime.now()
    return render_template("categories.html", categories=categories, budgets=total_budget_list, current_date=current_date)


@app.route('/expenses')
def expenses():
    with open("expense.json", "r") as f:
        existing_expense = json.load(f)
    with open("category.json", "r") as f:
        existing_category = json.load(f)
    with open("budget.json", "r") as f:
        existing_budget = json.load(f)

    expenses = existing_expense
    categories = existing_category
    budgets = existing_budget

    categories = update_categories_budgets(categories, budgets, expenses)

    return render_template('expenses.html', categories=categories)


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
