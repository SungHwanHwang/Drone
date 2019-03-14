scissor = '가위'
rock = '바위'
paper = '보'

win = '이겼다'
draw = '비겼다'
lose = '졌다'

result = ''

mine = paper
yours = rock

if mine == yours :
	result = draw
elif mine == rock :
	if yours == scissor :
		result = win
	if yours == paper :
		result = lose
elif mine == scissor :
	if yours == paper :
		result = win
	if yours == rock :
		result = lose
elif mine == paper :
	if yours == rock :
		result = win
	if yours == scissor :
		result = lose
			
print(result)
