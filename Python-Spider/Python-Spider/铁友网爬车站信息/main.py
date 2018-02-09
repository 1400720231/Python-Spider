# coding:utf-8
# author:panda
from time import time
from transform_to_pinyin import chinese_into_letters
from  times import get_times

# 读取所有站点名字
names_all = []
with open('station_names.txt', 'r') as f:
    names = f.readlines()
    for name in names:
        names_all.append(name.strip('\n'))  # 去掉换行符

# 把往来站点组合排列，追加到from_to中,例如：桂林-南宁
from_to = []
for a in range(0, len(names_all)):  # 每一个站与所有的站点排列组合桂林到桂林也是存在的，待会处理这里不处理
    A = names_all[a]
    for b in names_all:
        B = b
        # print(str(A)+'-'+str(B))
        from_to.append(str(A)+'-'+str(B))

# url = 'http://www.tieyou.com/daigou/nanning-guilin.html?date=2018-01-24&utm_source=tieyou&is_local=1'
# 把所有的站点写进去
with open('result.txt', 'w') as f:
    for name in names_all:
        f.write(name+',')
    f.write('\n')
    count = 0  # 每当count = 64 的时候归零
    num = 0  # 打印第几次
    for i in from_to:  # 取100 个出来先试一试
        STR = chinese_into_letters(i)  # 把字符串转化英文字母
        a,b = STR.split('-')
        # print(a,b)
        url = 'http://www.tieyou.com/daigou/{A}.html?date=2018-02-04&utm_source=tieyou&is_local=1'.format(A=STR)
        # print(url)
        # print(get_times(url))
        if a == b:  # 判断始发站是否相同
            number = 0  # 始发站和终点站不能相同，赋值为0
            print(url)
            print(number)
            f.write(str(number) + ',')
        else:
            try:
                number =get_times(url)
                print(url)
                print(number)
                f.write(str(number) + ',')  # 取出结果的对用的长度即可，因为我们要的只是次数
            except Exception as e:
                number = 'ERROR'
                f.write(str(number) + ',')  # 把错误写进txt防止空值错位，
                # print('错误的：', a, b)
                # print(url)
                # print(html)
                # raise e
        count += 1
        # 如果count=64，就换行，在excel中体现出来
        if count == len(names_all):
            f.write('\n')
            count = 0
        num += 1
        print('第' + str(num) + '次'+'\n')
