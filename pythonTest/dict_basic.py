winTable = {
	'가위' : '보',
	'바위' : '가위',
	'보' : '바위',
}

def rsp(mine, yours) :
	if mine == yours :
		return 'draw'
	elif winTable[mine] == yours:
		return 'win'
	else :
		return 'lose'
		

		
mine = '가위'
yours = '바위'

print(rsp(mine,yours))

message = {
	'win' : '이겼다!',
	'lose' : '졌다...',
	'draw' : '비겼다'
}

print(message[rsp(mine, yours)])