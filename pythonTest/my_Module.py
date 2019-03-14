def random_rsp() :
	""" 무작위로 가위바위보를 내는 """
	import random
	selected = random.choice(['가위', '바위', '보'])
	
	return selected
	
scissor = '가위'
rock = '바위'
paper = '보'