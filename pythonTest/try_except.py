def safe_pop_print(list, index) :
	try :
		print(list.pop(index))
	except IndexError :
		print('{} index의 값을 가져올 수 없습니다.'.format(index))

text = '100%'
try :
	number = int(text)
except ValueError :
	print('{}는 숫자가 아니에요'.format(text))
		
safe_pop_print([1,2,3], 5)

try :
	import my_module
except ImportError :
	print('모듈이 없습니다.')
	