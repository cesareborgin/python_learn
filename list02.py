# 有两个列表
# l1	=	[11,22,33]
# l2	=	[22,33,44]
# a.	 获取内容相同的元素列表
# b.	 获取 l1	 中有， l2 中没有的元素列表
# c.	 获取 l2	 中有， l1 中没有的元素列表
# d.	 获取 l1	 和 l2	 中内容都不同的元素
# l1	=	[11,22,33]
# l2	=	[22,33,44]
# for i in l1:
#     if i  in l2:
#         print(i)
# for i in l2:
#     if i not in l1:
#         print(i)
# for i in l1:
#     if i not in l2:
#         print(i)
# for i in l1,l2:
#     if i not in l1:
#         if i in l2:
#             print(i)
#     if i not in l2:
#         if i in l1:
#             print(i)

#有1-9数字组成互不相同的且不重的两位数
# count =0
# for w in range(1,9):
#     for v in range(1,9):
#         if w !=v:
#             count += 1
# print(count)

#99乘法表
# for i in range(1,10):
#     string = ""
#     for j in range(1,1+i):
#         string  += str(j) + "*" +str(i) + "="+str(i*j)+"\t"
#     print(string)
# 这里面的数字两个组合 多少种不同样的，数字不重复的
# li = [1,2,3,4,5,6]
# l = len(li)
# for i in range(0,l-1):
#     for v in range(i+1,l):
#         print(li[i],li[v])
# 公鸡5文一只，母鸡3文一只，小鸡3只1文，用100文买100只鸡，母鸡，小鸡都必须有，问公鸡、母鸡、小鸡要买多少只刚好凑足100文钱？
# for x in range(1,100//5):
#     for y in range(1,100//3):
#         for z in range(1,100):
#             if x+y+z == 100 and 5*x+y*3+z/3 == 100:
#                 print(x,y,z)

#利用下划线将列表元素拼接成一个字符串
# li = ["alex","eric","rain",123]
# li[3] = str(li[3])
# v = '_'.join(li)
# print(v)
# tu = ('alex', 'eric', 'rain')
# print(len(tu))
# print(tu[2])
# print(tu[1:])
# for elem in tu:
#     print(elem)
# for idx in range(len(tu)):
#     print(idx)
#
# for idx, elem in enumerate(tu, 10):
#     print(idx, elem)
# tu = ("alex",[11,22,{"k1":"v1","k2":["age","name"],"k3":(11,22,33)},44])
# tu[1][2]["k2"].append("sex")
nums = [2,7,11,15,1,8,7]
temp = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j] == 9:
            temp.append((i,j))
print(temp)