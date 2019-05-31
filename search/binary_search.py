#递归版本  最坏时间复杂度：O(logn)  最优时间复杂度：O(1)
def binary_search(alist,item):
	n = len(alist)
	if n > 0:
		mid = n//2
		if alist[mid] == item:
			return True
		elif alist[mid] > item:
			return binary_search(alist[:mid],item) #切片没有最后一个
		else:
			return binary_search(alist[mid+1:],item)
	return False

#非递归
def binary_search_2(alist,item):
	n = len(alist)
	first = 0
	last = n - 1

	while first <= last:

		mid = (first + last) // 2
		if alist[mid] == item:
			return True
		elif alist[mid] > item:
			last = mid - 1
		else:
			first = mid + 1
	return False

if __name__ == '__main__':

	#导入quick_sort
	import sys
	sys.path.append(r'./sort')
	from quick_sort import quick_sort

	a = [5,125,1,621,5,15,5,125,1,61,51,51,61,155,2,626,
         48,19,1,5662,52,64,8894,1,6,59,848,94,819]
	quick_sort(a,0,len(a)-1)
	print(a)
	print(binary_search(a,851))
	print(binary_search_2(a,851))