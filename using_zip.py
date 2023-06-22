# in Python zip is NOTHING TO DO with compression

def main():
    ''' we can use zip to combine data structures'''
    days_l   = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    fruits_t = ('Banana', 'Orange', 'Kiwi', 'Durian')
    drinks_s = {'Coffee', 'Tea', 'Water', 'Juice'}
    desserts = ['Crepe', 'Crumble', 'Tiramisu', 'Pancakes']

    # zip will use the minimum length collection for its output
    for day, fruit, drink, dessert in zip(days_l, fruits_t, drinks_s, desserts):
        print(f'On {day} I eat {fruit} with {drink} then {dessert}')

if __name__ == '__main__':
    main()