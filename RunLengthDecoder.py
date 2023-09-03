def run_length_decoding(encoded_string):
    decoded_string = ''
    i = 0
    
    while i < len(encoded_string):
        count = int(encoded_string[i])
        char = encoded_string[i + 1]
        decoded_string += char * count
        i += 2
    
    return decoded_string

print(run_length_decoding(input()))
