import os

from cffi import FFI
ffi = FFI()

from cryptography.fernet import Fernet

from consolemenu import *
from consolemenu.items import *


key = b""


def setkey():
    global key
    key = binput("Enter key:")
    try:
        f = Fernet(key)
    except Exception as e:
        print(str(e))
        os.system('pause')


def genkey():
    global key
    print("GENERATE KEY")
    key = Fernet.generate_key()
    print("KEY:"+str(key, "utf-8"))
    os.system('pause')


def showkey():
    global key
    print("SHOW KEY")
    print("KEY:"+str(key, "utf-8"))
    os.system('pause')


def binput(a):
    return bytes(input(a).strip(), "utf-8")


def encrypt():
    global key
    print("ENCRYPT")
    if not key:
        print("NO KEY SET")
        os.system('pause')
        return

    f = Fernet(key)
    print(str(f.encrypt(binput("String:")), "utf-8"))
    os.system('pause')


def decrypt():
    global key
    print("DECRYPT")
    if not key:
        print("NO KEY SET")
        os.system('pause')
        return

    f = Fernet(key)
    
    try:
        print(str(f.decrypt(binput("String:")), "utf-8"))
    except Exception as e:
        print(str(e))

    os.system('pause')


menu = ConsoleMenu("FERNET ENCRYPT/DECRYPT")
menu.append_item(FunctionItem("Set Key", setkey))
menu.append_item(FunctionItem("Generate Random Key", genkey))
menu.append_item(FunctionItem("Show Key", showkey))
menu.append_item(FunctionItem("Encrypt", encrypt))
menu.append_item(FunctionItem("Decrypt", decrypt))


if __name__ == "__main__":
    menu.show()
