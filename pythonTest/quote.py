string1 = 'some text'
string2 = '어떤 텍스트'
string3 = '{}도 {}도 지금 이것도 문자열'.format(string1, string2)

print(string1, string2, string3)

# 파이썬은 긴 문자열 을 만들 때 작은 따옴표 혹은 큰 따옴표 3개를 사용하면 편하다.(줄 바꿈 인식, 내부 따옴표 재 사용 인식)

long_string = '''첫째줄은 좋은데
둘째줄도 괜찮을까?'''

print(long_string)