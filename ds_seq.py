shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
#indexing or ‘Subscription' operation#
#索引或“下标（subscription）”操作符#
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
#负数表示倒着数，-1就是倒数第一
print('Item -2 is', shoplist[-2])
#-2表示倒数第二
print('Character 0 is', name[0])

#Slicing on a list#
print('Item 1 to 3 is', shoplist[1:3])
#冒号后的序列不包括在内
print('Item 2 to end is', shoplist[2:])
#从二到结尾，不需要指定结尾的序列
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
#从头到尾的话，不需要指明具体序列，只要一个：就可以

#从某一字符串中切片#
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

#还可以设置步长#
print('默认步长是1', shoplist[::1])
print('设置步长为2', shoplist[::2])
print('设置步长是3', shoplist[::3])
print('设置步长是负数', shoplist[::-1])
#步长是负数时，从后向前排列
print('设置步长是-2', shoplist[::-2])

