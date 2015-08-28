#!/usr/bin/env python
"""pwd_manager.py: password manager
The utlimate goal of this project/file is avoid using/remembering different
passwords for different accouts/websites. User only needs to remember one 
master password or even none, this file/project will be able to generate
different strong passwords for various purposes automatically, based on the
master pwd and identity(what accout/website the pwd is used for?)."""

__author__    = "mchen"

import getpass

import hashlib
import hmac

import base64

def get_master_pwd():
    "Get master password from user, input from cmd."
    mas_pwd = getpass.getpass(prompt='Please input master password:\n')
#    print(mas_pwd)
    return mas_pwd

def get_identity():
    "Get the identity, what accout/website the pwd is used for?"
    identity = input("Please input the identity name:\n");
    return identity

def encode_pwd(b_pwd):
    "Encode the byte pwd stream into charset (currently base64)"
    b64_pwd = base64.b64encode(b_pwd)
    return b64_pwd

def gen_password():
    "Generate passwords based on the master password and identity."
    b_mas_pwd = get_master_pwd().encode('utf-8')
    b_identity = get_identity().encode('utf-8')
#    print("master password in binary: %s\nindentity in binary: %s"\
#            %(b_mas_pwd, b_identity) )
  
    mas_pwd_sha256 = hashlib.sha256(b_mas_pwd).digest()
#    print("master password in sha256 hash:\n%s\nlenth: %d"\
#            %(mas_pwd_sha256, len(mas_pwd_sha256) ) )

    pwd = hmac.new(mas_pwd_sha256, msg=b_identity, \
                    digestmod=hashlib.sha256).digest()
#    print("Password: %s, Len: %d"%(pwd, len(pwd) ) )

    b64_pwd = encode_pwd(pwd)
#    print("Password in b64: %s, Len: %d"%(b64_pwd, len(b64_pwd) ) )
    print("Password: %s "%(b64_pwd) )
def main():
    gen_password()

if __name__ == "__main__":
    main()

