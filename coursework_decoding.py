import numpy as np


def decode_message(received, H):
    correlations = np.dot(H, received)
    decoded_index = np.argmax(correlations)
    return decoded_index


def hadamard_matrix(order):
    if order == 1:
        return np.array([[1]])
    else:
        H_n_minus_1 = hadamard_matrix(order // 2)
        top = np.hstack((H_n_minus_1, H_n_minus_1))
        bottom = np.hstack((H_n_minus_1, -H_n_minus_1))
        return np.vstack((top, bottom))


def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return binary_str


def to_letters(binary_array):
    s = ''
    binary_string = ''.join([str(bit) for bit in binary_array])
    decimal_value = int(binary_string, 2)
    s += chr(decimal_value)
    return (s)


def main():
    input_string = input("Введите зашифорванный код: ")
    input_string = input_string[:-1]
    numbers_list = input_string.split('n')
    numbers_array = []
    order = 2048
    H = hadamard_matrix(order)

    for input_str in numbers_list:
        numbers = []
        num_str = ""
        is_negative = False
        for char in input_str:
            if char.isdigit():
                num_str += char
            elif char == '-':
                is_negative = True
            if num_str:
                if is_negative:
                    num_str = "-" + num_str
                    is_negative = False
                numbers.append(int(num_str))
                num_str = ""

        numbers_array.append(np.array(numbers))

    for num in numbers_array:
        decode1 = decode_message(num, H)
        decode2 = decimal_to_binary(decode1)
        letter = to_letters(decode2)
        print(letter)


main()
