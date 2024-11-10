import sys
import os
import time

def rotate_word(word, inc):
    if inc > 90: #bad usecase warning - could fix but why?
        print("Increment too high, be sensible!")
        return 0

    new_word = [0] * len(word)
    for i in range (0, len(word)):
        j = ord(word[i]) + inc
        k = ord(word[i])

        #lowercase
        if j > 122 and k >= 97:
            j = 97 + (j - 122)

        #capitals
        elif j > 90 and k <= 90:
            j = 65 + (j-90)

        #int support ;)
        elif j > 57 and k < 57:
            j = 48 + (j-57)

        if chr(j).isalpha():
            new_word[i] = chr(j)
        elif str(chr(j)).isdigit():
            new_word[i] = chr(j)
        else:
            new_word[i] = str(word[i])

        if len(sys.argv) > 1:
            if sys.argv[1] == "-v":
                print(word[i], ",", k, "->", chr(j), ",", j)

    return ''.join(new_word)

#pretty sure it works...
def decipher_word(word, key):

    old_word = [0] * len(word)
    for i in range (0, len(word)):
        j = ord(word[i]) - key
        k = ord(word[i])

        #lowercase
        if j < 97 and k >= 97:
            j = 122 - (97-j)

        #capitals
        elif j < 65 and k <= 90:
            j = 90 - (65-j)

        #int support ;)
        elif j < 48 and k <= 57:
            j = 57 - (57-j)

        if chr(j).isalpha():
            old_word[i] = chr(j)
        elif str(chr(j)).isdigit():
            old_word[i] = chr(j)
        else:
            old_word[i] = str(word[i])

        if len(sys.argv) > 1:
            if sys.argv[1] == "-v":
                print(word[i], ",", k, "->", chr(j), ",", j)

    return ''.join(old_word)

def rotate_sentence(st, inc):
    words = st.split(' ')
    new_st = [0] * len(words)
    for i in range (0, len(words)):
        if words[i].isalpha():
            new_st[i] = rotate_word(words[i], inc)
        elif words[i].isdigit():
            new_st[i] = rotate_word(words[i], inc) #for some odd reason commas slip by
        else:
            new_st[i] = str(words[i])
    
    return ' '.join(new_st)

def decipher(st, key):
    words = st.split(' ')
    new_st = [0] * len(words)
    for i in range (0, len(words)):
        if words[i].isalpha():
            new_st[i] = decipher_word(words[i], key)
        elif words[i].isdigit():
            new_st[i] = decipher_word(words[i], key)
        else:
            new_st[i] = str(words[i])
    
    return ' '.join(new_st)

running = True
while running:
    os.system("clear") #change to clear for osX/linux!

    print("""
        Please select operation:
        
        1) Encrypt message
        2) Decrypt message
        3) Load ciphertext
        4) Leave :(
          
    """)

    selection = int(input("Action: "))
    if selection == 1:
        prompt = input("Enter plaintext: ")
        key = int(input("Enter int key: "))
        if key == 0:
            print("Non-valid key -> exiting...")
            running = False

        encrypted_prompt = rotate_sentence(prompt, key)
        print("Ciphertext: \n", encrypted_prompt, "\n")
        print("Do you wish to store it? \n")
        option = input("Enter option (yes/[no]): ") #have not implemented any no because it is standard and will escape immediately
        if option == "yes" or option == "y":
            filename = input("Enter filename: ")
            with open(filename, 'w') as file:
                for i in encrypted_prompt.splitlines():
                    file.write(i)
                    file.write("\n")
                print("Saved!")
                time.sleep(1)
                file.close()

    elif selection == 2:
        prompt = input("Enter ciphertext: ")
        key = int(input("Please enter key: "))
        print(decipher(prompt, key))
        input("")

    elif selection == 3:
        #load text file
        filename = input("Enter filename to load: ")
        with open(filename, 'r') as ciphertext:
            print("Ciphertext loaded! \n")
            print(ciphertext)
            action = input("Would you like to decrypt? (yes/[no])")
            if action == "yes" or action == "y":
                key = int(input("Please enter key: "))
                for i in ciphertext:
                    print(decipher(ciphertext.read(), key), "\n")

                save = input("Save to file? (yes/[no])")
                if save == "yes" or "y":
                    savefile_name = input("Enter filename: ")
                    with open(savefile_name, 'w') as savefile: 
                        for i in ciphertext:
                            savefile.write(decipher(ciphertext.read()))
                            savefile.write("\n")
                        savefile.close()

        ciphertext.close()

    elif selection == 4:
        print("Exiting...")
        running = False
    else:
        print("Non-valid selection.")
