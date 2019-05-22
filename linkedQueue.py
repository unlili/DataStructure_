'''
单向链表实现队列
定义了一个尾指针，指向队尾元素，在删除元素时可以直接让队尾元素指向新元素，尾指针后移即可。
	LinkedQueue类的方法
	lq = LinkedQueue()  创建一个队列
	lq.is_empty() 判断是否为空
	lq.first() 返回队列第一个元素
	lq.dequeue() 返回并删除队首元素
	lq.enqueue(e) 向队尾添加一个元素
	len(lq)   队列长度

'''
#定义异常类
class Empty(Exception):
	pass

class LinkedQueue:

	#定义节点类
	class _Node:
		def __init__(self,_element):
			self._element = _element
			self._next = None

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('队列为空')
		#head指向头节点
		return self._head._element

	def dequeue(self): # dequeue() 返回并删除队首元素
		if self.is_empty():
			raise Empty('队列为空')

		#保存第一个元素
		result = self._head._element
		self._head = self._head._next
		self._size -= 1
		#删除元素后如果队列为空，尾指针指向None
		if self.is_empty():
			self._tail = None
		return result

	def enqueue(self,e): # enqueue(e) 向队尾添加一个元素
		node = self._Node(e)
		if self.is_empty():
			#如果队列为空，head直接指向node
			self._head = node
		else:
			#如果队列不为空，最后一个元素指向node
			self._tail._next = node
		#尾指针指向node（最后一个节点）
		self._tail = node
		self._size += 1


if __name__ == '__main__':
	lq = LinkedQueue()
	print(len(lq))
	print(lq.is_empty())
	lq.enqueue(1) # 1
	lq.enqueue(2) # 1 2
	lq.enqueue(3) # 1 2 3
	lq.enqueue(4) # 1 2 3 4
	lq.enqueue(5) # 1 2 3 4 5
	print(len(lq))
	print(lq.first())
	lq.dequeue() # 2 3 4 5
	lq.dequeue() # 3 4 5
	print(lq.first())
	print(len(lq))
	print(lq.is_empty())










