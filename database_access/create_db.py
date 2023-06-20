import sqlite3

# we only need to run this ONCE to make the table in the database
def accessDB():
    '''create or access a database then make a table for zoo creeatures'''
    conn = sqlite3.connect('my_db') # either create or connect to existing db
    curs = conn.cursor() # access the db e.g. to execute SQL statements
    # we need an SQL statement
    st = '''
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost float
    )
    '''
    try:
        curs.execute(st) # at this point the SQL is sent to the database
        conn.commit()    # ... any changes will now be commited
        conn.close()     # tidy up
    except Exception as err:
        print(f'Problem: {err}')


if __name__ == '__main__':
    accessDB()