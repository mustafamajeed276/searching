def checkPalindrome(s):

    s = s.lower()
    rev_string = reverse(s)
    if s == rev_string:
        return True
    else:
        return False
    
inp = input("Enter a string: ")
print(checkPalindrome(inp))    