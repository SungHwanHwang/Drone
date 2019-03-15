"""
list와 dict 비교들

>>> list = [1,2,3,4,5]
>>> dict = {'one':1, 'two':2, 'three':3 }
>>> list[0]
1
>>> dict['one']
1
>>> del(list[0])
>>> list
[2, 3, 4, 5]
>>> del(dict['one'])
>>> dict
{'two': 2, 'three': 3}
>>> len(list)
4
>>> len(dict)
2
>>> 1 in list
False
>>> 2 in list
True
>>> 5 in list
True
>>> 'two' in dict.keys()
True
>>> 'one' in dict.keys()
False
>>> 'one; in dict.values()
  File "<stdin>", line 1
    'one; in dict.values()
                         ^
SyntaxError: EOL while scanning string literal
>>> 'one' in dict.values()
False
>>> list.clear()
>>> dict.clear()
>>> dict
{}
>>> list
[]





>>> list = [1,2,3,4,5]
>>> dict = {'one':1, 'two':2, 'three':3}
>>> list.pop(0)
1
>>> list
[2, 3, 4, 5]
>>> dict1={1:100, 2:200}
>>> dict2={1:1000, 3:300}
>>> dict1.update(dict2)
>>> dict1
{1: 1000, 2: 200, 3: 300}
>>> dict1 = {1:100, 2:200}
>>> dict2={1:1000,3:300}
>>> dict2.update(dict1)
>>> dict2
{1: 100, 3: 300, 2: 200}
>>> dict1
{1: 100, 2: 200}
>>> dict2
{1: 100, 3: 300, 2: 200}
>>>


"""