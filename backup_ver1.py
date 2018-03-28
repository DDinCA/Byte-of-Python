import  os
import time
#1.需要备份的文件与目录将被指定在一个列表中。
#例如在Windows下：
# source = ['"c:\\My Documents"', 'C:\\Code']
#又例如在 Mac OS X 与Linux下：
source = ['E:\\Study']
#在字符串中使用双引号用来括起其中包含的空格
#2.备份文件必须存储在一个主备份目录中
#例如在windows下：
# target_dir = 'E:\\Backup'
#又例如在Linux下：
target_dir = 'E:\\Learn'

#3.将备份文件打包成zip文件
#4.zip文件的文件名由当前的日期和时间组成
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#os.sep是系统自己分配的分隔符，根据系统不一样分配不同的分隔符

#如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)#mkdir是创建目录的意思，进过验证，可以创建
#5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
#{0} {1}表示顺序，{0}的地方是target，{1}的地方是后面的地址

#运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

