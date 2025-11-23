def reverseString():
    data = input("Enter the string")
    reversedString = ""
    for i in reversed(data):
        reversedString += i
    return reversedString
