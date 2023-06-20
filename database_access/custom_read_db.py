import sqlite3

def customRead():
    '''Ask which creature to show'''
    invalid = True
    while invalid:
        which_creature = input('which creature? ')
        if type(which_creature==str and which_creature !=''):
            invalid = False # quit the while loop
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature = "{which_creature}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close()
    except Exception as err:
        print('problem: {err}')
    # show any retrieved creatures
    for animal in rows:
        print( f'we have {animal[1]} {animal[0]} costing {animal[2]}' )

if __name__ == '__main__':
    customRead()