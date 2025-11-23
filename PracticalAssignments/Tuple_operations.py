def tuple_operation():
    data = tuple(input("Enter the elements separated by space ").split())
    if len(data) == 0:
        return "No data"
    print("length of tuple is: ", len(data))
    print("First element: {}, last element: {}".format(data[0], data[-1]))
    i = input("enter the element to be counted")
    if i in data:
        print("count is:", data.count(i))
    else:
        print(i+" not in tuple ")

