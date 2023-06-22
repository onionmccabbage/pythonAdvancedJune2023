from collections import deque

# a deque allows access to BOTH ends
def palindrome(word):
    '''check to see if the word is a palindrome'''
    dq = deque(word) # we now have a double-ended queue
    while len(dq)>1:
        if dq.popleft() != dq.pop(): # deque also has append and appendleft
            return False
        return True

if __name__ =='__main__':
    print( palindrome('tenet') )
    print( palindrome('madam') )
    print( palindrome('racecar') )
    print( palindrome('done') ) # False