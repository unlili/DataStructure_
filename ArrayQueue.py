'''
队列（循环队列）
ArrayQueue类的方法
	q = ArrayQueue()  创建一个队列
	q.is_empty() 判断是否为空
	q.first() 返回队列第一个元素
	q.dequeue() 返回并删除队首元素
	q.enqueue(e) 向队尾添加一个元素
	q._size 队列中元素个数
	q._front 队首指针
'''

class Empty(Exception):
	pass

class ArrayQueue:
	#默认队列大小
	DEFAULT_CAPACUTY = 10

	def __init__(self):
		#初始化队列用于储存元素
		self._data = [None] * ArrayQueue.DEFAULT_CAPACUTY
		#队列中元素长度（大小）
		self._size = 0
		#队首元素索引
		self._front = 0

	def __len__(self):
		return self._size

	#判断队列是否为空
	def is_empty(self):
		return self._size == 0

	#获取队首元素
	def first(self):
		if self.is_empty():
			raise Empty('队列为空')
		return self._data[self._front]

	#获取并删除队首元素，队首索引变为 f = (f + 1) % size
	def dequeue(self):
		if self.is_empty():
			raise Empty('队列为空')
		#获取队首元素
		answer = self._data[self._front]
		#设置队首为空，被python回收，无法被引用
		self._data[self._front] = None
		#重新修改队首元素索引
		self._front = (self._front + 1) % len(self._data)
		#队列大小减一
		self._size -= 1
		return answer

	#修改队列长度为cap(cap大于size)，并且将原来队列的队首改为第一个元素
	#动态修改队列大小
	def _resize(self,cap):
		#保存旧的列表
		old = self._data
		#重新设置列表大小，并且全为None
		self._data = [None] * cap
		#获取队首元素索引
		point = self._front
		#遍历原来队列
		for i in range(self._size):
			#把旧的队列元素重新赋值给新的，可能有剩余
			self._data[i] = old[point]
			#修改队首指针
			point = (1+point) % len(old)
		#把队首索引改为一
		self._front =  0

	def enqueue(self,e):
		#如果队列装满，队列大小变为原来的两倍，并修改元素的索引，
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
		point = (self._front + self._size) % len(self._data)
		self._data[point] = e
		self._size += 1

'''
q = ArrayQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# 1 2 3
print(q.first()) # 1 2 3
print(q.is_empty()) # 1 2 3
print(q.dequeue()) # 2 3
print(q.dequeue()) # 3 
print(q.dequeue()) # 空
print(q.is_empty())
q.dequeue()
'''
