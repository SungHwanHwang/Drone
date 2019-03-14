if True :
	print('블럭에 속한 코드')
	print('한줄 더')

print('이건 밖에')

if True :
	print('첫번째 출력이 되는 코드')
	
	if False :
		print('이건 실행 안됨')
	
	if True :
		print('이건 실행 됨')
		
print('최종 실행 됨')


if False :
	print('첫번째 출력이 되는 코드')
	
	if False :
		print('이건 실행 안됨')
	
	if True :
		print('이건 실행 됨')
		
print('제일 밖에 코드가 false일 때 그 조건 밖에 있는 것만 실행 됨')


