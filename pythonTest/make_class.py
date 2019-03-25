# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:55:23 2019

@author: h5435
"""

class Human() :
    '''사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = '영어'

print(person1.language)
print(person2.language)

person1.name = '서울시민'
person2.name = '인도시민'

print(person1.name)
print(person2.name)

def speak(person) :
    print('{}이 {}로 말을 합니다.'.format(person.name, person.language))

Human.speak = speak

person1.speak()
person2.speak()

