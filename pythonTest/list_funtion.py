list1 = [135, 462, 27, 2753, 234]

# index 함수 사용하면 해당 () 내 값의 위치를 알 수 있다.
print(list1.index(27))

if 50 in list1:
    list1.index(50)
else:
    print('없음')

# list 합치기 '+'연산
list2 = [1,2,3] + [4,5,6]
print(list2)

#list 합치기 'extend'연산
list1.extend([9,10,11]) # 성능이 더 좋다.
print(list1)

#insert list.insert(자리수, 넣을 숫자)
list1.insert(2, 999)
print(list1)

# -1을 넣었을 땐 끝에자리를 옆으로 밀어내고 그 자리에 insert
# 자리수 넘치는 걸 index 값으로 주었을 때는 마지막에 값 삽입
list1.insert(10000, 555)
print(list1)

# list.sort()를 사용하면 정렬이 된다.
list1.sort()
print(list1)

#list.revers()를 사용하면 역정렬이 된다.
list1.reverse()
print(list1)