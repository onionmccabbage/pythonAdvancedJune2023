import sqlite3

def customUpdate():
    '''update members of the database'''
    
    conn = sqlite3.connect('my_db') # either create or connect to existing db
    curs = conn.cursor() # access the db e.g. to execute SQL statements
    # we need an SQL statement - use ? as a wild-card
    st = '''

    '''

if __name__ == '__main__':
    customUpdate()
