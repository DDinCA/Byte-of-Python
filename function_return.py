def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
#怎样只用一个input？
print((maximum(input(), input())))
#return 语句如果没有自己编辑一个值的话，会返回none
def some_function():
    pass
print(some_function())
#内置的max语句不能显示两者equal，只能显示值
print(max(input(), input()))
