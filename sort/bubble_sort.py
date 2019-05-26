# coding:utf-8

# 最优时间复杂度O(n)
# 最坏时间复杂度O(n^2)
# 稳定性：稳定
def bubble_sort(alist):
	n = len(alist)
	#进行n-1次冒泡排序,每次冒泡需要进行比较的次数
	for i in range(n-1,0,-1): # i从n-1递减到1
		#用于判断是否进行交换
		flag = 0 
		for j in range(i): # 0 ~ i
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
				flag = 1
		#如果没有进行交换，证明队列就是有序的直接返回
		if flag == 0:
			return alist
	return alist

if __name__ == '__main__':
	a = [5,4,2,66,77,22,456,456,456,21578,434234,545,363,826,854.614,32,532,21,78]
	print(a)
	print(bubble_sort(a))