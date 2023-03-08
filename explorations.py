import argon2
import base64
import bcrypt
from  ketchup import ketchup
from pepper import pepper
import hashlib
 

# adding 5gz as password

#salt = "5gz"
 
# Adding salt at the last of the password


# Encoding the password


# Printing the Hash

#print(hashed.hexdigest())

# Declaring our password

password = b'GeekPasswor383729739239d'
 
# Adding the salt to password

salt = bcrypt.gensalt()
# Hashing the password

hashed = bcrypt.hashpw(password, salt)
 
# printing the salt

print(salt)
 
# printing the hashed

print(hashed)
 

# pepperedPassword = hash_hmac('sha512', password, pepper);
# passwordHash = bcrypt(pepperedPassword);


password2 = hashed+pepper
#hashed = hashlib.md5(dataBase_password.encode())

#argon2 is stronger then md5

#passs = hashed+pepper+salt
#passwordHash = argon2.hash_password(passs)

#passwordHash = (hash('sha256', password2))


encoded = base64.b64encode(password2)
 
newb = bcrypt(encoded)


newp =newb

#for reference only
#realpasswordHash = bcrypt(password)
#encryptedHash = encrypt(passwordHash, serverSideKey)


# Declare the password as a bytes object

#realpassword = bcrypt.hashpw(newp, ketchup)
 
 
# Print the hashed password

#print(realpassword)




#data = base64.b64decode(encoded)




 








 



 
import rsa
 
# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)
 
# this is the string that we will be encrypting
message = "hello geeks"
 
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
                         publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("decrypted string: ", decMessage)