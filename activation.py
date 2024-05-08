import os
import hashlib

def check_activation():
    file_there  = True
    if os.path.exists("./activation/key.act"):
        with open("./activation/key.act", "r") as keyfile:
            key = keyfile.read()
    else:
        file_there = False
    if os.path.exists("./activation/type.act"):
        with open("./activation/type.act", "rb") as typefile:
            type = typefile.read()
    else:
        file_there = False
    if os.path.exists("./activation/mail.act"):
        with open("./activation/mail.act", "rb") as mailfile:
            mail = mailfile.read()
    else:
        file_there = False
    if os.path.exists("./activation/name.act"):
        with open("./activation/name.act", "rb") as namefile:
            name = namefile.read()
    else:
        file_there = False
    if file_there:
        decrypt = hashlib.md5()
        decrypt.update(name)
        decrypt.update(mail)
        decrypt.update(type)
        decrypt.update("JAMADE".encode())
        if decrypt.hexdigest() == key:
            return type.decode()
    return "FAIL"
        
def write_activation(key, type, name, mail):
    if not os.path.exists("./activation"):
        os.mkdir("./activation")
    with open("./activation/key.act", "w") as keyfile:
        keyfile.write(key)
    with open("./activation/type.act", "w") as typefile:
        typefile.write(type)
    with open("./activation/mail.act", "w") as mailfile:
        mailfile.write(mail)
    with open("./activation/name.act", "w") as namefile:
        namefile.write(name)