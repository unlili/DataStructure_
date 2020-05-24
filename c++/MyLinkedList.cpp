#ifndef MYLINKEDLIST_H
#define MYLINKEDLIST_H

template<class T> class MyLinkedList;//类模板声明

template<class T>
class Node
{
	friend class MyLinkedList<T>;
public:
	T data; //数据域
	Node * link;//指针域
private:
	Node(T);
};

template<class T>
class MyLinkedList
{
public:
	MyLinkedList() { first = 0; length = 0; };      
	int  length;       //元素个数
	void insert(T);    //头插
	void deleteEle(T); //删除指定元素
	void invert();     //反转
	void show();
	void connect(MyLinkedList<T>);

private:
	Node<T> * first;
};

template<class T>
Node<T>::Node(T element)
{
	data = element;
}

template<class T>
void MyLinkedList<T>::insert(T k)
{
	/*
	frist -> [data|link] -> 0
	*/
	Node<T> * newNode = new Node<T>(k);
	newNode->link = first;
	first = newNode;
	length++;
}

template<class T>
void MyLinkedList<T>::deleteEle(T k)
{
	Node<T> * previous = 0;
	Node<T> * cur;
	//for (cur = first; 
	//	cur&& cur->data!=k; 
	//	previous=cur,cur = cur->link
	//	){;}
	
	cur = first;
	while(cur&&cur->data!=k)//定位该元素位置，previous保存前面的节点，
	{
		previous = cur;
		cur=cur->link;
	}
	
	if (cur)//判断链表是否为空
	{
		if (previous) previous->link = cur->link;//判断删除的元素是否为第一个
		else first = first->link;
		delete cur;
		length--;
	}
}

template<class T>
void MyLinkedList<T>::invert()
{
	Node<T> *p = first;
	Node<T> *q = 0;
	                                    
	while (p)
	{
		Node<T> * r = q;
		q = p;
		p = p->link;
		q->link = r;    
	}
	first = q;
}

template<class T>
void MyLinkedList<T>::connect(MyLinkedList<T> m)
{
	if (!first) { first = m.first; return; }//第一个链表是空的

	if (!m.first) { return; }//第二个链表是空的
	if (m.first)
	{
		Node<T> * it = this->first;
		while (it->link)
		{
			it = it->link;
		}
		it->link = m.first;
	}

}

template<class T>
void MyLinkedList<T>::show()
{
	for (Node<T> * cur = first; cur; cur = cur->link)
	{
		std::cout << cur->data;
		if (cur->link) std::cout << "->";
	}
	std::cout <<" "<< this->length<<" "<< std::endl;
}

#endif
