# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:30:13 2019
@author: h5435
"""

# 공유하는 클래스
class Animal() :
    def __init__(self, name) :
        self.name = name
    
    def walk(self):
        print('걷는다')
    
    def eat(self) :
        print('먹는다')
    
    def greet(self) :
        print('{}이/가 인사한다'.format(self.name))
        
class Human(Animal) :
    
    def __init__(self, name, hand) :
        super().__init__(name)
        self.hand = hand
    
    def wave(self) :
        print('{}을 흔들면서'.format(self.hand))
        
    def greet(self) :
        self.wave()
        super().greet() # 부모 : super()

person = Human('사람', '오른손')
person.greet()
