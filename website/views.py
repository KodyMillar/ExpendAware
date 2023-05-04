from flask import Blueprint, request, redirect, url_for, render_template
from .models import Expense, Category, Budget
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # -----------------------------------
        # Gets the expense from the HTML
        # -----------------------------------
        category_name = request.form.get('category_name')

        budget_name = request.form.get('budget_name')
        budget_amount = request.form.get('budget_amount')
        budget_fk_category = request.form.get('budget_fk_category')


        exp_descr = request.form.get('exp_descr') 
        exp_price = request.form.get('exp_price') 
        exp_fk_category = request.form.get('exp_fk_category')

        # -----------------------------------
        # Provides the schema for the expense
        # -----------------------------------
        if category_name:
            new_category = Category(name=category_name)
            db.session.add(new_category)

        if budget_name and budget_amount and budget_fk_category:
            new_budget = Budget(name=budget_name, amount=budget_amount, category_name=budget_fk_category)
            db.session.add(new_budget)
        
        if exp_descr and exp_price and exp_fk_category:
            new_expense = Expense(descr=exp_descr, price=exp_price, category_name=exp_fk_category)
            db.session.add(new_expense)
        
        
        # -----------------------------------
        # Adds new expense to the database
        # -----------------------------------
        db.session.commit()

        return redirect(url_for('views.home'))

    # -----------------------------------
    # Extracts data from database
    # -----------------------------------
    categories = Category.query.all()
    budgets = Budget.query.all()
    expenses = Expense.query.all()

    return render_template("home.html", categories=categories, budgets=budgets, expenses=expenses)