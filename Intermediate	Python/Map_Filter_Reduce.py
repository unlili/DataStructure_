'''
Map会将⼀个函数映射到⼀个输⼊列表的所有元素上。
这是它的规范：map(function_to_apply,	list_of_inputs)
'''


'''
items	=	[1,	2,	3,	4,	5]
squared	=	[]
for	i	in	items:
	squared.append(i**2)
====>
'''

items	=	[1,	2,	3,	4,	5]
squared	=	list(map(lambda	x:	x**2,	items))

def	multiply(x):								
	return	(x*x)
def	add(x):								
	return	(x+x)

funcs	=	[multiply,	add]
for	i in range(5):# 0 1 2 3 4				
	value	=	map(lambda	x:x(i),	funcs)				
	print(list(value),end="-")
print()


number_list	= range(-5,	5)
less_than_zero = filter(lambda x:x > 1, number_list)#通过一个lamada对函数进行过滤
print(list(less_than_zero))		

from functools import reduce
product	= reduce((lambda x,	y: x * y), [1, 2,3,4,5,6,7,8,9]	)
print(product)
