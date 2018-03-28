#推荐总是使用括号来指明元组的开始和结束
#尽管括号只是一个可选选项
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
#把zoo作为一个整体带入了new zoo，所以new zoo一共只有三个个体
print('Number of cages in the new zoo is', len(new_zoo))
#这句其实就是计算new zoo里的个体数量
print('All animals in new zoo are', new_zoo)
#注意打印出的zoo是包括在括号里的
print('Animals brought from old zoo are', new_zoo[2])
#Python从0开始计数
print('Lase animal brought from old zoo is', new_zoo[2][2])
#new zoo【2】【2】，第一个【2】表示是new zoo中的第三个，第二个【2】表示new zoo中的第三个里的第三个
#看样子指定个数可以叠加
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))
#减去new zoo中最后那个zoo整体，同时加上zoo的数量
