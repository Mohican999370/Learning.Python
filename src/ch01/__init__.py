def read_array():
    input_string = input("Enter the elements separated by spaces: ");
    tokens = input_string.split(" ");
    return [int(token) for token in tokens];