"""asdasd"""
def print_number_sequence(count):
    """asdasd"""
    numbers = [int(i) for i in range(1, count+1)]
    for i, j in enumerate(numbers):
        numbers[i] = j**2
    sequence = " ".join(str(numbers))
    print(sequence)
print_number_sequence(int(input()))
