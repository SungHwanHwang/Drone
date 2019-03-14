for i in [1, 2, 3, 4, 5] :
	print(i)
	
for i in range(5) :
	print(i+1)
	
names = ['철수', '영희', '바둑이', '귀도']

name = []

for i in range(4) :
	name.append(names[i])
	
print(name)

# 배열 길이 구하기
len(names)

for i in range(len(names)) :
	name = names[i]
	print('{}번째 : {}'.format(i+1, name))
	

# name = names[i] 과정을 한줄에 끝낼 때 enumerate를 사용	
for i, name in enumerate(names) :
	print('{}번째 : {}'.format(i+1, name))