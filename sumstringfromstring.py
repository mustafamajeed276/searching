strng = input("Enter a string: ")
given_strng = input("Enter a string to search: ")
if given_strng in strng:
    print(f"The string '{given_strng}' is found in the given string.")
else:
    print(f"The string '{given_strng}' is not found in the given string.")
