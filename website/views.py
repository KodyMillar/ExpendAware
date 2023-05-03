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
        n_category = request.form.get('category')

        # -----------------------------------
        # Provides the schema for the expense
        # -----------------------------------
        new_expense = Expense(descr=n_descr, amount=n_amount)
        
        # -----------------------------------
        # Adds new expense to the database
        # -----------------------------------
        db.session.add(new_expense)
        db.session.commit()

        return redirect(url_for('views.home'))

    # -----------------------------------
    # Extracts data from database
    # -----------------------------------
    expenses = Expense.query.all()

    return render_template("home.html", expenses=expenses)