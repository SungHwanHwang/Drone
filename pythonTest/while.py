# 변수 초기화
"""
selected = None
while selected not in ['가위', '바위', '보'] :
	selected = input('가위, 바위, 보 중에 선택하세요 >')
	
print('선택된 값은 : ', selected)
"""

patterns = ['가위', '바위', '보']
length = len(patterns)

#for pattern in patterns : 
#	print(pattern)


#for i in range(len(patterns)) :
#	pattern = patterns[i]
#	print(pattern)
i = 0	
while i < length :
	print(patterns[i])
	i=i+1
	
	
	
selected = None;

while selected not in ['가위', '바위', '보'] :
	selected = input('가위바위보 중 하나 입력 > ')
print('최종입력 값 : ', selected)