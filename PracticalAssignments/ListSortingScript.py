def sortedlist():
    try:
        data = input("Enter numbers separated by spaces: ")
        l1=[]
        for i in data.split():
            l1.append(int(i))
        return "ascending:", sorted(l1), "descending", sorted(l1, reverse=True)
    except ValueError:
        return "Invalid List"


print(sortedlist())
