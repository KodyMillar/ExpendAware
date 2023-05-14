from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import json
from datetime import datetime
import pprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'


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

# Check for errors in user input
def validate_amount(amount):
    try:
        int(amount)
    except ValueError:
        return False
    if int(amount) < 0 or amount == "":
        return False
    return True

def check_for_existing(name_input, existing_list, criteria):
    for listing in existing_list:
        if name_input.lower() == listing[criteria].lower():
            return False
    return True

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
    current_date = datetime.now().strftime("%d %b %Y")

    # Append the new data to the existing data
    if request.method == 'POST':
        if 'descr' in request.form and 'amount' in request.form and 'category' in request.form:
            descr = request.form['descr']
            amount = request.form['amount']
            category = request.form['category']

            if validate_amount(amount) == True:
            
                new_expense = {
                    "descr": descr,
                    "amount": amount,
                    "category": category
                }
                existing_expense.append(new_expense)
                for category in existing_category:
                    if category['category'] == new_expense['category']:
                        category['total expenses'] += int(new_expense['amount'])
        elif 'name' in request.form and 'amount' in request.form and 'category' in request.form:
            name = request.form['name']
            amount = request.form['amount']
            category = request.form['category']

            if validate_amount(amount) == True and name != "":
            
                new_budget = {
                    'name': name,
                    'amount': amount,
                    'category': category
                }
                existing_budget.append(new_budget)
        elif 'category' in request.form:
            category = request.form['category']
            
            if category != "" and check_for_existing(category, existing_category, "category"):
            
                new_category = {
                    'category': category,
                    'total budget': 0,
                    'total expenses': 0,
                    'date': current_date
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

    #get total budget 
    total_budget = 0
    with open("category.json", "r") as file:
        categories = json.load(file)
    
    for category in categories:
        total_budget += category['total budget']

    #get total expenses
    total_expenses = 0
    category_usage_percentage = 0

    for category in categories:
        total_expenses += category['total expenses']
    

    categories = update_categories_budgets(categories, budgets, expenses)
    return render_template('index.html', 
        expenses=expenses, 
        categories=categories, 
        budgets=budgets, 
        total_budget=total_budget, 
        total_expenses=total_expenses
        )


@app.route('/categories', methods=['GET', 'POST'])
def categories():

    # Get information from category and budget json files
    with open("category.json", "r") as file:
        category_list = json.load(file)
    categories = category_list

    with open("budget.json", "r") as file:
        budget_list = json.load(file)

    category_to_delete = ""

    # delete category
    if request.method == "POST":
        category_list = categories
        for category in category_list:
            if category['category'] == list(request.form)[0]:
                new_budget_list = []
                for budget in budget_list:
                    if budget["category"] != category["category"]:
                        new_budget_list.append(budget)
                budget_list = new_budget_list
                category_to_delete = category
                categories.remove(category_to_delete)
                with open("category.json", "w") as file:
                    json.dump(categories, file)
                with open("budget.json", "w") as file:
                    json.dump(new_budget_list, file)
                break

    total_budget_list = categories
    # add budgets to category files
    for category in total_budget_list:
        category["total budget"] = 0
        for budget in budget_list:
            if budget["category"] == category["category"]:
                category["total budget"] += int(budget["amount"])
    
    with open("category.json", "w") as file:
        json.dump(total_budget_list, file)

    return render_template("categories.html", categories=categories, total_budgets=total_budget_list, budgets=budget_list)


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




@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    with open("expense.json", "r") as f:
        existing_expense = json.load(f)
    with open("category.json", "r") as f:
        existing_category = json.load(f)    
    with open("budget.json", "r") as f:
        existing_budget = json.load(f)
    expenses = existing_expense
    categories = existing_category
    budgets = existing_budget

    if request.method == 'POST':

        # Get user input
        budget_from_str = request.form["budget-from"]
        budget_to_str = request.form["budget-to"]
        transfer_amount = request.form['transfer-amount']

        # Fix syntax issue replacing single to double quote
        budget_from_str_fixed = budget_from_str.replace("'", "\"")
        budget_to_str_fixed = budget_to_str.replace("'", "\"")

        # Convert string to dictionary
        budget_from_dict = json.loads(budget_from_str_fixed)
        budget_to_dict = json.loads(budget_to_str_fixed)

        if int(budget_from_dict["amount"]) - int(transfer_amount) >= 0:

            # Change budget
            budget_from_dict["amount"] = int(budget_from_dict["amount"]) - int(transfer_amount)
            budget_to_dict["amount"] = int(budget_to_dict["amount"]) + int(transfer_amount)

            # Update budgets
            for budget in budgets:
                if budget["name"] == budget_from_dict["name"] and budget["category"] == budget_from_dict["category"]:
                    budget["amount"] = budget_from_dict["amount"]
                if budget["name"] == budget_to_dict["name"] and budget["category"] == budget_to_dict["category"]:
                    budget["amount"] = budget_to_dict["amount"]
    
        # Update budgets.json
        with open("budget.json", "w") as f:
            json.dump(budgets, f)
    return render_template('transfer.html', expenses=expenses, categories=categories, budgets=budgets)



@app.route('/login', methods=['GET', 'POST'])
def login():
    with open("login.json", "r") as f:
        existing_user = json.load(f)

    users = existing_user
    newUser = {}

    if request.method == 'POST':
        emailInput = request.form.get("email")
        passwordInput = request.form.get("password")

        nameReg = request.form.get("nickname")
        emailReg = request.form.get("reg-email")
        pwd1Reg = request.form.get("pwd1")
        pwd2Reg = request.form.get("pwd2")


        if nameReg == "":
            for user in users:
                if user["password"] == passwordInput and user["email"] == emailInput:
                    return redirect(url_for("index"))
            
            flash('Incorrect email or password')
            return redirect(url_for('empty'))
        else:
            newUser['name'] = nameReg
            newUser['password'] = pwd1Reg
            newUser['email'] = emailReg
            users.append(newUser)
            with open("login.json", "w") as file:
                json.dump(users, file, indent=2)
            flash(f'${ nameReg } is registered')
            # return redirect(url_for("index"))

    return render_template("login.html")


@app.route('/cost')
def cost():
    return render_template('cost.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/statistic')
def statistic():
    return render_template('statistic.html')

@app.route('/empty')
def empty():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)