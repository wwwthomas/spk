import rncryptor
from dotenv import load_dotenv
import os 
#from ketchup1 import ketchup
from pepper1 import pepper
from library import a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z

#ketchup=x()

#to change ketchup or uncomment to obfuscate xD
#ketchup=a(),b(),c(),d(),e(),f(),g(),h(),i(),j(),k(),l(),m(),n(),o(),p(),q(),r(),s(),t(),u(),v(),w(),x(),y(),z()
cryptor = rncryptor.RNCryptor()

with open("/root/saltpepperketchup/outputs/salt.txt", "rb") as binary_file:
     salt = binary_file.read()


password = (salt+pepper+ketchup)

#when ketchup hiding

# ketchup = ketchup.ketchup 
# password = (salt+pepper+ketchup)


with open("/root/saltpepperketchup/outputs/encrypted.txt", "rb") as binary_file:
    encrypted_data = binary_file.read()










decrypted_data = cryptor.decrypt(encrypted_data, password)

#or

#decrypted_data = cryptor.decrypt(encrypted_data, byte)




# print(decrypted_data)

print(decrypted_data)


