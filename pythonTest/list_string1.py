# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:29:27 2019

@author: h5435
"""

my_list = [1, 2, 3, 4, 5, 6]
my_list[0]

print(my_list[0])

# string일 때
str = 'Hello World'
print(str[0])
print('H' in str)
print(str.index('W'))

#string을 리스트로 만들기
characters = list('abcdef')
print(characters)

words = 'Hello World는 프로그래밍을 배우기에 아주 좋은 사이트 입니다.'
#words_list = list(words)
words_list = words.split()
print(words_list)

time_str = '10:35:27'
time_list = time_str.split(':')
print(time_list)

# 기준으로 붙이고 싶은 문자.join(time_list)
time_str = '.'.join(time_list)
print(time_str)