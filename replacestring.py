original_string = input("Enter a string: ")

# Store original string for display
print("\nOriginal String:", original_string)


pos_replace = int(input("Enter position to replace (starting from 0): "))
new_char = input("Enter new character: ")

if 0 <= pos_replace < len(original_string):
    replaced_string = (
        original_string[:pos_replace] +
        new_char +
        original_string[pos_replace + 1:]
    )
else:
    replaced_string = original_string
    print("Invalid position for replacement.")

print("After Replacement:", replaced_string)


pos_delete = int(input("Enter position to delete (starting from 0): "))

if 0 <= pos_delete < len(replaced_string):
    deleted_string = (
        replaced_string[:pos_delete] +
        replaced_string[pos_delete + 1:]
    )
else:
    deleted_string = replaced_string
    print("Invalid position for deletion.")

print("After Deletion:", deleted_string)