def multiply(a, b):
    return a * b


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"{a} * {b} = {multiply(a, b)}")


if __name__ == "__main__":
    main()
