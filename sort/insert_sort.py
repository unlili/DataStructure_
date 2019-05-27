#最优时间复杂度 O(n)
#最坏时间复杂度 O(n**2)
#稳定性：稳定
def insert_sort(alist):
	n = len(alist)
	#从右边的无序列表中取几个放到前面的有序中
	for i in range(1,n-1):
		#把i与前面的对比，放到合适的位置
		while i>0 :
			if alist[i] < alist[i-1]:
				alist[i],alist[i-1] = alist[i-1],alist[i]
				i -= 1
			else:
				break
			
if __name__ == '__main__':
	a = [65,65,62,96,48,2,63,954,962,325,333,3641]
	print(a)
	insert_sort(a)
	print(a)



