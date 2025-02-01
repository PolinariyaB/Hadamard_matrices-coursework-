import numpy as np


def text_to_binary(s):
    code1 = []
    for letter in s:
        code1.append([int(x) for x in bin(ord(letter))[-11:]])
    code1 = np.array(code1)
    return code1


def binary_to_decimal(code1):
    decimal_list = []
    for binary_array in code1:
        binary_str = ''.join(str(bit) for bit in binary_array)
        decimal_value = int(binary_str, 2)
        decimal_list.append(decimal_value)
    return np.array(decimal_list)


def hadamard_matrix(order):
    if order == 1:
        return np.array([[1]])
    else:
        H_n_minus_1 = hadamard_matrix(order // 2)
        top = np.hstack((H_n_minus_1, H_n_minus_1))
        bottom = np.hstack((H_n_minus_1, -H_n_minus_1))
        return np.vstack((top, bottom))


def add_noise(codeword, error_index_1, error_index_2):
    noisy_codeword = codeword.copy()
    noisy_codeword[error_index_1] *= -1
    noisy_codeword[error_index_2] *= -1
    return noisy_codeword


def encode_message(message, H):
    codeword = H[message]
    return codeword


def main():
    s = input("Введите сообщение: ")
    code1 = text_to_binary(s)
    list1 = binary_to_decimal(code1)
    noisy_message = []

    H = hadamard_matrix(2048)
    for encoded_letter in list1:
        print(encoded_letter)
        coded_letter = encode_message(encoded_letter, H)
        error_pos = input(f"Введите две позиции ошибок для сообщения, разделенные пробелом: ")
        pos1, pos2 = map(int, error_pos.split())
        noisy_letter = add_noise(coded_letter, pos1, pos2)
        noisy_letter_str = ''.join(str(bit) for bit in noisy_letter)
        print()
        noisy_message.append(noisy_letter_str)
        noisy_message.append("n")
    print("Закодированное сообщение: ", ''.join(noisy_message))

main()