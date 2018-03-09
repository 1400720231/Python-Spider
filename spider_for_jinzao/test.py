# coding:utf-8
# author:mini_panda

# 读取所有站点名字共114个
names_all = []
with open('station_names.txt', 'r') as f:
    names = f.readlines()
    for name in names:
        names_all.append(name.strip('\n'))  # 去掉换行符
with open('result2.txt', 'w') as f:
    for i in names_all:
        f.write(i+ '\n')