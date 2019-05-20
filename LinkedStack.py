'''
单向链表实现栈
	ls = LinkedStack() 通过LinkedStack创建一个栈对象
	       ls.push(e) 把e添加到栈s的顶部
	         ls.pop() 从栈s中移除并且返回栈顶元素
	         ls.top() 在不移除栈顶元素的情况下，返回顶部元素；若栈为空抛出异常
	    ls.is_empty() 栈空返回True 
	          len(ls) 返回栈的长度
'''
#定义异常类
class Empty(Exception):
	pass

class LinkedStack:

	#定义一个内部类，节点类
	class _Node:
		__slots__ = '_element','_next'

		def __init__(self,_element,_next):
			#储存的元素
			self._element = _element
			#指向下一个节点的指针
			self._next = _next

	def __init__(self):
		#定义头元素
		self._head = None
		#记录栈元素数量
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def push(self,e):
		#创建一个节点给head，并且原来的_head为新节点的_next
		self._head = self._Node(e,self._head)
		self._size += 1

	def top(self):
		if self.is_empty():
			raise Empty('栈为空')
		return self._head._element

	def pop(self):
		if self.is_empty():
			raise Empty('栈为空')
		answer = self._head._element
		#把新的头部节点赋值给_head
		self._head = self._head._next
		self._size -= 1
		return answer
'''
ls = LinkedStack()
print(ls.is_empty())
ls.push(1) # 1
ls.push(2) # 2 1
ls.push(3) # 3 2 1
print(ls.top()) # 3 2 1
print(ls.pop()) # 2 1
print(len(ls)) # 2 1
'''
