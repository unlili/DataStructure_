#include<iostream>
#include<list>
using namespace std;

int getMaxDigit(int arr[],int n)
{
	int p = 1;
	int q = 10;
	for (int i = 0; i < n; i++)
	{
		while (arr[i] > q)
		{
			p++;
			q *= 10;
		}
	}
	return p;
}

void radixSort(int arr[],int n)
{
	int digits = getMaxDigit(arr, n);
	list<int> lists[10];//10 buckets
	int d, k, factor;
	int j;
	for (d = 1,factor=1; d <= digits;factor*=10,d++)
	{
		for (j = 0; j < n; j++)
		{
			lists[(arr[j] / factor) % 10].push_back(arr[j]);
		}
		for (j = k = 0; j < 10; j++)
		{
			while (!lists[j].empty() )
			{
				arr[k++] = lists[j].front();
				lists[j].pop_front();
			}
		}
	}
}

int main()
{
	int a[] = { 132432,433,43,34,7,657,6534,5654,75,62346 };
	int size = sizeof(a) / sizeof(int);

	radixSort(a, size);

	for (int i = 0; i < size; i++)
	{
		cout << a[i] << "  ";
	}cout << endl;

	return 0;
}
