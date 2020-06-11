#!/usr/bin/python3

import re


# for validating an Ip-address 
regex_all_IP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

regex_all_IP_Private = '''^(^0\.)|(^10\.)|(^100\.6[4-9]\.)|(^100\.[7-9]\d\.)|(^100\.1[0-1]\d\.)|(^100\.12[0-7]\.)|(^127\.)|(^169\.254\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.0\.0\.)|(^192\.0\.2\.)|(^192\.88\.99\.)|(^192\.168\.)|(^198\.1[8-9]\.)|(^198\.51\.100\.)|(^203.0\.113\.)|(^22[4-9]\.)|(^23[0-9]\.)|(^24[0-9]\.)|(^25[0-5]\.)'''


regex_Private_IP_127 = '''^(127?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


regex_IP_Private_A = '''^(10?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


regex_IP_Private_B = '''^(172?)\.(1[6-9]|2[0-9]|3[0-1]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


regex_IP_Private_C = '''^(192?)\.(168?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''



def check_IP(value):
    if (re.search(regex_all_IP, value)):
        return ("Valid IP address  " + value)
    else:
        return ("Invalid IP address  " + value)    

def check_IP_Private(value):
    if (re.search(regex_all_IP_Private, value)):
        return ("Valid Private IP address  " + value)
    else:
        return ("Invalid Private IP address  " + value)  
        
def check_IP_Private_A(value):
    if (re.search(regex_IP_Private_A, value)):
        return ("Valid Private IP address class A  " + value)
    else:
        return ("Invalid Private IP address class A  " + value) 
 
def check_IP_Private_B(value):
    if (re.search(regex_IP_Private_B, value)):
        return ("Valid Private IP address class B  " + value)
    else:
        return ("Invalid Private IP address class B  " + value) 
        
def check_IP_Private_C(value):
    if (re.search(regex_IP_Private_C, value)):
        return ("Valid Private IP address class C  " + value)
    else:
        return ("Invalid Private IP address class C  " + value) 

def checkB_IP(value):
    if (re.search(regex_all_IP, value)):
        return True
    else:
        return False   

def checkB_IP_Private(value):
    if (re.search(regex_all_IP_Private, value)):
        return True
    else:
        return False 
        
def checkB_IP_Private_A(value):
    if (re.search(regex_IP_Private_A, value)):
        return True
    else:
        return False 
 
def checkB_IP_Private_B(value):
    if (re.search(regex_IP_Private_B, value)):
        return True
    else:
        return False 
        
def checkB_IP_Private_C(value):
    if (re.search(regex_IP_Private_C, value)):
        return True
    else:
        return False
