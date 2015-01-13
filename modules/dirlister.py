#!/usr/bin/env python 

import os 

def run(**args):

    print "[*] dirlister module"
    files = os.listdir(".")

    return str(files)
