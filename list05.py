# def func(start,end,a=0,b=0):
#     if start == end:
#         return a,b
#     if start%3==0 and start%7==0:
#         a +=1
#         b +=start
#     res = func(start+1,end,a,b)
#     return res
# ret = func(1,21)
# print(ret)
# l1 = [11,22,33]
# l2 = [22,33,44]
# l3 =set(l1)&set(l2)
# print(l3)
#定义函数统计一个字符串中大写字母、小写字母、数字的个数、并以字典为结果返回给调用者
# 第一种方法：比大小
# def func1(x):
#     daxie = 0
#     xiaoxie = 0
#     num = 0
#     for i in x:
#         if i>='A' and i<='Z':
#             daxie +=1
#         if i>='a' and i<='z':
#             xiaoxie +=1
#         if str(i).isdigit():
#             num +=1
#     return {"大写字母个数": daxie, "小写字母个数": xiaoxie, "数字个数": num}
# a = func1("QWERvSdsd12Sssd34SD4453")
# print(a)
# def func2(x):
#     daxie = 0
#     xiaoxie = 0
#     num = 0
#     for i in x:
#         if i.isupper():
#             daxie +=1
#         if i.islower:
#             xiaoxie +=1
#         if str(i).isdigit():
#             num  +=1
#     return {"大写字母个数": daxie, "小写字母个数": xiaoxie, "数字个数": num}
# b = func2("HSKDHSKtdsg21237HHKsdsh")
# print(b)
#.利用内置函数zip(),join(),已知l1=["我",22,33,4,4]，l2=["爱",22,55,6,7]，l3=["学",22,33,44,5]，l4=["python",22,33,4,5] 获取字符串s = '我_爱_学_python'
# l1=["我",22,33,4,4]
# l2=["爱",22,55,6,7]
# l3=["学",22,33,44,5]
# l4=["python",22,33,4,5]
# l5= "_".join(list(zip(l1,l2,l3,l4))[0])
# print(l5)

# #利用递归实现 1*2*3*4*5*6*7 = 5040
# def func(n):
#     if n==1:
#         return 1
#     return n*func(n-1)
# print(func(7))
# 猴子第一天摘下若干桃子，当天吃了一半，感觉不过瘾就多吃列一个，第二天早上又将剩下的桃子吃了一半， # 还是不过瘾又多吃了一个，以后每天都吃前一天剩下的一半再加一个，到第10天刚好剩一个，第10天还没吃呢 # 问猴子第一天摘了多少桃子？
#  第一种方法
s = 1
func = lambda x:(x+1)*2
for i in range(0, 9):
    s = func(s)
print(s)
# 第二种方法,递归
# def func(x, day):
#     day -= 1
#     if day == 0:
#         return x #     x = (x+1)*2
#     ret = func(x, day)
#     return ret
# ret = func(1,10)
# print(ret)