import json # this library lets us use JSON in Python

def main():
    '''load a JSON file'''
    try:
        fin = open('todos.json', 'rt')
        all_j = fin.read()
        print( type(all_j) ) # str
        # we can convert the string to a structure ( a list )
        all_l = json.loads(all_j) # loads ALL the json 
        # part_d = json.load(all_j)[0] # loads just element 0
        print(all_l, type(all_l) ) #, part_d, type(part_d))
    except Exception as err:
        print(f'problem {err}')

def makeJSON(d):
    '''take a structure and convert it to JSON'''
    d_j = json.dumps(d)
    print( d_j, type(d_j) )

if __name__ == '__main__':
    main()
    d = [{'n':'Ada'}, {'n':'Timnit'}]
    makeJSON(d)