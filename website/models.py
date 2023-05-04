from . import db

class Category(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    budgets = db.relationship('Budget')
    expenses = db.relationship('Expense')


class Budget(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    amount = db.Column(db.Integer)
    category_name = db.Column(db.String(50), db.ForeignKey('category.name'))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descr = db.Column(db.String(100))
    price = db.Column(db.Integer)
    category_name = db.Column(db.String(50), db.ForeignKey('category.name'))