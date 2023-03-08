import rncryptor
from dotenv import load_dotenv
import os 
#from ketchup import ketchup
from pepper import pepper
from salt import salt
from library import a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z

#ketchup=x()

#to change ketchup or uncomment to obfuscate xD

#ketchup=a(),b(),c(),d(),e(),f(),g(),h(),i(),j(),k(),l(),m(),n(),o(),p(),q(),r(),s(),t(),u(),v(),w(),x(),y(),z()


mustard= '3848329'  #useless mustard
data = str(os.getenv('KEY'))
password = (salt+pepper+ketchup)



# rncryptor.RNCryptor's methods
cryptor = rncryptor.RNCryptor()
encrypted_data = cryptor.encrypt(data, password)



with open("/root/saltpepperketchup/outputs/encrypted.txt", "wb") as binary_file:
   
    # Write bytes to file
    binary_file.write(encrypted_data)



#uncomment  to store password locally

# with open("/root/saltpepperketchup/output2.txt", "wb") as binary_file:
   
#     # Write bytes to file
#     binary_file.write(password)



#save salt

with open("/root/saltpepperketchup/outputs/salt.txt", "wb") as binary_file:
   
#     # Write bytes to file
     binary_file.write(salt)



