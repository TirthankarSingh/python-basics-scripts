def remove_duplicates():
    try:
        data = input("input list values space separated").split()
        if len(data) == 0:
            return "empty list"
        unique_list=[]
        for i in range(len(data)):
            if data[i] not in unique_list:
                unique_list.append(data[i])
        return unique_list
    except Exception as e:
        return "Invalid Input"
