import json
from cryptography.fernet import Fernet

jsonfile = 'mypass.json'
with open(jsonfile) as jf:
    my_dict = json.load (jf)
    print(my_dict['username'])
    print(my_dict['password'])
mypass = my_dict['password']
# password encryption
message = mypass.encode("utf-8")
#print(message)
key = Fernet.generate_key()
f = Fernet(key)
#print(key)
#print(f)
encrypted = f.encrypt(message)
#print(encrypted)
# password decryption
encode = "utf-8"
decrypted = f.decrypt(encrypted)
#print(decrypted)
new_pass = decrypted.decode("utf-8")
#print(new_pass)
