# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:31:04 2019
@author: h5435
"""
areas = []
for i in range(1, 11) :
    if i % 2 == 0 :
        areas.append(i*i)
print('areas : ', areas)

# list Comprehension
# for문을 돌며 나오는 i값, 그 i값의 연산을 for문 앞에 적어주어 원하는 list를 만든다.
areas2 = [i*i for i in range(1,11) if i%2 == 0]
print('areas2 : ', areas2)

# for문 중첩 기능
areas3 = [(x,y) for x in range(15) for y in range(15)]

print(areas3)