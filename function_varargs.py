def total(a = 5, *numbers, **phonebook):
    print('a', a)
#遍历元组中所有项目，元组即位置参数的合集，单个的，不带等号
    for single_item in numbers:
        print('single_item', single_item)
    #遍历字典中所有项目，字典即关键字参数的合集，带等号的
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
