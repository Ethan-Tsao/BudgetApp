import sqlite3 as db
import datetime as dt

# produce a sample script first as a baseline to conver to a full application

def init_db():
    '''
    initialize database with budget and expenses tables
    '''
    pass

def init_budget():
    '''
    initialize new table to produce the projected budget if non-existant
    - parameters should include monthly or yearly budget
    - if monthly budget, interpolate into yearly budget
    '''
    pass

def init_expenses():
    '''
    initialize table with fields: type (earning or expense), amount, category, note, date if non-existant
    '''
    pass

def add_categories():
    '''
    add category or categories to budget and earnings/expenses tables
    '''

def log():
    '''
    add an entry to a earnings/expenses table
    '''

def compare():
    '''
    compare current budget trajectory to projected budget
    - provide percent difference i.e. current budget/projected budget * 100
    '''

def project_budget():
    '''
    given current spending and earning, project new budget to meet original budget
    - take remaining budget space and normalize over time remaining
    '''



if __name__ == "__main__":
    pass