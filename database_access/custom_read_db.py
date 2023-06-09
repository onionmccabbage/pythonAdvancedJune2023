import sqlite3

def customRead():
    '''Ask which creature to show'''
    invalid = True
    while invalid:
        which_creature = input('which creature? ')
        if type(which_creature==str) and which_creature !='':
            invalid = False # quit the while loop
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # SQL = will return exact match
    # SQL LIKE allows wildcards (%)
    # in SQL queries we can use '=' or 'IS'
    # or we can use wild-cards:
    # LIKE will ignore case
    # LIKE "s%" anything beginning s
    # LIKE "%s" anything ending s
    # LIKE "%s%" anything containing s
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature LIKE "%{which_creature}%"
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