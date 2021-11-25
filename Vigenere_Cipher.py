#Gelber Castillo Lab 2 - Vigenere Cipher
import random
import math

keywords        = ['SECURITY', 'VIGENERE', 'DEFENSE', 'PROTECT', 'SHIELD']
alphabet_keys   = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#Where we will store encrypted text
ciphertext      = []
ciphertext_num  = []
ciphertext_arr  = []
#Where we will store the decrypted text
decreptedtext   = []
decrypted_num   = []
decrypted_arr   = []
#Dicts
alpha_num       = {}
num_alpha       = {}

#This function encrypts the plaintext using the key.
#First, if the given phrase is bigger than the key, we reformat the key to match the size of the phrase.
#Then, we use the formula ((Letter index + Key index) mod 26) to get the values for the encrypted phrase.
#We then we use the num_alpha hashtable to get a corresponding letter.

def encrypt(plaintext, key):
    #This if statement is only applicable when plaintext is larger than key. Otherwise, we move on.
    if (len(plaintext) > len(key)):
        key         *= math.floor(len(plaintext) / len(key))
        difference  = len(plaintext) - len(key)
        dif_key     = key[:difference]
        key         = ''.join([key, dif_key])

    for i in range(len(plaintext)):
        #Every ((Letter index + Key index) mod 26) element is stored in ciphertext_num
        #ciphertext_num.append((alpha_num[plaintext[i]] + alpha_num[key[i]]) % 26)
        #Uses num_alpha hashtable.
        if (plaintext[i].isspace()):
            ciphertext_num.append(" ")
            ciphertext_arr.append(" ")
            #Finalized key with the proper spaces (if included)
            key = key[:i] + " " + key[i:]
        else:
            #Every ((letter index + Key index) mod 26) element is stored in ciphertext_num
            ciphertext_num.append((alpha_num[plaintext[i]] + alpha_num[key[i]]) % 26)
            ciphertext_arr.append(num_alpha[ciphertext_num[i]])
    ciphertext = "".join(ciphertext_arr)
    return ciphertext, key

#Decrypting the ciphertext using the formula (letter index - key index)
#If the outcome is negative, we add 26 (number of letters in the alphabet)

def decrypt(ciphertext, key):
    for i in range(len(ciphertext)):
        if(ciphertext[i].isspace()):
            decrypted_num.append(" ")
            decrypted_arr.append(" ")
        else:
            decrypted_num.append(alpha_num[ciphertext[i]] - alpha_num[key[i]])
            if (decrypted_num[i] < 0):
                decrypted_num[i] += 26
            decrypted_arr.append(num_alpha[decrypted_num[i]])
    decryptedtext = "".join(decrypted_arr)
    return decryptedtext
                        
def main():
    #Creating 2 hashtables.
    #The first matches a letter of the alphabet to its numerical position starting from 0.
    #ex. 'A' = 0, 'B' = 1, ... , 'Z' = 25
    #The second matches a number to its correlating alphabetical letter.
    #ex. 0 = 'A', 1 = 'B', ... , 25 = 'Z'
    for a_key, a_value in zip(alphabet_keys, alphabet_values):
        alpha_num[a_key] = a_value
        num_alpha[a_value] = a_key       
    #Initializing a random key
    chosen_key = keywords[random.randint(0,4)]
    while(True):
        plaintext = input("Plaintext: \t")
        #The condition below validates the input. We reject any input that does not
        #contain letters and continue asking for a valid plaintext input until we get one.
        #Then we convert the string to uppercase.
        if False in [(letter.isalpha() or letter.isspace()) for letter in plaintext]:
            print("Only letters are allowed.")
        else:   
            plaintext = plaintext.upper()
            break
    #This block encrpts, then decrypts
    ciphertext, key_reformatted = encrypt(plaintext, chosen_key)
    decryptedtext               = decrypt(ciphertext, key_reformatted)
    #Printing results
    print("Keyword: \t" + chosen_key)
    print("Ciphertext: \t" + ciphertext)
    print("Decrypted: \t" + decryptedtext)
main()
