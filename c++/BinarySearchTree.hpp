#ifndef  BINARYSEARCHTREE_HPP
#define BINARYSEARCHTREE_HPP
#include<iostream>

// binary search tree
/*
template<class T>
		class Element<T>{T key};
		|
		class Node<T>{  Element<t> data };
		|
		class BST<T> {Node<T> * root};
*/
enum Boolean { FALSE, TURE }; //自定义布尔类型

template<class Type> class BST;//前置声明

template<class Type>
class Element
{
public:
	Type key;
};

template<class Type>
class Node
{
	friend class BST<Type>;
public:
	Element<Type> data;
	Node * leftChild;
	Node * rightChild;
	void display(int i);
};

template<class Type>
class BST
{
public:
	BST(Node<Type> * init = 0) :root(init) {};
	Boolean insert(const Element<Type> & x);

	Node<Type> * deleteEle(const Element<Type> & x);

	void inOrder();   //
	void preOrder();
	void postOrder();
	void levelOrder();

	Node<Type> * search(const Element<Type> & x);
	Node<Type> * search(Node<Type>*, const Element<Type>&);//递归查找



	Node<Type> * iterSearch(const Element<Type> &);//迭代查找
	void display()
	{
		if (this->root) root->display(1);
		else cout << "this tree is empty" << endl;
	}
private:
	Node<Type> * root;
};

template<class Type>
void Node<Type>::display(int i)
{
	if (this->leftChild) leftChild->display(2 * i);
	std::cout << "position:" << i << "  data.key" << this->data.key << "\n";
	if (this->rightChild) rightChild->display(2 * i + 1);
}

template<class Type>
Boolean BST<Type>::insert(const Element<Type> & x)
{
	Node<Type> * p = this->root;
	Node<Type> * q = 0;          //q指向p的父节点
	while (p)
	{
		q = p;
		if (x.key == p->data.key) return FALSE;//不允许重复

		// 必须是if else ,不能双if并列
		if (x.key < p->data.key)
			p = p->leftChild;
		else
			p = p->rightChild;
	}
	//找到的q的位置的左子或者右子就是插入元素的位置
	p = new Node<Type>;
	p->leftChild = p->rightChild = 0;
	p->data = x;

	if (!root) root = p;
	else if (x.key < q->data.key) q->leftChild = p;
	else if (x.key > q->data.key) q->rightChild = p;
	return TURE;
}

template<class Type>
Node<Type> * BST<Type>::search(const Element<Type> & x)
{
	return this->search(root, x);
}
template<class Type>
Node<Type> * BST<Type>::search(Node<Type> * cur, const Element<Type> & x)
{
	if (!cur) return 0;
	if (x.key == cur->data.key) return cur;
	if (x.key < cur->data.key) return search(cur->leftChild, x);
	return search(cur->rightChild, x);
}

template<class Type>
Node<Type> * BST<Type>::iterSearch(const Element<Type> & x)
{
	for (Node<Type> * t = this->root; t;)
	{
		if (x.key == t->data.key) return t;
		// if ~ else ~
		if (x.key < t->data.key)
			t = t->leftChild;
		else
			t = t->rightChild;
	}
	return 0;
}

template<class Type>
Node<Type> * BST<Type>::deleteEle(const Element<Type> & x)
{
	Node<Type> * t = this->root;
	Node<Type> * f = this->root;
	int pos = 0;// 要删除节点在其父节点的位置： -1：在左侧    1：在右侧    0：就是根节点 
	while (t)
	{

		if (x.key == t->data.key) break;
		// if ~ else ~
		else if (x.key < t->data.key)
		{
			f = t;
			t = t->leftChild;
			pos = -1;
		}
		else
		{
			f = t;
			t = t->rightChild;
			pos = 1;
		}
	}//找到该节点 t
	//该节点父节点 f
	//cout << "TEST_1" << endl;
	//cout << "TEST:" << t->data.key << endl;
	//cout << "TEST:" << f->data.key << endl;

	if (t)
	{
		if (t->leftChild && t->rightChild)//左右子树都存在
		{

			Node<Type> * leftMax = t->leftChild;
			Node<Type> * pre = t;

			while (leftMax->rightChild)
			{
				pre = leftMax;
				leftMax = leftMax->rightChild;
			}
			//std::cout << "---" << std::endl;
			//std::cout << leftMax->data.key << "\n";
			//std::cout << "---" << std::endl;
			//std::cout << pre->data.key << "\n";
			//std::cout << "---" << std::endl;
			Node<Type> * tmp = t;
			t->data = leftMax->data;

			if (pre->leftChild == leftMax)
				pre->leftChild = leftMax->leftChild;
			else
				pre->rightChild = leftMax->leftChild;
			return tmp;
		}
		//FINISh~~Yeah!!!
		else if (t->leftChild && !t->rightChild)//左子树存在，右子树不存在
		{
			if (pos == -1)
			{
				f->leftChild = t->leftChild;
			}
			else
			{
				f->rightChild = t->leftChild;
			}
			return t;
		}
		//FINISh~~Yeah!!!
		else if (t->rightChild && !t->leftChild)//右子树存在，左子树不存在
		{
			if (pos == -1)
			{
				f->leftChild = t->rightChild;
			}
			else
			{
				f->rightChild = t->rightChild;
			}
			return t;
		}
		else// FINISH~~Yeah!!!
		{
			Node<Type> * tmp = t;
			if (pos == 0) t = 0;//只有一个根节点且根节点就是要删除的节点
			else if (pos == -1) f->leftChild = 0;
			else f->rightChild = 0;
			return tmp;
		}
	}
	else
	{
		return NULL;
	}
}

#endif
