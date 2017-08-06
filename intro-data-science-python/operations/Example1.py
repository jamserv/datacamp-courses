def example1():
    # Addition and subtraction
    print(5 + 5)
    print(5 - 5)

    # Multiplication and division
    print(3 * 5)
    print(10 / 2)

    # Exponentiation
    print(4 ** 2)

    # Modulo
    print(18 % 7)

    # How much is your $100 worth after 7 years?
    x = 100 * 1.1 ** 7
    y = 100 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1

    print x
    print y
    
def listReverse():
    # Create lists first and second
    first = [11.25, 18.0, 20.0]
    second = [10.75, 9.50]

    # Paste together first and second: full
    full = first + second

    # Sort full in descending order: full_sorted
    full_sorted = sorted(full, reverse=True)

    # Print out full_sorted
    print(full_sorted)
    
example1()