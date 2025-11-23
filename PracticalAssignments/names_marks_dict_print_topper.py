def topper(**kwargs):
    max_marks = max(kwargs.values())
    d1={}
    for k, v in kwargs.items():
        if kwargs.get(k) == max_marks:
            d1.update({k:max_marks})
    return d1
