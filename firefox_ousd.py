#!/usr/bin/env python3

import os
import sys

def ffuser():
    os.system(f'ps ax | grep -P OUSD > grep.txt') 
    f = open("grep.txt","r")
    greptxt = f.read()
    if f"firefox -P OUSD" not in greptxt:
        os.system(f'/usr/bin/firefox -P OUSD "https://gmail.com" &')
    open('grep.txt', 'w').close()

ffuser()