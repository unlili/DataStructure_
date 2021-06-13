'''

*args 和 **kwargs


'''
def	test_var_args(f_arg,	*argv):				
	'''
	argv 会把后面的变成一个列表输入进函数
	*args	是⽤来发送⼀个⾮键值对的可变数量的参数列表给⼀个函数.
	'''
	print("first	normal	arg:",	f_arg)				
	for	arg	in	argv:								
		print("another	arg	through	*argv:",arg)


test_var_args('yasoob',	'python',	'eggs',	'test')


#**kwargs	允许你将不定长度的键值对,	作为参数传递给⼀个函数。
def	greet_me(**kwargs):				
	for	key,	value	in	kwargs.items():								
		print("{0}	==	{1}".format(key,	value))

greet_me(n="aa",a="ee")

#=================================================================================

def	test_args_kwargs(arg1,	arg2,	arg3):				
	print("arg1:",	arg1)				
	print("arg2:",	arg2)				
	print("arg3:",	arg3)

args = ["two",3,5]
test_args_kwargs(*args)

args = ("two","haha","wo")
test_args_kwargs(*args)

kwargs	=	{"arg3":3,"arg2":"two","arg1":5}
test_args_kwargs(**kwargs)
