'''
双向链表实现 双端队列
	定义了一个父类，用于在两个节点之间进行插入，删除指定节点
LinkedDeque类方法
	first() 返回第一个元素
	last() 返回最后一个元素
	insert_first(e) 插入到队首
	insert_last(e) 插入到队尾
	delete_first() 删除队首
	delete_last() 删除队尾
'''

#定义异常类
class Empty(Exception):
	pass

class _DoubleLinkedBase:

	class _Node:
		def __init__(self,_element,_prev,_next):
			self._element = _element
			self._prev = _prev
			self._next = _next

	def __init__(self):
		self._header = self._Node(None,None,None)
		self._trailer = self._Node(None,None,None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	#predecessor n. 前任，前辈
	#successor n. 继承者；后续的事物
	#在两个节点之间插入并且返回该节点
	def _insert_between(self,e,predecessor,successor):
		node = self._Node(e,predecessor,successor)
		predecessor._next = node
		successor._prev = node
		self._size += 1
		return node

	#删除某一节点并且并返回其元素
	def _delete_node(self,node):
		#获取前一指针和后一指针
		predecessor = node._prev
		successor = node._next
		#修改前一指针的next 和后一指针的prev
		predecessor._next = successor
		successor._prev = predecessor

		self._size -= 1
		element = node._element
		#改None被python回收
		node._prev = node._next = node._element = None
		return element

class LinkedDeque(_DoubleLinkedBase):

	def first(self):
		if self.is_empty():
			raise Empty('队列为空')
		return self._header._next._element

	def last(self):
		if self.is_empty():
			raise Empty('队列为空')
		return self._trailer._prev._element

	def insert_first(self,e):
		#在head和头元素之间插入
		self._insert_between(e,self._header,self._header._next)

	def insert_last(self,e):
		#在尾元素和trailer之间插入
		self._insert_between(e,self._trailer._prev,self._trailer)

	def delete_first(self):
		if self.is_empty():
			raise Empty('队列为空')
		#直接调用删除方法
		self._delete_node(self._header._next)

	def delete_last(self):
		if self.is_empty():
			raise Empty('队列为空')
		self._delete_node(self._trailer._prev)

if __name__ == '__main__':
	ldq = LinkedDeque()
	print(len(ldq))
	ldq.insert_first(5) # 5
	ldq.insert_last(9) # 5 9
	ldq.insert_last(8) # 5 9 8
	ldq.insert_first(20) # 20 5 9 8
	ldq.insert_last('qqq') # 20 5 9 8 qqq
	print(ldq.is_empty())
	print(ldq.first())
	print(ldq.last())
	ldq.delete_first() # 5 9 8 qqq
	ldq.delete_first() # 9 8 qqq
	ldq.delete_last() # 9 8 
	print(ldq.first())
	print(ldq.last())


	
			