def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")


if __name__ == "__main__":
    main()
