# -*- coding: utf-8 -*-
"""
    raise : 에러를 발생시키는 역할
"""
def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed :
        raise ValueError
    if yours not in allowed :
        raise ValueError
        
    winnerTable = {'가위':'보',
                   '바위':'가위',
                   '보':'바위'
                   }
    if mine == yours :
        print('비겼다')
    elif winnerTable[mine] == yours :
        print('이겼다')
    else :
        print('졌다')
        

try :
    rsp('가','바위')
except ValueError:
    print('잘못된 값을 넣은 것 같습니다')
    
    
school = {'1반' : [172, 185, 198, 177, 165, 199],
          '2반' : [165, 177, 167, 180, 191]
          }
try:
    for class_number, students in school.items():
        for student in students :
            if student > 190 :
                print(class_number, '반에 190을 넘는 학생이 있습니다.')
                raise StopIteration # 이중 포문일 때 한번에 밖으로 빠져나가는 법
except StopIteration:
    print('정상종료')