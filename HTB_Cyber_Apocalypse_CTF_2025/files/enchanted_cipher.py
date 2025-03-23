
def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        if 'A' <= char <= 'Z':
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        elif 'a' <= char <= 'z':
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def get_valid_group_str(full_str, start_retrieve_index):
    count = 0
    group_str = ''
    for i in range(start_retrieve_index, len(full_str)):
        group_str += full_str[i]
        if str.isalpha(full_str[i]):
            count += 1
            if count == 5:
                break
    
    return group_str

def main():
    ciphertext = input()
    num_of_group = int(input())
    shift_list = eval(input())
    
    plaintext = ''
    str_start_index = 0
    for i in range(len(shift_list)):
        group_str = get_valid_group_str(ciphertext, str_start_index)
        str_start_index += len(group_str)
        plaintext += caesar_decrypt(group_str, shift_list[i])
    
    print(plaintext)

main()