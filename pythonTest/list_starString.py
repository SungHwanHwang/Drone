# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:10:03 2019

@author: h5435
"""
list = [1, 2, 3, 4, 5]
text = 'hello world'
print(list[1])
print(text[1])

# list[시작:끝] ==> 시작부터 끝 전까지를 뽑아 줌
text[1:5]
print(text[1:5])

list = ['영', '일', '이', '삼', '사', '오']
print(list[1:3])

print(list[2:len(list)])
print(list[2:])

print(list[0:2])
print(list[:2])

print(list[:]) # 리스트를 복사하는 것 새로운 리스트를 만드는 것
print(list)