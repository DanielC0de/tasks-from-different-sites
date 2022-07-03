def max_digit(number: int) -> int:
    return max([int(a) for a in str(number)])


number = 12345
print(max_digit(number))
