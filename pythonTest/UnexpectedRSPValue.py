# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:06:09 2019
@author: h5435
"""
class UnexpectedRSPValue (Exception) :
    '''Exception Class를 상속(값이 가위 바위 보 가운데 아무것도 아닌 경우 발생하는 에러)'''

class BadUserName (Exception) :
    '''나쁜유저네임'''

class PasswordNotMatched(Exception) :
    '''패스워드가 맞지 않음'''