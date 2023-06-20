# we can write to a file like this
fout = open('snip.txt', 'a') # 'a' will append to the text file
# we have a file access object (through which we access the actual file)
print( 'here is some content', file=fout )
fout.close() # always a good idea to tidy up

# often we need more control over writing to a file
def writeToTextFile(text):
    '''use a file access object to write lots of text content'''
    try:
        # 'xt' will only work if there is (e)xclusive file access
        fout = open('my_log.txt', 'w') # 'wt' will (over)write, 'at' will append text (text is the default)
        size = len(text)
        offset = 0
        chunk  = 12
        while True: # this is a never ending loop
            if offset > size:
                fout.write('\n') # we end our otuput with a new line character
                break # this will stop the while loop
            else:
                # use slicing to output a part of the whole text
                fout.write( text[offset:offset+chunk] )
                offset += chunk
    # handle specific exceptions
    except FileExistsError as err:
        print(f'The file already exists {err}')
    # end up with a catch-all for any other exceptions
    except Exception as err:
        print( f'Something went wrong: {err}' )
    finally: # this will always run, even if an exception occurs 
        pass

if __name__ == '__main__':
    t = 'we can persist very long strings of characters in a text file'
    writeToTextFile(t)