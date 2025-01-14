#!/usr/bin/env python3

import os
import sys

def ffuser():
    os.system(f'ps ax | grep -P Conches > grep.txt') 
    f = open("grep.txt","r")
    greptxt = f.read()
    if f"firefox -P Conches" not in greptxt:
        os.system(f'/usr/bin/firefox -P Conches "https://gmail.com" &')
    open('grep.txt', 'w').close()

ffuser()