
# SaltPepperKetchup 🧂🌶️🍅 

Python3, apt and latest Pip necessary

python3-dotenv
```sh
apt install python3-dotenv
```

```sh
git clone this repo
```

```sh
cd saltpepperketchup/
```
create venv
```sh
python3 -m .
```

install requirements
```sh
pip3 install -r re.txt
```

install rncryptor
```sh
pip3 install rncryptor
```






#goals and motivation:
store keys and delete keys values in .env
reuse with password with encrypted protection
external kill switch to eject ketchup 

Best security practices remain to use strong passwords and close ports and use firewalls

SaltPepperKetchup main goal was for env key values to not be exposed if server is compromised.
IT IS NOT A 100% SECURITY AS ATTACKS CAN OCCUR WHILE YOU ARE USING THE SERVER.

future goal:
add more obfuscation to make kecthup harder to find
frontend and password manager
scan ports and firewal issues in real-time




#encrypt:

create .env or use .f/.env and 


change absolute paths in run.sh and derun.sh
change absolute paths in spkm.py and decrypt.sh
copy-paste run.sh and derun.sh anywhere

run
```sh
 source run.sh
```

delete KEY value from .env
AND
Remove pepper password after usage



#decrypt 

Add back only pepper password in .env


run where you pasted
```sh
 source derun.sh
```
OR
```sh
cd  saltpepperketchup/ 
```
```sh
source bin/activate 
```
```sh
python3 decrypt.py
```
OR use decrypt function as a module from decryptfunction.py

to use decrypt import module:
from decryptfunction import g

return decrypted_data





how to hide decrypt.py or derun.sh, and ketchup. #near useless

sudo chmod -r library/



optional:
keep whole password stored local, not advised



#Keys final status:
Key; deleted, encrypted,

#Decrypt key:
Password; outside or instant inside.
Salt; stored
Pepper; hidden, erased, instant inside.
(Optional) Ketchup; hidden, outside, password-protected, erasable from outside.

Sensitive data;
encrypted.txt is accessible only if Salt,  Pepper, and Ketchup are all leaked




Additional info:
Use a space before a command to delete from history
recommended to store pepper out of server




Usage:

Export encrycted deleted key in new .env

Remove password from pepper when closing program,
Even if server compromised, or shared, only encrypted data remains, be careful there can still be a keylogger so your password could have been leaked.

(optional) remove passw value from mysql external server,
If server becomes unreachable, you can do this to maybe save your locally encrypted stored key.


The chicken vs the egg, becomes; a race for a hidden module vs your speed of reaction.

If pepper is no where to be found, your key is still encrypted, so use a safe password for more strenght.

If pepper is leaked but ketchup is impossible to find, your key is still encrypted.


#Use Key value in other .emv without storing:

You could set the env variables like this:

 export PRIVATE_KEY=0X32323

and then read it with os module.

import os

private_key=os.getenv("PRIVATE_KEY")
But this way, environment variable works only for the duration that shell is live. If you close the shell and restart it, you have to set environmental variable again. python-dotenv prevents us from doing this repetitive work.For this create .env file and add variables in this format

 PRIVATE_KEY=fb6b05d6e75a93e30e22334443379292ccd29f5d815ad93a86ee23e749227
then in the file u want to access anv variables

import os
from dotenv import load_dotenv 

#default directory for .env file is the current directory
#if you set .env in different directory, put the directory address load_dotenv("directory_of_.env)
load_dotenv()
load_dotenv() will set the environment variables from .env and we access with os module

   private_key=os.getenv("PRIVATE_KEY")



# import os
# import subprocess
# import sys

# os.environ['LD_LIBRARY_PATH'] = "my_path" # visible in this process + all children
# subprocess.check_call(['sqsub', '-np', sys.argv[1], '/path/to/executable'],
#                       env=dict(os.environ, SQSUB_VAR="visible in this subprocess"))

#use as a venv in other projects




#bash commands
#source "/root/saltpepperketchup/bin/activate" && python3 /root/saltpepperketchup/decrypt.py 





#optional:
Host ketchup key on other server
Create ketchup kill switch
Enter and erase ketchup access password


remove +ketchup at line 18in spkm.py and decrypt.py to not use ketchup

```sh
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```
```sh
pip3 install mysqlclient
```


CREATE TABLE table (
	passw nvarchar(50),
	strenght int
);

INSERT INTO table (passw, strenght)

VALUES

('fnefeeoio22eb2oi',800);



SELECT passw FROM table;




-then choose a letter in library/ketchups and put your infos
-and replace letter in spkm.py and decrypt.py  ketchup = d()


sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('your SSH hostname'),
    ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
    remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='your PythonAnywhere database username',
        passwd='your PythonAnywhere database password',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='your database name, eg yourusername$mydatabase',
    )
    # Do stuff
    connection.close()

https://help.pythonanywhere.com/pages/AccessingMySQLFromOutsidePythonAnywhere/




other future upgrades;

deadmansswitch?
https://github.com/d3fc0n6/Dead-Mans-Switch


discussions;
https://news.ycombinator.com/item?id=4381905



cookbook for python-dotenv manipulator


python-dotenv [OPTIONS] COMMAND [ARGS]...



       -f, --file PATH
              Location of the .env file, defaults to .env file in current working directory.

       -q, --quote [always|never|auto]
              Whether to quote or not the variable values.  Default mode is always. This does not
              affect parsing.

       -e, --export BOOLEAN
              Whether to write the dot file as an executable bash script.

       --version
              Show the version and exit.

       --help Show this message and exit.

   Commands:
       get    Retrieve the value for the given key.

       list   Display all the stored key/value.

       run    Run command with environment variables present.

       set    Store the given key/value.

       unset  Removes the given key.

bash commands;

#nano source ~/.bashrc

historyDeln() {
  n=$(history 1 | awk '{print $1}')    # current history number
  historyDel $(( $n-$1 )) $(( $n-1 ))  # Call historyDel with ranges
}

# source ~/.bashrc



discussions:

best is safe password andrestrict ports
[12:01 AM]
You need some ports open
[12:01 AM]
Well could be a more strict Ip list
[12:01 AM]
it: Instead of moving the key, you could simply set the file to immutable, like this:

sudo chattr +i /home/user/.ssh/authorized_keys
Once you've set up the source IP limitation, and you've secured the key file against tampering, it won't matter if the private key gets leaked - it still won't be usable from any other system.

There are a lot of other things you can do to limit the users when they connect with keys - see the man page for sshd. There's also been some questions about this at Serverfault, for example Limited SSH access for log retrieval.
[12:01 AM]
I see your point like even this approach the keys are still local
[12:02 AM]
What about Smart Cards?
[12:02 AM]
I would suggest Smart Cards and secure tokens*. These have a storage that cannot be read, only be used from the secure cryptoprocessor. This means nobody that have full access to token can read the private key. The only thing user can do is to send a string to either be signed or decrypted, and get the result back.

The Smart card/secure token can also generate the keypair on the card, ensuring the key never has been, and can been outside of card/token. The public key can then be extracted to then be inserted into authorized keys.

*Secure USB tokens are effectively a Smart card and a Smart card reader, combined in the same chip with the same security level.

I would suggest a smart card and smart card reader, if multiple authorized users are gonna use the same terminal to connect to the SSH server under their own identity.


That's really ultimate security stuff [12:06 AM] https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslcryptodevice [12:06 AM] SSLCryptoDevice [12:07 AM] Seems out of scope tough [12:09 AM] teps that finally worked for me: 1.Install OpenSSL from sources, specifying -DOPENSSL_LOAD_CONF when running ./config 1.1.Create/build your OpenSSL engine and add it to your openssl.cnf file 2.Install httpd from sources, using these commands: CFLAGS='-DSSL_EXPERIMENTAL_ENGINE -DSSL_ENGINE -DOPENSSL_LOAD_CONF' ./configure --enable-ssl --with-ssl=/usr/local/ssl --with-pcre=/usr/local/pcre --enable-so make make install 2.1.Edit httpd-ssl.conf by adding SSLCryptoDevice engine_id and make sure that when execute $ openssl engine, the engine_id specifier appears on the list. Also, you have to create self-signed cerificate and private key, modify the httpd.conf file, but this is not the subject of this question. Search: how to configure HTTPS on Apache. 3.$ httpd -k restart and that is all [12:10 AM] Still not secure if server compromised as it is self signed [12:11 AM] Generally, the best practice is to generate the private key along with the CSR on the server where you intend to install the SSL certificate. This way, you eliminate the risk of vulnerability during the transfer from one machine to another. However, sometimes you may need to create the private key via an external CSR generator tool. For this reason, there are special files called key stores that can safely store your public and private key pair. Keystores (PFX and KS files) PKCS#12 (.pfx or .p12) and .jks* (created by the Java keytool) are special files containing your public/private keypair. You can store these files anywhere, including remote servers. Their main security appeal is a password that protects the contents. Anytime you want to use your private key, you have to enter a strong password.  Be sure to create a sophisticated, random password if you use this method. Another benefit of such files is that you can easily distribute copies if multiple people need to use the certificate. Just make sure you completely trust them and their intentions when sharing the private key password. [12:12 AM] Oh this part interesting [12:12 AM] So the Keystores need a password everytime they are used 🌐KitKatMarty🌐 — Today at 12:15 AM The Reality Of Peppers In the security and cryptography realms, "make sense" isn't enough. Something has to be provable and make sense in order for it to be considered secure. Additionally, it has to be implementable in a maintainable way. The most secure system that can't be maintained is considered insecure (because if any part of that security breaks down, the entire system falls apart). And peppers fit neither the provable or the maintainable models... [12:16 AM] The current password hashing algorithms (bcrypt, pbkdf2, etc) all are designed to only take in one secret value (the password). Adding in another secret into the algorithm hasn't been studied at all. [12:16 AM] Woaah [12:16 AM] Went deep [12:17 AM] It Requires You To Roll Your Own Crypto Since no current algorithm supports the concept of a pepper, it requires you to either compose algorithms or invent new ones to support a pepper. And if you can't immediately see why that's a really bad thing: Anyone, from the most clueless amateur to the best cryptographer, can create an algorithm that he himself can't break




inspiration;


Fist we should talk about the exact advantage of a pepper:

The pepper can protect weak passwords from a dictionary attack, in the special case, where the attacker has read-access to the database (containing the hashes) but does not have access to the source code with the pepper.
A typical scenario would be SQL-injection, thrown away backups, discarded servers... These situations are not as uncommon as it sounds, and often not under your control (server-hosting). If you use...

A unique salt per password
A slow hashing algorithm like BCrypt
...strong passwords are well protected. It's nearly impossible to brute force a strong password under those conditions, even when the salt is known. The problem are the weak passwords, that are part of a brute-force dictionary or are derivations of them. A dictionary attack will reveal those very fast, because you test only the most common passwords.

The second question is how to apply the pepper ?

An often recommended way to apply a pepper, is to combine the password and the pepper before passing it to the hash function:

$pepperedPassword = hash_hmac('sha512', $password, $pepper);
$passwordHash = bcrypt($pepperedPassword);
There is another even better way though:

$passwordHash = bcrypt($password);
$encryptedHash = encrypt($passwordHash, $serverSideKey);
This not only allows to add a server side secret, it also allows to exchange the $serverSideKey, should this be necessary. This method involves a bit more work, but if the code once exists (library) there is no reason not to use it.


wow you made this far, help contribute on this project or leave me a start:)

tutorial;
https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/amp/