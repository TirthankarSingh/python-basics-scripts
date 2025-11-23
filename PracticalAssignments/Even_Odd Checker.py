
def even_odd_check():
    try:
        num = int(input("Input the number to be checked: "))
        return "Even" if num % 2 == 0 else "odd"
    except ValueError:
        return "invalid input"
