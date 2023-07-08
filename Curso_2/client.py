#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:45:04 2023

@author: rafaelfabrichimidt
"""

import socket 
import time

HOST = 'localhost'
PORT = 3011

s = socket.socket()

s.connect((HOST, PORT))

while True:
    
    data = s.recv(1024)
    
    print(data.decode('utf-8'))
    
    time.sleep(2 )