import bcrypt
import os

p = str(os.getenv('PEPPER'))

password=p.encode('utf8')


salty = bcrypt.gensalt()

with open("/root/saltpepperketchup/outputs/salty.txt", "wb") as binary_file:
   
#     # Write bytes to file
     binary_file.write(salty)

pepper = bcrypt.hashpw(password, salty)