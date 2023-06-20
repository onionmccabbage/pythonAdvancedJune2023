# we can also write and read byte files 

def makeBytes(values):
    '''make a byte string froom the values'''
    b = bytes(values)
    # print(b)
    return b

def writeBytes(b):
    '''write bytes to a file'''
    try:
        fout = open('bfile', 'wb') # 'w' will (over)write 'b' for bytes
        fout.write(b)
        fout.close()
    except Exception as err:
        print(f'oops {err}')

def readBytes():
    '''retrieve bytes from a byte file'''
    fin = open('bfile', 'rb')
    retrieved_b = fin.read()
    fin.close()
    return retrieved_b


if __name__ == '__main__':
    v = range(0, 256)
    b = makeBytes(v)
    writeBytes(b)
    r = readBytes()
    print(  ) # this will attempt to print bytes...
