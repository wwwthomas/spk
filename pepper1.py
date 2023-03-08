import bcrypt
import os

p = str(os.getenv('PEPPER'))

password=p.encode('utf8')


with open("/root/saltpepperketchup/outputs/salty.txt", "rb") as binary_file:
     salty = binary_file.read()

pepper = bcrypt.hashpw(password, salty)