def word_counter():
    try:
        s1=str(input("Enter a sentence: ")).split()
        d1={}
        for i in s1:
            if i not in d1:
                d1.update({i:s1.count(i)})
        return d1
    except ValueError:
        return "Invalid Input"

print(word_counter())

