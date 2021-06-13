
'''
	可迭代对象(Iterable)
	迭代器(Iterator)
	迭代(Iteration)-循环来遍历某个东西时，这个过程本⾝就叫迭代
'''

def generator_function():
	for i in range(10):
		yield i

#for in 可以遍历一个生成器
for item in generator_function():
	print(item)
print("-----------------------------------------------------------------------------")

#斐波那契数列的⽣成器
def fibon(n):
	a=b=1
	for i in range(n):
		yield a
		a,b = b,a+b
print(list(fibon(10)))

print("-----------------------------------------------------------------------------")

def	generator_function():				
	for	i	in	range(3):	
		yield	i 

#Python内置函数：next()。它允许我们获取⼀个序列的下⼀个元素。
gen	= generator_function()
print(next(gen))#	Output:	0
print(next(gen))#	Output:	1
print(next(gen))#	Output:	2
#print(next(gen))
print("-----------------------------------------------------------------------------")
#使用生成器遍历一个字符串
#内置函数，iter。它将根据⼀个可迭代对象返回⼀个迭代器对象。
my_string	=	"Yasoob"
my_iter	= iter(my_string) #iter
for i in range(len(my_string)):
	print(next(my_iter))

print("-----------------------------------------------------------------------------")
