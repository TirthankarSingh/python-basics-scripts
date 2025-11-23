def min_max_sum_list():
    try:
        data = input("Enter numbers separated by spaces: ")
        l1=[]
        for i in data.split():
            l1.append(int(i))
        return "Min: ", min(l1), "max: ", max(l1), "sum: ", sum(l1)
    except ValueError:
        return "invalid Input"

