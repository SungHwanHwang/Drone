"""
def rsp(mine, yours) :
	#가위바위보 승패를 판단하는 코드
	winTable = {
		'가위' : '보',
		'바위' : '가위',
		'보' : '바위'
	}
	
	if mine not in winTable.keys() :
		raise ValueError
	if yours not in winTable.keys() :
		raise ValueError
	
	if mine == yours :
		print('비겼다')
	
	elif winTable[mine] == yours :
		print('이겼다')
	else :
		print('졌다')
			
try :
	rsp('가위', '바위')
except ValueError :
	print('잘못된 값을 넣었습니다.')
"""

school = {'1번' : }