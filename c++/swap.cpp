#include<iostream>
#include<vector>
#include<ctime>
using namespace std;
void swap01(int & a,int & b)
{
	int temp = a;
	a = b;
	b = temp;
}
void swap02(int * a, int * b)//拷贝指针
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

template<typename T>
void swap03(T &a, T &b)
{
	int c = a;
	a = b;
	b = c;
}

template<typename T>
void printArray(T arr[],int count)
{
	for (int i = 0; i < count; i++)
	{
		cout << arr[i] << "  ";
	}
	cout << endl;
}

template<typename Q>
void printVector(vector<Q> v)
{
	for (vector<Q>::iterator it = v.begin(); it != v.end(); it++)
	{
		cout << *it << "  ";
	}
	cout << endl;
}

template<typename A>
vector<A> randomArray(vector<A> v)
{
	srand((unsigned int)time(NULL));//设置随机数种子
	vector<A> temp;
	for (int i = v.size(); i > 0; i--)
	{
		int index = rand() % i;
		temp.push_back( v.at(index) );
		v.erase(v.begin() + index);
	}
	return temp;
}
//冒泡
void bubbleSort(int arr[],int count)
{
	for (int i = 0; i < count; i++)// 0 1 2 3 4 5 6 7
	{
		for (int j = 0; j < count - i -1; j++)
		{
			if (arr[j + 1] > arr[j])  
				swap01(arr[j + 1], arr[j]);
		}
	}
}
//选择
void selectSort(int arr[], int count)
{
	for (int i = 0; i < count; i++)
	{
		for (int j = i + 1 ; j < count;j++)
		{
			if (arr[i] < arr[j]) swap01(arr[i],arr[j]);
		}
	}
}
//插入
// 3 7 5 1 9 0 3 5
// 0 1 2 3 4 5 6 7 
// 3 7 5 1 9 0 3 5
// 3 7 5   1 9 0 3 5
void insertSort(int arr[], int count)
{
	for (int i = 1; i < count; i++)
	{
		for (int j = i; j > 0; j--)
		{
			if (arr[j]<arr[j - 1]) swap01(arr[j], arr[j - 1]);
		}
	}
}

void insertSort02(int arr[], int count)
{
	for (int i = 1; i < count; i++)
	{
		for (int j = i; j > 0; j--)
		{
			if (arr[j] < arr[j - 1]) swap01(arr[j], arr[j - 1]);
		}
	}
}

int factorial(int a)
{
	if (a == 1) return 1;
	return a*factorial(a - 1);
}

int binarySearch(int arr[], const int x, const int n)
{
	int low = 0;
	int heigh = n - 1;
	int mid;
	while (low <= heigh)
	{
		mid = (low + heigh) / 2;
		if (arr[mid] == x) return mid;
		else if (arr[mid]>x)
		{
			heigh = mid - 1;
		}
		else if (arr[mid] < x)
		{
			low = mid + 1;
		}
	}
	return -1;
}

int binarySearch(int arr[], const int x,int left,int right)
{
	if (left <= right)
	{
		int mid = (left + right) / 2;
		if (arr[mid] > x) return binarySearch(arr, x, left, mid - 1);
		else if (arr[mid] < x) return binarySearch(arr, x, mid + 1, right);
		else return mid;
	}
	return -1;
}

void permutation(char arr[],int l,int r)
{
	if(l==r)
	{
		for (int i = 0; i <= r; i++)
			cout << arr[i];
		cout << endl;
	}
	else
	{
		for (int i = l; i <= r; i++)
		{
			swap03<char>(arr[l], arr[i]);
			permutation(arr, l + 1, r);
			swap03<char>(arr[l], arr[i]);
		}
	}
}

/*
//快排
void quickSort(int arr[], int count)
{

}


//归并
void mergeSort()
{

}
//堆排
void heapSort()
{

}
*/

int main()
{

	char a[] = "abcde";
	permutation(a, 0, 4);

	return 0;
}
