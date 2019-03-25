# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:01:50 2019
@author: h5435
"""

numbers = []
for i in range(10) :
    numbers.append(i)
print(numbers)

del numbers[0]
print(numbers)

del numbers[:5]
print(numbers)

print(numbers[1:3])

# 값을 한번에 바꿀 수 있음
numbers[1:3] = [77, 88]
print(numbers[1:3])
print(numbers)

# 값을 더 추가해서 바꿀 수 있음
numbers[1:3] = [77, 88, 99]
print(numbers)

# 값을 축소해서 바꿀 수 있음
numbers[1:4] = [8]
print(numbers)