# list 일 때 루프
seasons = ['봄', '여름', '가을', '겨울']

for season in seasons :
	print(season)
	
# dictionary 일 때 루프
ages = {
	'Tod' : 35,
	'Jane' : 23,
	'Paul' : 62
}

print(ages)

for key in ages.keys() :
	print(key)

for value in ages.values() :
	print(value)
	

# keys()는 생략이 가능 ex) for key in ages :	
for key in ages.keys() :
	print('{}의 나이는 {} 입니다.'.format(key, ages[key]))
	
# dict에서는 items() 함수를 써주면 key와 value의 값을 동시에 받을 수 있다.
for key, value in ages.items() :
		print('{}의 나이는 {} 입니다.'.format(key, value))

# dictionary는 값의 순서를 보장해 주지 않는다.