import sqlite3

def customUpdate():
    '''update members of the database'''
    invalid = True
    while invalid:
        which_creature = input('Which creature meeds updating? ')
        if type(which_creature)== str and which_creature != '':
            invalid = False
    # we should also validate the qty
    qty = int(float(input('What is the updated quantity? ')))

    conn = sqlite3.connect('my_db') # either create or connect to existing db
    curs = conn.cursor() # access the db e.g. to execute SQL statements
    # we need an SQL statement - use ? as a wild-card
    st = f'''
    UPDATE zoo
    SET count={qty}
    WHERE creature = "{which_creature}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(f'Problem: {err}')

if __name__ == '__main__':
    customUpdate()
