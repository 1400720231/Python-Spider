# coding: utf-8
# author: 1400720231

from transform_to_pinyin import chinese_into_letters
from times import get_times

# 读取所有站点名字共114个
names_all = []
with open('station_names.txt', 'r') as f:
    names = f.readlines()
    for name in names:
        names_all.append(name.strip('\n'))  # 去掉换行符

# 把往来站点组合排列，追加到from_to中,例如：深圳-茂名， 茂名-深圳，茂名-广州，广州-茂名等等
from_to = []
for a in range(0, len(names_all)):  # 每一个站与所有的站点排列组合桂林到桂林也是存在的，待会处理这里不处理
    A = names_all[a]
    for b in names_all:
        B = b
        # print(str(A)+'-'+str(B))
        from_to.append(str(A)+'-'+str(B))

# 把横着所有的站点写到txt进去，作为excel的横向标题：|a|b|c|d|
with open('result.txt', 'w') as f:
    for name in names_all:
        f.write(name+',')
    f.write('\n')  # 写近文件后换行
    count = 0  # 每当count = 114 的时候归零
    num = 0  # 打印第几次
    for i in from_to:  # 取n个出来先试一试
        STR = chinese_into_letters(i)  # 把字符串转化英文字母
        a, b = STR.split('-')
        # print(a,b)
        # 参考url：http://www.tieyou.com/daigou/guangzhou-shenzhen.html?date=2018-03-22&utm_source=tieyou&is_local=1
        url = 'http://www.tieyou.com/daigou/{A}.html?date=2018-03-22&utm_source=tieyou&is_local=1'.format(A=STR)
        # print(url)
        # print(get_times(url))
        if a == b:  # 判断始发站是否相同
            number = 0  # 始发站和终点站不能相同，若相同则赋值为0
            print(url)
            print(number)
            f.write(str(number) + ',')  # 因为excel默认分隔符是逗号，所以每次写入一个数据都加一个逗号
        else:
            try:
                number = get_times(url)
                print(url)
                print(number)
                f.write(str(number) + ',')  # 取出结果的对应的长度即可，因为我们要的只是次数
            except Exception as e:
                number = 'ERROR'
                f.write(str(number) + ',')  # 把错误写进txt防止空值错位，
                # print('错误的：', a, b)
                # print(url)
                # print(html)
                # raise e
        count += 1
        # 如果count=114，就换成下一行行，在excel中体现出来
        if count == len(names_all):
            f.write('\n')
            count = 0
        num += 1  # 最终的行数，按道理应该是114x114次
        print('第' + str(num) + '次'+'\n')
