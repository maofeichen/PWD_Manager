#!/usr/bin/env python
"""pwd_manager.py: password manager
The utlimate goal of this project/file is avoid using/remembering different
passwords for different accouts/websites. User only needs to remember one 
master password or even none, this file/project will be able to generate
different strong passwords for various purposes automatically."""

__author__    = "mchen"

import getpass

def get_master_pwd():
    "Get master password from user, input from cmd."
    mas_pwd = getpass.getpass(prompt='Please input master password:\n')
    print(mas_pwd)

def main():
    get_master_pwd()

if __name__ == "__main__":
    main()

