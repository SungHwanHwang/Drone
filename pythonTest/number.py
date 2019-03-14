name = '드론'
age = 25

print('제이름은 ', name, '이고', ' 나이는 ', age, '살 입니다.')

power = 2**10

print(power);

stringPlus = '드론' + '날아간다.'

print(stringPlus)

# 파이썬 정수와 실수
# 나눗셈에서 정수 결과 값, 실수 결과 값 얻고 싶을 때

div1 = 6 / 5 #실수 결과 값
div2 = 6 // 5 # 정수 결과 값

print("{}, {}".format(div1, div2))

# 파이썬 실수는 부동소수점(완벽한 실수가 아님), 어느 정도의 오차 범위가 있다.
print(0.1 + 0.1 == 0.2) # True
print(0.1 + 0.1 + 0.1 == 0.3) #True

# 캐스팅
print(int(5.0))	# 정수로
print(float(5)) # 부동소수점으로
print(5*1.0) # 부동소수점으로