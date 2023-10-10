def callme(**kwargs):
    for key, value in kwargs.items():
        print(f"KeyWord {key}, Value {value}")

callme(first="Dera",last="bizboy",age="20")