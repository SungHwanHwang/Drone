list1 = [1, 2, 3, 4]
list1.append(5)

# index 첨자로 지우기
# list1.pop(0)
# del(list1[0])

# 값으로 지우기
list1.remove(1)

print(list1)

# 튜플 만들기
tuple1 = (1,2,3)
print(tuple1)

# list로 tuple 만들기
list1 = [1,2,3]
tuple3 = tuple(list1)
print(tuple3)

# tuple 로 값 얻기(index첨자로 얻을 수 있음)
print(tuple3[0])

# 튜플은 값의 수정 혹은 삭제가 불가능하다.