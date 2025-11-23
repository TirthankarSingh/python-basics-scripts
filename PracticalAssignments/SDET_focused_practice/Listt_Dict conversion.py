items = ["apple", "banana", "cherry"]


def dict_conversion():
    if not items:
        return "Empty List"
    d1={}
    for i in range(1,len(items)+1):
        d1.update({i:items[i-1]})
    print(d1)

dict_conversion()
