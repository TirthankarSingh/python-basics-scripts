def menu_driven():
    try:
        event = True
        l=[]
        while event:
            task = int(input("Enter the required option, Enter 1 to Add item, Enter 2 to Remove item, Enter 3 to View "
                             "items and 4 to Exit"))

            if 0 < task < 5:
                if task == 1:
                    l.append(input("Enter what you want to add"))
                elif task == 2:
                    l.remove(input("Enter what you want to remove"))
                elif task == 3:
                    print(l)
                elif task == 4:
                    event = False
            else:
                print("Invalid Input")
    except ValueError:
        return "Invalid Input"



