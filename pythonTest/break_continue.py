list = [1, 2, 3, 5, 7, 2, 5, 237, 55]

for i in list :
	if i % 3 == 0 :
		print(i)
		break;
		
# 블록 내로 너무 들어가지 않게 해준다.
for i in range(len(list)) :
	if i % 2 == 0 :
		continue
	print(i)
	print(i)
	print(i)
	print(i)
	