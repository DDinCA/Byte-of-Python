import os
import time

source = ['E:\\Study']
target_dir = 'E:\\Learn'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#添加一条来自用户的注释用以创建zip文件的文件名
comment = input('Enter a comment --> ')
#检查是否有输入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
#NOW后面跟一个下划线，同时将评论中的空格用下划线代替，厉害！
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
