#选择排序

#最优时间复杂度
#最坏时间复杂度
#稳定性
def selection_sort(alist):
	n = len(alist)

	#比较的长度
	for j in range(n-1): # 0 ~ n-2
		#最小值索引
		min_index = j
		#遍历剩下的，把最小值索引给min_index
		for i in range(j+1,n):
			if alist[min_index] > alist[i]:
				min_index = i
		#把最小值放到开头
		alist[j],alist[min_index] = alist[min_index],alist[j]

	return alist

a = [1556,89,63,574,259,358,6,88,74,256,614]
print(a)
print(selection_sort(a)
)




