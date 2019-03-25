# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:50:01 2019
@author: h5435
"""

class Human() :
    '''인간'''
'''
person = Human()
person.name = '철수'
person.weight = 60.5
'''

def create_human(name, weight) :
    person = Human()
    person.name = name
    person.weight= weight
    return person

def eat(person) :
    person.weight += 0.1
    print('{}가 먹어서 {}kg이 되었습니다'.format(person.name, person.weight))
    
def walk(person) :
    person.weight -= 0.1
    print('{}가 걸어서 {}kg이 되었습니다'.format(person.name, person.weight))

Human.create = create_human
Human.eat = eat
Human.walk = walk

person = Human.create('철수', 60.5)
person.walk()
person.eat()
person.walk()
