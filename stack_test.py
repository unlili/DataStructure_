'''
简单的栈列子
验证一个表达式的括号是否匹配
	输入           输出
	(3+6)+(2-1)    true
	()[]{}         true
	{[()]}         true
	((             false
	))             false

'''
from stack import ArrayStack 

def is_matched(string):
	#创建一个栈
	s = ArrayStack()

	left = '{[('
	right = '}])'

	#遍历这个字符串
	for c in string:
		#如果c在left中则放入s中
		if c in left:
			s.push(c)

		elif c in right:
			if s.is_empty():
				#如果c在栈中，但是栈却为空说明缺少左边的匹配 列如 ))、{)}、{[)]}
				return False

			#c在right中，拿c在right中的索引 和 栈顶元素在left中的索引做比较，并且移除栈顶元素。列如 (}、([})、[}]
			if right.index(c) != left.index(s.pop()):
				return False

	#如果string为(( ，缺少右侧括号匹配，则栈不为空，返回false
	return s.is_empty()

#----------------------------------------
print(is_matched('(1+2)(4+5)[6666]'))
print(is_matched('(ff(ff[ff]'))
print(is_matched('f)fff)ff'))
print(is_matched('ff(ff}ff'))