import json # this library lets us use JSON in Python

def main():
    '''load a JSON file'''
    try:
        fin = open('todos.json', 'rt')
        all_j = fin.read()
        print( type(all_j) ) # str
        # we can convert the string to a structure ( a list )
        all_l = json.loads(all_j)
        print(all_l, type(all_l))
    except Exception as err:
        print(f'problem {err}')

if __name__ == '__main__':
    main()