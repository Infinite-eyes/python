# -*- codeing = utf-8 -*-
# @Time: 2020/6/27 22:33
# @Author :
# @File : 02遍历.py.py
# @Software： PyCharm


# namelist = ["小张","小王","小李"]
# for name in namelist:
#     print(name)
#
# nametemp = input("请输入添加的学生的姓名：")
# namelist.append(nametemp)
#
#
# for name in namelist:
#     print(name)
#
#


# 增
# a = [1,2]
# b = [3,4]
# a.append(b) #列表嵌套
# print(a)
#
# a.extend(b)
# print(a)
#


# a = [0,1,2]
# a.insert(1,3)
# print(a)


# 删


# movieName = ["加勒比海盗","骇客帝国","第一滴血","指环王","指环王","速度与激情"]
#
# for name in movieName:
#     print(name)
#
# # del movieName[2]# 删除指定下标
# # movieName.pop()  #删除最后一个
# movieName.remove("指环王") #删除指定一个
#
# for name in movieName:
#     print(name)

# 改

# namelist = ["小张","小王","小李"]
# namelist[0] = "fasfa"
# print(namelist)


# 查

# namelist = ["小张", "小王", "小李"]
# findName = input("请输入你要查找的学生姓名：")
#
# if findName in namelist:
#     print("1111")
# else:
#     print("22222")
#
# if findName not in namelist:
#     print("1111")
# else:
#     print("22222")


# a = ["a","b","c","a","b"]
# print(a.index("a",0,4))#可以查找指定下标范围元素 返回下标
# print(a.index("a",1,3))




#
# a = ["a","b","c","a","b"]
# print(a.count("c"));

#
# a = [1,4,2 ,3]
#
# print(a)
# a.reverse()
# print(a)
# a.sort() #升序
# a.sort(reverse=True)#降序
# print(a)


#二维数组
# schoolNames = [[],[],[]]
#
#
# schoolNames = [["北京大学","清华大学","南开","山东"],["北京大学","清华大学","南开","山东"],["北京大学","清华大学","南开","山东"]]
#
# print(schoolNames[0][0])


import random

offices = [[],[],[]]

names = ["A","B","C","D","E","F"]

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

print(offices)

i = 1
for office in offices:
    print("%d  - %d"%(i,len(office)))
    i +=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)











