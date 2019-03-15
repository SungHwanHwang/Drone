# paking : 포장, unpaking : 포장된 값에서 여러 값을 꺼내오는 것
a, b = 1, 2
print('{}, {}'.format(a, b))

c = (3, 4)
print(c)

d, e = c
print(d, ', ', e)

f = d, e
print(f)


# 기존 두 값의 순서 변경
x = 5
y = 10
temp = x

x = y
y = temp
print('{}, {}'.format(x, y))

# 파이썬에서 가능한 방법
x, y = y, x
print('{}, {}'.format(x, y))

# tuple을 활용한 함수에서 여러개의 값을 return 받는 방법
def tuple_func() :
	return 1, 2

q, w = tuple_func()
print('{}, {}'.format(q, w))