def even_odd():
    try:
        r1 = int(input("Enter lower range for even odd"))
        r2 = int(input("Enter highest range for even odd"))
        even = []
        odd = []
        for i in range(r1, r2 + 1):
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return "Even: ", even, "Odd: ", odd
    except ValueError:
        return "Invalid Input"


print(even_odd())
