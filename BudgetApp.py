import sqlite3
import datetime as dt

# produce a sample script first as a baseline to conver to a full application
class Budget():
    def __init__(self, income_yr):
        self.income_yr = income_yr
        self.income_mo = self.income_yr/12
        self.init_budget()
        self.init_expenses()           

    def init_budget(self):
        '''
        initialize new table to produce the projected budget if non-existant
        - parameters should include monthly or yearly budget
        - if monthly budget, interpolate into yearly budget
        '''
        conn = sqlite3.connect('budgetapp.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS budget(
                    kind TINYTEXT, 
                    amount INT, 
                    category TINYTEXT)''')

        first_budget = ('kind', self.income_yr, 'total')
        c.execute('''INSERT INTO budget 
            VALUES (?,?,?)''', first_budget)
        conn.close()

    def init_expenses(self):
        '''
        initialize table with fields: kind (earning or expense), amount, category, note, date if non-existant
        - date is format YYYY-MM-DD
        '''
        conn = sqlite3.connect('budgetapp.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    kind TINYTEXT,
                    amount FLOAT(10,2),
                    category TINYTEXT, 
                    note TEXT, 
                    date DATE)''')
        conn.close()

    def log(self, kind, amount, category, date, note=''):
        '''
        add an entry to a earnings/expenses table
        - only allows for one entry at a time
        '''
        conn = sqlite3.connect('budgetapp.db')
        c = conn.cursor()
        c.execute('''INSERT INTO expenses
                    VALUES (?,?,?,?,?)''', (kind, amount, category, note, date))
        conn.commit()
        conn.close()

    # def view_expense(self):
    #     '''
    #     view expense table
    #     '''
    #     conn = sqlite3.connect('budgetapp.db')
    #     c = conn.cursor()
    #     for row in c.execute('SELECT * FROM expenses'):
    #         print(row)

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
    new_budget = Budget(83000)
    print('hello')

    conn = sqlite3.connect('budgetapp.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    for row in c.fetchall():
        print(row)
    conn.close()
