def changeTheCase(s):
    result = ""
    for i in s:

        if i.islower():
            result += i.upper()

        if i.isupper():
            result += i.lower()

    return result

inp = input("Enter a string: ")
print("String after changing the case:")
print(changeTheCase(inp))                