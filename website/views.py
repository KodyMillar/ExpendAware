from flask import Blueprint, request, redirect, url_for, render_template
from .models import Expense, Category
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # -----------------------------------
        # Gets the expense from the HTML
        # -----------------------------------
        n_descr = request.form.get('descr') 
        n_amount = request.form.get('amount') 
        n_category = request.form.get('name')
        n_category_exp = request.form.get('category_name')
        n_budget = request.form.get('budget')

        # -----------------------------------
        # Provides the schema for the expense
        # -----------------------------------
        if n_descr and n_category_exp and n_amount:
            new_expense = Expense(descr=n_descr, amount=n_amount, category_name=n_category_exp)
            db.session.add(new_expense)
        
        if n_category and n_budget:
            new_category = Category(name=n_category, budget=n_budget)
            db.session.add(new_category)    
        
        # -----------------------------------
        # Adds new expense to the database
        # -----------------------------------
        db.session.commit()

        return redirect(url_for('views.home'))

    # -----------------------------------
    # Extracts data from database
    # -----------------------------------
    expenses = Expense.query.all()
    categories = Category.query.all()

    return render_template("home.html", expenses=expenses, categories=categories)