'''
双端队列
	     dq = Deque() 创建一个双端队列
	    dq.is_empty() 判断队列是否为空 *
   	   dq.add_first() 向队首添加元素
	    dq.add_last() 向队尾添加元素
	dq.delete_first() 获取并删除队首元素
	 dq.delete_last() 获取并删除队尾元素
	       dq.first() 返回队列第一个元素
	        dq.last() 返回队列最后一个元素
	    dq.is_empty() 判断是否为空
	          len(dq) 双端队列中元素的个数,使用__len__方法实现  *
'''
class Empty(Exception):
	pass

class Deque:
	#默认队列大小
	DEFAULT_CAPACUTY = 10

	def __init__(self):
		#初始化队列用于储存元素
		self._data = [None] * Deque.DEFAULT_CAPACUTY
		#队列中元素长度（大小）
		self._size = 0
		#队首元素索引
		self._front = 0

	#返回队列大小
	def __len__(self):
		return self._size

	#判断队列是否为空
	def is_empty(self):
		return self._size == 0

	#向队首添加元素
	def add_first(self,e):
		#如果队列装满，队列大小变为原来的两倍，并修改元素的索引，
		if self._size == len(self._data):
			self._resize(2 * len(self._data))

		#如果队首索引为0则新添加的队首为队列末端
		if self._front == 0:
			self._front = len(self._data) - 1
		else:
			self._front = self._front - 1
		self._data[self._front] = e
		self._size += 1

	#向队尾添加元素
	def add_last(self,e):
		#如果队列装满，队列大小变为原来的两倍
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
		#获取队尾索引
		point = (self._front + self._size) % len(self._data)
		self._data[point] = e
		self._size += 1

	def delete_first(self):
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

	def delete_last(self):
		if self.is_empty():
			raise Empty('队列为空')
		#获取队尾元素索引
		back = (self._front + self._size - 1) % len(self._data)
		#获取队尾元素
		answer = self._data[back]
		#设置队尾元素为空，被python回收，无法被引用
		self._data[back] = None
		#队列大小减一
		self._size -= 1
		return answer

	def first(self):
		if self.is_empty():
			raise Empty('队列为空')
		return self._data[self._front]

	def last(self):
		if self.is_empty():
			raise Empty('队列为空')
		#获取队尾元素索引
		back = (self._front + self._size - 1) % len(self._data)
		return self._data[back]

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


dq = Deque()
dq.add_first(1) # 1
dq.add_first(2) # 2 1
dq.add_first(3) # 3 2 1
print(dq.is_empty())
dq.add_last(2) # 3 2 1 2
dq.add_last(3) # 3 2 1 2 3
print(dq.first())
print(dq.last())
dq.delete_first() # 2 1 2 3
print(dq.first())
dq.delete_last() # 2 1 2
print(dq.last())
dq.delete_last() # 2 1
dq.delete_last() # 2
print(dq.first())
dq.delete_first() #
print(dq.is_empty())