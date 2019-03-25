# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:15:52 2019

@author: h5435
"""

# 공유하는 클래스
class Animal() :
    def walk(self):
        print('걷는다')
    
    def eat(self) :
        print('먹는다')
    
    def greet(self) :
        print('인사한다')
        
class Cow(Animal) :
    '''소'''
    
# python 상속 방법
class Human(Animal) :
    
    def wave(self) :
        print('손을 흔든다')
        
    def greet(self) :
        self.wave()
        
class Dog(Animal) :
    
    def wag(self) :
        print('꼬리를 흔든다')
    
    def greet(self) :
        self.wag()
'''       
person = Human()
person.greet()

dog = Dog()
dog.greet()
'''
cow = Cow()
cow.greet()