import sqlite3
import datetime as dt

# produce a sample script first as a baseline to conver to a full application
class Budget():
    def __init__(self, income_yr):
        self.income_yr = income_yr
        self.income_mo = self.income_yr/12
        # self.categories = [kind, amount, category, note, date]
        self.init_budget()
        self.init_expenses()
        pass            

    def init_budget(self):
        '''
        initialize new table to produce the projected budget if non-existant
        - parameters should include monthly or yearly budget
        - if monthly budget, interpolate into yearly budget
        '''
        conn = sqlite3.connect('budgetapp.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE budget(
                    kind TINYTEXT, 
                    amount INT, 
                    category TINYTEXT)''')
        pass

    def init_expenses(self):
        '''
        initialize table with fields: kind (earning or expense), amount, category, note, date if non-existant
        - date is format YYYY-MM-DD
        '''
        conn = sqlite3.connect('budgetapp.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE expenses (
                    kind TINYTEXT,
                    amount FLOAT(,2),
                    category TINYTEXT, 
                    note TEXT, 
                    date DATE)''')
        pass

    def log(self, kind, amount, category, note, date):
        '''
        add an entry to a earnings/expenses table
        - only allows for one entry at a time
        '''
        conn = sqlite3.connect('budgetapp.db')
        c = conn.cursor()
        c.execute('''INSERT INTO expenses
                    VALUES (?,?,?,?,?)''', (kind, amount, category, note, date))
        pass

    def add_category(self, category):
        '''
        add category or categories to budget and earnings/expenses tables
        - food, transportation, rent, savings, entertainment
        '''
        pass



    def compare(self):
        '''
        compare current budget trajectory to projected budget
        - provide percent difference i.e. current budget/projected budget * 100
        '''
        pass

    def project_budget(self):
        '''
        given current spending and earning, project new budget to meet original budget
        - take remaining budget space and normalize over time remaining
        '''
        pass


if __name__ == "__main__":
    pass