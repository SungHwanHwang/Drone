# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:12:55 2019

@author: h5435
"""
#python에서 메소드란 클래스에 포함되어 있는 함수를 가리키는 다른 이름을 말함

class Human() :
    '''인간'''
    def create_human(name, weight) :
        person = Human()
        person.name = name
        person.weight = weight
        return person
    
    # 보통 메소드의 첫번째 인자는 self로 사용한다.
    def eat(self) :
        self.weight += 0.1
        print('{}가 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))
    
    def walk(self) :
        self.weight -= 0.1
        print('{}가 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))
        
    def speak(self, message) :
        print(message)
        

person = Human.create_human('철수', 60.5)
person.eat()
person.walk()
person.eat()

person.speak('안녕하세요 파이썬입니다.')