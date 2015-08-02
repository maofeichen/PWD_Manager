#!/usr/bin/env python
"""pwd_manager.py: password manager
The utlimate goal of this project/file is avoid using/remembering different
passwords for different accouts/websites. User only needs to remember one 
master password or even none, this file/project will be able to generate
different strong passwords for various purposes automatically."""

__author__    = "mchen"

import getpass

import hashlib
import hmac

def get_master_pwd():
    "Get master password from user, input from cmd."
    mas_pwd = getpass.getpass(prompt='Please input master password:\n')
    print(mas_pwd)
    return mas_pwd

def get_identity():
    "Get the identity, the identitiy of the password."
    identity = input("Please input the identity name:\n");
    return identity

def gen_password():
    "Generate passwords based on the master password and identity."
    b_mas_pwd = get_master_pwd().encode('utf-8')
    b_identity = get_identity().encode('utf-8')
    print("master password in binary: %s\n\
            indentity in binary: %s"\
            %(b_mas_pwd, b_identity) )
  
    mas_pwd_sha256 = hashlib.sha256(b_mas_pwd).digest()
    print("master password in sha256 hash:\n%s\n\
            lenth: %d"\
            %(mas_pwd_sha256, len(mas_pwd_sha256) ) )

    pwd = hmac.new(mas_pwd_sha256, \
                    msg=b_identity, \
                    digestmod=hashlib.sha256).hexdigest()
    print("Password: %s"%(pwd) )

def main():
    gen_password()

if __name__ == "__main__":
    main()

