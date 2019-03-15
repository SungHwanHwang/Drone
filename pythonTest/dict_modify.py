# list 생각해보기
list = [1, 2, 3, 4, 5]

print(list)

list[2] = 33

print(list)

list.append(6)

print(list)

dict = {
	'one' : 1,
	'two' : 2
}

print(dict)

dict['one'] = 11

print(dict)

dict['three'] = 3

print(dict)

del(list[0])

print(list)

del(dict['one'])

print(dict)

# pop으로 index 첨자만 사용해서 list 값을 지울 수 있다.
list.pop(0)
print(list)
list.pop(1)
print(list)

# dict도 마찬가지
dict.pop('two')
print(dict)