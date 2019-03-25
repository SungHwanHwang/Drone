# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:12:55 2019

@author: h5435
"""
#python에서 메소드란 클래스에 포함되어 있는 함수를 가리키는 다른 이름을 말함

class Human() :
    '''인간'''
    def __init__(self, name, weight) :
        '''초기화 함수'''
        self.name = name
        self.weight = weight
        
    def __str__(self):
        '''문자열의 함수'''
        return '{}(몸무게 {}kg)'.format(self.name, self.weight)
    
    # 보통 메소드의 첫번째 인자는 self로 사용한다.
    def eat(self) :
        self.weight += 0.1
        print('{}가 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))
    
    def walk(self) :
        self.weight -= 0.1
        print('{}가 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))
        
    def speak(self, message) :
        print(message)
        

person = Human('사람', 60.5)
print(person)

