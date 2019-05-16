'''

ArrayStack类的方法
	s = ArrayStack() 通过ArrayStack创建一个栈对象
	s.push(e) 把e添加到栈s的顶部
	s.pop(e) 从栈s中移除并且返回栈顶元素
	s.top() 在不移除栈顶元素的情况下，返回顶部元素；若栈为空抛出异常
	s.is_empty() 栈空返回True 
	len(s) 返回栈的长度

定义了一个异常类，在调用一个空栈的s.top方法时抛出

'''
class Empty(Exception):
	pass

class ArrayStack:

	def __init__(self):
		#定义一个列表来实现栈
		self._data = []

	def __len__(self):
		#返回栈中元素个数
		return len(self._data)

	def is_empty(self):
		#用len方法判断栈是否为空
		return len(self._data) == 0

	def push(self,e):
		#使用append方法把一个元素添加到列表尾部来代替添加到栈顶
		self._data.append(e)

	def top(self):
		#如果栈为空抛出Empty异常
		if self.is_empty():
			raise Empty('栈为空')
		return self._data[-1]

	def pop(self):
		#如果栈为空抛出Empty异常
		if self.is_empty():
			raise Empty('栈为空')
		#用列表的pop方法代替pop
		return self._data.pop()

'''
#简单测试
s = ArrayStack()
s.push(1)
print(s.is_empty())
s.push(2)
print(s.top())
s.push(3)
print(s.__len__())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s.top())
'''





