from flask import render_template, request, redirect, url_for, flash, current_app as app
from app import db
from .models import Budget, Income, Investment
from .utils import import_csv

@app.route('/')
def index():
    budgets = Budget.query.all()
    incomes = Income.query.all()
    investments = Investment.query.all()
    print(incomes)
    return render_template('index.html', budgets=budgets, incomes=incomes, investments=investments)

@app.route('/import', methods=['POST'])
def import_data():
    files = request.files.getlist('file')
    for file in files:
        import_csv(file)
    flash('Data imported successfully!', 'success')
    return redirect(url_for('index'))
