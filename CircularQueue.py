'''
循环链表实现循环队列
	尾指针的next指向头指针

CircularQueue类的方法
	cq = CircularQueue()  创建一个队列
	cq.is_empty() 判断是否为空
	cq.first() 返回队列第一个元素
	cq.dequeue() 返回并删除队首元素
	cq.enqueue(e) 向队尾添加一个元素
	len(cq)   队列长度
	rotate()  尾指针后移
'''

#定义异常类
class Empty(Exception):
	pass

class CircularQueue:
	#定义节点类
	class _Node:
		def __init__(self,_element):
			self._element = _element
			self._next = None

	def __init__(self):
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('队列为空')
		#尾指针的next指向头
		return self._tail._next._element

	def dequeue(self): #删除并返回第一个元素
		if self.is_empty():
			raise Empty('队列为空')
		result = self._tail._next._element
		if self._size == 1:
			#如果队列删除后只有一个，tail指向None
			self._tail = None
		else:
			#尾元素指针指向头元素的下一个元素
			self._tail._next = self._tail._next._next
		self._size -= 1
		return result
		
	def enqueue(self,e): #向队尾添加元素
		node = self._Node(e)
		if self.is_empty():
			node._next = node
		else:
			#新的指针指向头
			node._next = self._tail._next
			#原来指向头的指针指向新节点
			self._tail._next = node
		self._tail = node
		self._size += 1

	#实现指针后移
	def rotate(self):
		if self._size > 0:
			self._tail = self._tail._next

if __name__ == '__main__':
	# cq = CircularQueue()
	# cq.enqueue(1) # 1 
	# cq.enqueue(2) # 1 2 
	# cq.enqueue(3) # 1 2 3 
	# print(len(cq))
	# cq.enqueue(4) # 1 2 3 4 
	# cq.enqueue(5) # 1 2 3 4 5 
	# print(cq.first())
	# cq.enqueue(6) # 1 2 3 4 5 6
	# cq.dequeue()  # 2 3 4 5 6
	# print(cq.first())
	# print(len(cq))
	# cq.rotate() # 3 4 5 6 2
	# cq.dequeue()
	# print(cq.first())
