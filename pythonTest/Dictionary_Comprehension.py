# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:49:44 2019
@author: h5435
"""

students = ['태연','진우','정현','하늘','성진']
for number, name in enumerate(students) :
    print('{}번의 이름은 {}입니다.'.format(number, name))

students_dict = {'{}번'.format(number + 1) : name for number, name in enumerate(students)}
print(students_dict) 

scores = [85, 92, 78, 90, 100]

#zip을 통해 딕셔너리 생성 
for x, y in zip(students, scores) :
    print(x, y)
    
scores_dict = {student : score for student, score in zip(students, scores)}
print(scores_dict)