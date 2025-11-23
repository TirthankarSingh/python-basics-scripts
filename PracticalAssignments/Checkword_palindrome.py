def palindrome():
    data = input("Enter the string")
    reversedString = ""
    for i in reversed(data):
        reversedString += i
    return "palindrome" if data == reversedString else "not palindrome"
