# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:59:32 2019
@author: h5435
"""

from UnexpectedRSPValue import BadUserName, PasswordNotMatched
'''
value = '가'

# raise 에러명("에러 일 경우 표시할 문장")
try :
    if value not in ['가위', '바위', '보'] :
        raise UnexpectedRSPValue

except UnexpectedRSPValue :
    print('에러가 발생했습니다.')
'''
def sign_up() :
    ''' 회원 가입 함수 '''
    return True

try : 
    if sign_up() != False:
        raise PasswordNotMatched
        
except BadUserName :
    print('이름으로 사용할 수 없는 입력입니다.')
    
except PasswordNotMatched:
    print('입력한 패스워드가 서로 일치하지 않습니다.')