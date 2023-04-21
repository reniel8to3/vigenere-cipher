#create dictionary
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define main function
def main():
#ask user for input
print ('Hello!  This program is designed to create a Vegenere Cipher.')
    plaintext = input("What do you want to decipher? Please use uppercase letters with no spaces only. ")
    keyword = input("What is the key to the code? Please use uppercase letters only. ")
    secret_code = encrypt(plaintext, keyword)
    secret_revealed = decrypt(secret_code, keyword)

    print('Deciphering...')
    print("The resulting Vigenere Cipher is: " + secret_code)
    print("Your code is : " + secret_revealed)
#create defining functions
plaintext_to_index = dict(zip(letters, range(len(letters))))
index_to_plaintext = dict(zip(range(len(letters)), letters))
#create encrypt function
    def encrypt(plaintext, keyword):
    encrypted = ""
    split_message = [plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (plaintext_to_index[letter] + plaintext_to_index[keyword[i]]) % len(letters)
            encrypted += index_to_plaintext[number]
            i += 1

    return encrypted
#create decrypt function
    def decrypt(plaintext, keyword):
    decrypted = ""
    split_encrypted = [plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (plaintext_to_index[letter] - plaintext_to_index[keyword[i]]) % len(letters)
            decrypted += index_to_plaintext[number]
            i += 1

    return decrypted

main()