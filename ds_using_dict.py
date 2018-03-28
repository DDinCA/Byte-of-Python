#"ab" 是address和book的缩写
ab = {'Swaroop': 'swaroop@swaroopch.com', 'Larry': 'larry@wall.org', 'Matsumoto': 'matz@ruby_lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
print("Swaroop's address is", ab['Swaroop'])

#删除一对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
#\n用来空一行

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
#{}表示这里要填入一个值，后面的format来定义填进去的具体值
#添加一行
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
