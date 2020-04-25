# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:31:58 2020

@author: abhin
"""

def login(username, password):
    p=getPassword(username)
    if p==password:
        return True
    else:
        return False
    