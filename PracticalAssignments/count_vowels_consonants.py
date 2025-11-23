def count_vowels_consonants():
    data = input("Enter the sentence")
    if len(data) == 0:
        return "No input data"
    v1=["a", "e", "i", "o", "u"]
    v=0
    c=0
    for i in data:
        if i.isalpha() and i.lower() in v1:
            v+=1
        elif i.isalpha():
            c+=1
    return "vowels: ", v, "consonants: ", c

