#ifndef _MYQUEUE_H
#define _MYQUEUE_H
/*
front
	------------------
	* 9 6 5 3 9 7 5 3
	------------------
	                 rear
*/
template<class T>
class MyQueue
{
public:
	MyQueue(int queueCapacity = 10);
	~MyQueue();
	bool isEmpty() const;
	T& frontEle() const;
	T& rearEle() const;
	void push(const T & item);
	void pop();
private:
	int capacity;    //队列容量
	int front;    //队首下标
	int rear;     //队尾下标
	T * queue;       //创建动态数组
};

template<class T>
MyQueue<T>::MyQueue(int queueCapacity)
{
	this->capacity = queueCapacity;
	if (capacity < 1) throw "queue capacity must be > 0";
	queue = new T[capacity];
	front = rear = 0;
}
template<class T>
inline bool MyQueue<T>::isEmpty() const
{
	return front == rear;
}

template<class T>
void MyQueue<T>::push(const T & item)
{
	//if (rear == capacity - 1)
	//	rear = 0;
	//else

	if ((rear + 1) % capacity == front)
	{
		T* newQueue = new T[capacity * 2];

		int start = (front + 1) % capacity;//获取队首元素位置

		if (start < 2)//no wrap
			std::copy(queue + start, queue + start + capacity - 1,newQueue);
		else
		{
			std::copy(queue + start, queue + capacity, newQueue);
			std::copy(queue, queue + rear+1, newQueue + capacity - start);
		}
		front = 2 * capacity - 1;
		rear = capacity - 2;
		capacity *= 2;
		delete[]queue;
		queue = newQueue;
	}
	rear = (rear + 1) % capacity;
	queue[rear] = item;
}

template<class T>
inline T& MyQueue<T>::frontEle() const
{
	if (this->isEmpty()) throw "queue is empty. no front element";
	return queue[(front + 1) % capacity];
}

template<class T>
inline T& MyQueue<T>::rearEle() const
{
	if (this->isEmpty()) throw "queue is empty. no front element";
	return queue[rear];
}

template<class T>
void MyQueue<T>::pop()
{
	if (this->isEmpty()) throw "queue is empty. no front element";
	front = (front + 1) % capacity;
	queue[front].~T();
}

template<class T>
MyQueue<T>::~MyQueue()
{
	delete[] queue;
}

#endif

