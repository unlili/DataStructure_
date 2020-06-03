#ifndef MYHEAP_H
#define MYHEAP_H

template<class T>
void mySwap(T &a, T &b)
{
	T tmp = a;
	a = b;
	b = tmp;
}
/*

*/
template<class T>
class Heap
{
public:
	Heap(int, bool);
	Heap(T * arr);
	virtual ~Heap();
	void push(const T &e);
	inline T & top() const;
	T & pop();
	inline bool isEmpty();
private:
	bool isMax;// true 大根堆 false 小根堆
	T * heapArray;
	int heapSize;
	int currentSize;//指向最后一个元素的后面，即每插入一个就加1
	void up(int index);
	void down(int index);
};

template<class T>
Heap<T>::Heap(int mx = 10, bool isMax = true)
{
	this->isMax = isMax;//大根堆
	if (mx < 1) throw "max size must be >=1 ";
	heapSize = mx;
	currentSize = 0;
	heapArray = new T[heapSize];
}

template<class T>
Heap<T>::~Heap()
{
	delete[] heapArray;
}

template<class T>
inline bool Heap<T>::isEmpty()
{
	return this->currentSize == 0;
}

template<class T>
void Heap<T>::push(const T & e)
{
	if (this->currentSize == heapSize) throw "Heap is full";
	heapArray[currentSize] = e;
	up(currentSize++);//向上heapify
}

template<class T>
void Heap<T>::up(int index)
{
	if (index == 0) return;

	if (this->isMax)
	{
		while (heapArray[index] > heapArray[(index - 1) / 2])
		{
			mySwap(heapArray[index], heapArray[(index - 1) / 2]);
			index = (index - 1) / 2;
		}
	}
	else
	{
		while (heapArray[index] < heapArray[(index - 1) / 2])
		{
			mySwap(heapArray[index], heapArray[(index - 1) / 2]);
			index = (index - 1) / 2;
		}
	}
}

template<class T>
void Heap<T>::down(int index)
{
	int extreme;
	int left = index * 2 + 1;
	int right = left + 1;

	while (index < currentSize / 2)
	{
		//获得子节点最大值下标
		if (this->isMax)
		{
			if ((right < currentSize) && heapArray[left] < heapArray[right])
				extreme = right;
			else
				extreme = left;

			if (heapArray[index] >= heapArray[extreme]) break;
		}
		else
		{
			if ((right < currentSize) && heapArray[left] > heapArray[right])
				extreme = right;
			else
				extreme = left;
			if (heapArray[index] <= heapArray[extreme]) break;
		}

		mySwap(heapArray[index], heapArray[extreme]);
		index = extreme;
		left = index * 2 + 1;
	}
}

template<class T>
inline T& Heap<T>::top() const
{
	return heapArray[0];
}

template<class T>
T& Heap<T>::pop()
{
	T tmp = heapArray[0];
	heapArray[0] = heapArray[--currentSize];
	down(0);
	return tmp;
}


#endif
