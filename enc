#!/bin/bash
echo "AES File Encryption utility"
echo "What you want to do?

[1] Encrypt.
[2] Decrypt.
[3] Shred & Delete.
"
read que
if [ "$que" == 1 ]
then
echo "Enter File name that you want to Encrypt: "
read inpt
echo "Encrypting "$inpt" ....."
openssl enc -aes-256-cbc -a -A -md sha512 -pbkdf2 -iter 250000 -salt -in $inpt -out $inpt-"enc"
echo "Created an Encrypted file named "$inpt-"enc"
elif [ "$que" == 2 ]
then
echo "Enter File name that you want to Decrypt: "
read inpt
echo "Decrypting "$inpt" ....."
openssl enc -aes-256-cbc -a -A -md sha512 -pbkdf2 -iter 250000 -salt -d -in $inpt -out $inpt-"dec"
echo "Created an Encrypted file named "$inpt-"dec"
elif [ "$que" == 3 ]
then
echo "Enter File name that you want to Shred: "
read inpt
echo "Shreding file "$inpt
shred -v -n 5 $inpt
rm -rf $inpt
else
 echo "Invalid Option"
fi
