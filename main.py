from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

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

    return render_template('home.html', expenses=expenses, categories=categories, budgets=budgets)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
