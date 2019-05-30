#
#
#
def merge_sort(alist):

	n = len(alist)
	if  n < 2:
		return 
	mid = n//2

	s1 = alist[:mid]
	s2 = alist[mid:]

	merge_sort(s1)
	merge_sort(s2)

	merge(s1,s2,alist)

#合并两个数组s1 s2 排序复制合并到alist中
def merge(s1,s2,alist):
	i = j = 0
	while i + j < len(alist):
		if j == len(s2) or ( i<len(s1) and s1[i]<s2[j]):
			alist[i+j] = s1[i]
			i += 1
		else:
			alist[i+j] = s2[j]
			j += 1

if __name__ == '__main__':
	a = [51,62,36,95,984,156,354,354,35,62,62,12,56,82,3,5,369,2564,814356]
	merge_sort(a)
	print(a)







