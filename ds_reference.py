print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist
#不论删除mylist还是shoplist，实际上两个是同一个序列，因此删掉之后两者输出的是一样的
del mylist[0]

print('Shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')

mylist = shoplist[:]
#因为是切片形成的列表，所以删掉拷贝出来的项不会影响原始列表
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
