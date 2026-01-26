# funtion to count frequency in a string

def frequency(s):
    # creat a dictionary to store frequency
    #of each character

    s = s.lower()
    d = {}

    for i in range(len(s)):
        #check if character is already in dictionary
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d

#driver code

inp = input("Enter a string: ")
print("Frequency of each character in the string:")
print(frequency(inp))            