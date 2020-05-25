#include"binaryTree.h"
using namespace std;

int main()
{
	BinaryTree<char> bTree;
	//定义结点
	treeNode<char> plus, subtract,multiply,divide;
	treeNode<char> a, b, c, d, e;

	//赋值
	plus.data = '+';
	subtract.data = '-';
	multiply.data = '*';
	divide.data = '/';
	a.data = 'A';
	b.data = 'B';
	c.data = 'C';
	d.data = 'D';
	e.data = 'E';

	//--->构建二叉树
	bTree.root = &plus;
	plus.leftChild = &subtract;
	plus.rightChild = &e;
	subtract.leftChild = &multiply;
	subtract.rightChild = &d;
	multiply.leftChild = &divide;
	multiply.rightChild = &c;
	divide.leftChild = &a;
	divide.rightChild = &b;
	/*
	      +
	     ╱ ╲
		-   E
	   ╱ ╲
      *   D
	 ╱ ╲
    /   C
   ╱ ╲
  A   B
    */
	bTree.inOrder();
	cout << endl;
	bTree.preOrder();
	cout << endl;
	bTree.postOrder();
	cout << endl;
	bTree.levelOrder();
	return 0;
}
