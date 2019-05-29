#最坏时间复杂度 O(n**2) 每次划分只能分成一部分
#最优时间复杂度 O(nlogn) 交换为n 划分为logn
#稳定性：不稳定

def quick_sort(alist,first,last):
	#first快排的起始 low指针
	#last快排的结束 heigh指针

	#只有first小于last才进行递归
	if first >= last:
		return

	#一列表的第一个元素为中间值
	mid_value = alist[first]
	low = first
	heigh = last

	#循环执行者两个操作直到左边的比中间值小，右边的比中间值大
	while low < heigh:

		#heigh左移去找到一个比中间值小的给low的位置
		while low < heigh and alist[heigh] >= mid_value:
			heigh -= 1
		alist[low] = alist[heigh] 

		#low右移去找到一个比中间值大的给heigh的位置
		while low < heigh and alist[low] < mid_value:
			low += 1
		alist[heigh] = alist[low]

	#把中间值放到中间
	alist[low] = mid_value

	#通过手动传入参数，来控制递归是对一个列表进行操作
	quick_sort(alist,first,low-1)
	quick_sort(alist,low+1,last)

if __name__ == '__main__':
	a = [54,5,6,9,100,856,412,56,96,2,68,548,58,4598,5895,584,8485,48,54,8,4,854,95414,4,854,56,4]
	quick_sort(a,0,len(a)-1)
	print(a)







