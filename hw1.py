# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 20:15:17 2025

@author: USER
"""
def dec_to_bin(num):
    binary=""
    for i in range (7,-1,-1):
        if num > 2**i:  
            binary+="1"
            num-=2**i
    
        else:
            binary+="0"
    return binary

def bin_to_hex(binary):
    hex_chars = "0123456789ABCDEF"
    hexadecimal=""
    
    while len(binary) % 4 != 0:
        binary = "0" + binary
        
    for i in range(0, len(binary), 4):
        four_bits = binary[i:i+4]  
        decimal_value = 0
        
        for j in range(4):
          decimal_value += int(four_bits[j]) * (2 ** (3-j))  
        hexadecimal += hex_chars[decimal_value]
    
    return hexadecimal

while True:
    reply=input('請輸入一個介於1~255的數字:')
    
    try:
        reply1 = int(reply)
        if 1 <= reply1 <= 255:      
           print("%s的二進位是: %s"%(reply,dec_to_bin(reply1)))
           print("%s的十六進位是: %s"%(reply,bin_to_hex(reply)))  
        
        else:
                print("數字不在有效範圍內！請輸入 1 到 255 之間的數字。")
    except ValueError:
     print("請輸入有效的數字！")
       
                
       
       