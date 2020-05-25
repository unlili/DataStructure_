#ifndef _BINARYTREE_H
#include<cstdlib>
#include<iostream>
#include<queue>
template<class T> class BinaryTree;

template<class T>
class treeNode
{
public:
	treeNode()
	{
		this->leftChild = NULL;
		this->rightChild = NULL;
	}
	T data;
	treeNode<T> * leftChild;
	treeNode<T> * rightChild;
};

template<class T>
class BinaryTree
{
public:
	void preOrder();   //前序    根左右
	void preOrder(treeNode<T> * cur);

	void inOrder();    //中序    左根右
	void inOrder(treeNode<T> * cur);

	void postOrder();  //后序    左右根
	void postOrder(treeNode<T> * cur);

	void levelOrder(); //层遍历 ===> 使用队列遍历 

	void visit(treeNode<T> * t);

	treeNode<T> * root;
};

template<class T>
void BinaryTree<T>::visit(treeNode<T> * t)
{
	std::cout << t->data;
}

template<class T>
void BinaryTree<T>::inOrder()
{
	this->inOrder(root);
}

template<class T>
void BinaryTree<T>::inOrder(treeNode<T> * cur)
{
	if (cur)
	{
		inOrder(cur->leftChild);
		visit(cur);
		inOrder(cur->rightChild);
	}
}

template<class T> 
void BinaryTree<T>::preOrder()
{
	preOrder(root);
}

template<class T>
void BinaryTree<T>::preOrder(treeNode<T> * cur)
{
	if (cur)
	{
		visit(cur);
		preOrder(cur->leftChild);
		preOrder(cur->rightChild);
	}
}

template<class T>
void BinaryTree<T>::postOrder()
{
	postOrder(root);
}

template<class T>
void BinaryTree<T>::postOrder(treeNode<T> * cur)
{
	if (cur)
	{
		postOrder(cur->leftChild);
		postOrder(cur->rightChild);
		visit(cur);
	}
}

template<class T>
void BinaryTree<T>::levelOrder()
{
	std::queue<treeNode<T>*> q;// 存放结点指针的队列
	treeNode<T> * cur = root;
	while (cur)
	{
		visit(cur);
		if (cur->leftChild) q.push(cur->leftChild);
		if (cur->rightChild) q.push(cur->rightChild);
		if (q.empty()) return;
		cur = q.front();
		q.pop();
	}
}

#endif
