import os
print("AES Encryption Utility")
print("What you want to do?\n 1. Encrypt File\n 2. Decrypt File\n 3. Shred & Delete File\n")
que = int(input("Enter Option No: "))

if que == 1:
    inpt = input("Enter File name to Encrypt: ")
    os.system("openssl enc -aes-256-cbc -a -A -md sha512 -pbkdf2 -iter 250000 -salt -in "+inpt+" -out "+inpt+".e")
    print("Created Encrypted file "+inpt+".e")

elif que == 2:
    inpt = input("Enter File name to Decrypt: ")
    os.system("openssl enc -aes-256-cbc -a -A -md sha512 -pbkdf2 -iter 250000 -salt -d -in "+inpt+" -out "+inpt+".d")
    print("Created Decrypted file "+inpt+".d")

elif que == 3:
    inpt = input("Enter File name to Shred & Delete: ")
    os.system("shred -v -n 5 "+inpt)
    os.system("rm -rf "+inpt)
    print("Erased file "+inpt)

else:
    print("Invalid Option")


