def evenEvens(numbers):
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    evenEvens([6,3,5,6,7,2,5,6])

