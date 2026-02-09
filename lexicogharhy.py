# program to demonstrate lexicographical comparison of strings in Python

def nextWord(s):

    #if string is empty
    if (s==""):
        return "a"
    
    #find the first character from the end which is not 'z'
    i = len(s) - 1
    while (s[i] == 'z' and i >= 0):
        i -= 1

    #if all characters are 'z' append
    #an 'a' at the end of string
    if (i == -1):
        s = s + 'a'

    # if there are some non z characters
    # else:
    s = s.replace(s[i], chr(ord(s[i]) + 1 ), 1)

    return s

inp = input("Enter a string: ")
print(nextWord(inp))        