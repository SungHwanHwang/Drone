list2 = [37, 23, 10 ,33, 29, 40]
print(list2)

# 파이썬 배열 추가
list2.append(16)
print(list2)

# 파이썬 배열 추가2
list3 = list2 + [16]
print(list3)

list4 = list2 + list3
print(list4)

# n의 값이 list에 들어있는지 확인하는 ownerShip
n = 16
ownerShip = n in list3
print(ownerShip)

n = 10

if n in list3 : 
	print('{}은 있어'.format(n))
	

# 자리수로 지우는 법
print(list4)
del list4[12] # 12번째 자리 수를 지움
print(list4)

# 값 기준으로 지우는 법
# 같은 값이 여러개여도 가장 앞에 값 하나만 삭제
list4.remove(33)
print(list4)