import sqlite3


def populateDB(creatures_t):
    '''create or access a database then populate a table for zoo creeatures'''
    conn = sqlite3.connect('my_db') # either create or connect to existing db
    curs = conn.cursor() # access the db e.g. to execute SQL statements
    # we need an SQL statement - use ? as a wild-card
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    # apply the SQL to the DB
    # iterate over the creatures we will be inserting
    for item in creatures_t:
        try:
            # validate our data members
            if type(item['creature']==str):
                n = item['creature']
            else:
                raise Exception('Creature name must be a string')
            if type(item['count']==int):
                count = item['count']
            else:
                raise Exception('Creature count must be an integer')
            if type(item['cost']==float):
                cost = item['cost']
            else:
                raise Exception('Creature cost must be a float')
            # inject our values into the SQL statement
            # NB we could call executemany()
            curs.execute(st, (n, count, cost)) # at this point the SQL is sent to the database
            conn.commit()    # ... any changes will now be commited
        except Exception as err:
            print(f'Problem: {err}')
    # after all the work, we close the db connection
    # careful - if there was an exception, there will be nothing to close...
    if conn:
        conn.close()

if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )  
    populateDB(creatures_t)