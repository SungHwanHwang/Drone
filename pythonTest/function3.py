# a * x^2 + b * x + c = 0, a != 0 인 x에 관한 2차 방정식에 대해,
# 근의 공식은


def print_sqrt(a, b, c) :
	r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

	print('해는 {} 또는 {}'.format(r1, r2))

def print_round(number) :
	rounded = round(number)
	print(rounded)
ㅇ
# 실행인자
x = 1
y = 2
z = -8

		   #매개변수
print_sqrt(1, 2, -8)

print_round(2.2)
