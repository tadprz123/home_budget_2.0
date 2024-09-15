import pandas as pd
from . import db
from .models import Budget, Income, Investment

def import_csv(file):
    data = pd.read_csv(file)
    if 'Category' in data.columns:
        for index, row in data.iterrows():
            budget_entry = Budget(date=row['Date'], category=row['Category'], amount=row['Amount'])
            db.session.add(budget_entry)
    elif 'Source' in data.columns:
        for index, row in data.iterrows():
            income_entry = Income(date=row['Date'], source=row['Source'], amount=row['Amount'])
            db.session.add(income_entry)
    elif 'Type' in data.columns:
        for index, row in data.iterrows():
            investment_entry = Investment(date=row['Date'], type=row['Type'], amount=row['Amount'])
            db.session.add(investment_entry)
    db.session.commit()
