# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:53:02 2019

@author: USER
"""
def return_false() :
    print('함수return_false')
    return False

def return_true() :
    print('함수return_true')
    return True

a = 10
if a<0 and 2**a > 1000 and a%5 == 2 and round(a) == a :
    print('복잡한 식')

print('테스트1')
a = return_false()
b = return_true()

if a and b :
    print(True)
else :
    print(False)

print('테스트2')
if return_false() and return_true() :
    print('true')
else :
    print('false')
    

dic = {'Key2':'Value1'}

# 파이썬은 단락 평가를 함
if 'Key1' in dic and dic['Key1'] == 'Value1' :
    print('Key1도 있고 그 값은 Value1이다')
else :
    print('아니네')