"""Ejudge"""
def run_length_encoding(input_string):
    """Encoder"""
    encoded_string = ''
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += str(count) + input_string[i - 1]
            count = 1
    encoded_string += str(count) + input_string[-1]
    return encoded_string

print(run_length_encoding(input()))
