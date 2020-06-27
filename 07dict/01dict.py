# -*- codeing = utf-8 -*-
# @Time: 2020/6/27 23:18
# @Author :
# @File : 01dict.py
# @Software： PyCharm

#
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
#


# info = {"name":"吴彦祖","age":18}
#
# print(info["name"])
# print(info["age"])
# #访问了不存在的键 报错
# # print(info["gender"])
# # print(info.get("gender"))
# print(info.get("gender","m")) #设定默认值

info = {"name":"吴彦祖","age":18}
#增


# newID = input("请输入id：")
# info["id"] = newID
# print(info["id"])

#删

# print("%s "%info["name"])
# del info["name"]
# # print("%s "%info["name"]) #删除再掉会崩
# print(info.get("name", "m"))
#

# print("%s"%info)
# del info
# print("%s"%info)


#clear

# print("%s"%info)
# info.clear()#清空
# print("%s"%info)



#改
#
# info["age"] = 20
# print("%s" % info)
#

#查

# print(info.keys())
# print(info.values())
# print(info.items()) #每个键值对是一个元组


#遍历

# for key in info.keys():
#     print(key)
#
# for value in info.values():
#     print(value)


# for key,value in info.items():
#     print("key=%s,value=%s"%(key,value))


# mylist = ["a","b","c","d"]
#
# for x in mylist:
#     print(x)



mylist = ["a","b","c","d"]
print(enumerate(mylist))

for i,x in enumerate(mylist): #同时拿到列表下标和元素
    print(i,x)