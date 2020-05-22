#ifndef _MYSTACK_H
#define _MYSTACK_H
#include"MyUtil.h"
/*
| 6 | <-top
| 3 |
| 7 |
| 3 |
| 9 |
| 4 |
|___|
*/
template<class T>
class MyStack
{
public:
	MyStack(int stackCapacity = 10);
	~MyStack();
	bool isEmpty() const;//常函数不能改变成员属性，成员属性前加mutable常函数就可以修改了，常对象只能调用常函数
	T& Top() const;
	void Push(const T& item);
	void Pop();
private:
	T * stack;  //动态创建数组
	int top;    //记录栈顶
	int capacity;
};

template<class T>
inline bool MyStack<T>::isEmpty() const
{
	return top == -1;
}

template<class T>
inline T& MyStack<T>::Top() const
{
	if (this->isEmpty())	throw "stack is empty";
	return stack[top];//==>? *(stack+top)
	
}

template<class T>
MyStack<T>::MyStack(int stackCapacity):capacity(stackCapacity)
{
	if (capacity < 1) throw "stack capacity must be > 0";
	stack = new T[capacity];
	top = -1;
}

template<class T>
MyStack<T>::~MyStack()
{
	delete[] stack;
}

template<class T>
void MyStack<T>::Push(const T& item)
{
	if (top == capacity - 1)
	{
		ChangeSize1D(stack, capacity, 2 * capacity);//stack数组大小乘二
		capacity *= 2;
	}
	stack[++top] = item;
}

template<class T>
void  MyStack<T>::Pop()
{
	if (this->isEmpty())	throw "stack is empty";
	stack[top--].~T();
}

#endif
