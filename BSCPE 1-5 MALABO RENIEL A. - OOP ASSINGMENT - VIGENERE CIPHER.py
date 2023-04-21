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
#create decrypt function