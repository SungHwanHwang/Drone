def add_10(value) :
	result = value + 10
	return result
	
def add_102(value) :
	if value <10 :
		return 10
	else:
		return value

print(add_10(10))

print(add_102(12))

# 파이썬은 여러 값 반환이 가능하다.
def print_sqrt(a, b, c) :
	r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	
	return r1, r2
	
a1, a2 = print_sqrt(1, 2, -8)

print('첫번째값 : {}'.format(a1))
print('두번째값 : {}'.format(a2))

