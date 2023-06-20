import sqlite3

# we only need to run this ONCE to make the table in the database
def readDB():
    '''create or access a database then populate a table for zoo creeatures'''
    conn = sqlite3.connect('my_db') # either create or connect to existing db
    curs = conn.cursor() # access the db e.g. to execute SQL statements
    # we need an SQL statement
    st = '''
    SELECT creature, count, cost FROM zoo
    '''
    # apply the SQL to the DB
    try:
        curs.execute(st) # at this point the SQL is sent to the database
        conn.commit()    # ... any changes will now be commited
        # we can now read back our data
        rows = curs.fetchall()
        conn.close()     # tidy up
    except Exception as err:
        print(f'Problem: {err}')
    # we can print the returned data
    for animal in rows:
        print( f'we have {animal[1]} {animal[0]} each costing {animal[2]}' )

if __name__ == '__main__':
    readDB()