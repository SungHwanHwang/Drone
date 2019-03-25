# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:38:55 2019

@author: h5435
"""
list1 = []

i = 0

for i in range(20) :
    list1.append(i)

print(list1[5:15])

# step을 통해 특정 숫자만큼 건너 뛴 값들 만 받아 올 수 있다.
print(list1[5:15:2])
print(list1[5:15:3])

# 음수의 step을 사용할 때는 거꾸로 써줘야 한다.
# 뒤로 부터 받을 때는 값을 모두 써줄 때에도 -1 step을 적어주어야한다.
print(list1[15:5:-1])
print(list1[14:5:-1])

print(list1[::3])