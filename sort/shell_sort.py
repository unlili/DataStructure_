#最坏时间复杂度 O(n^2)
#最优时间复杂度 不确定
#稳定性 不稳定
def shell_sort(alist):
	n = len(alist)
	gap = n // 2
	while gap > 0:# 1//2 == 0   1%2 == 1

		#一个根据步长的插入排序
		for i in range(gap,n):

			while i > 0:
				if alist[i-gap] > alist[i]:
					alist[i-gap],alist[i] = alist[i],alist[i-gap]
					i -= gap
				else:
					break
		gap //= 2

if __name__ == '__main__':
	a = [89,52,62,8,2,8,6,89,48,6,48,5,68]
	shell_sort(a)
	print(a)
