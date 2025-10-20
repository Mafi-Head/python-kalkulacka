def get_values():
    a = float(input("Zadejte číslo A: "))
    b = float(input("Zadejte číslo B: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# TODO: Implementujte funkci násobení
def multiply(a, b):
    # return a * b
    pass

# TODO: Implementujte funkci dělení
def divide(a, b):
    # if b == 0:
    #     return "Nelze dělit nulou!"
    # return a / b
    pass


if __name__ == "__main__":
    a, b = get_values()
    print("Součet:", add(a, b))
    print("Rozdíl:", subtract(a, b))
    # print("Součin:", multiply(a, b))
    # print("Podíl:", divide(a, b))
