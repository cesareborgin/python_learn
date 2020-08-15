#高阶函数定义:
# 1.函数接收的参数是一个函数名
#
# 2.函数的返回值是一个函数名
#
# 3.满足上述条件任意一个,都可称之为高阶函数
# def foo():
#     print('我的函数名作为参数传给高阶函数')
# def high_order1(func):
#     print('我是高阶函数1,我接受的参数名是%s' %func)
#     func()
# def high_order2(func):
#     print('我是高阶函数2,我接受的参数名是%s' %func)
#     return func
# high_order1(foo)
# high_order2(foo)
#高阶函数应用1:把函数当做参数传给高阶函数
# import time
# def foo():
#     print('from the foo')
#
# def timmer(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print('函数%s 运行时间是%s' %(func,stop_time-start_time))
# timmer(foo)
# #总结:我们确实为函数foo增加了foo运行时间的功能,但是foo原来的执行方式是foo(),现在我们需要调用高阶函数timmer(foo),改变了函数的调用方式把函数当做参数传给高阶函数
# #五 函数嵌套
# def father(name):
#     print('from father %s' %name)
#     def son():
#         print('from son')
#         def grandson():
#             print('from grandson')
#         grandson()
#     son()
#
# father('林海峰')
# #六 闭包
# '''
# 闭包:在一个作用域里放入定义变量,相当于打了一个包
# '''
# def father(name):
#     def son():
#         name='alex'
#         print('我爸爸是 [%s]' %name)
#         def grandson():
#             name='wupeiqi'
#             print('我爷爷是 [%s]' %name)
#         grandson()
#     son()
#
# father('林海峰')
user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]

current_user={'username':None,'login':False}

def auth_deco(func):
    def wrapper(*args,**kwargs):
        if current_user['username'] and current_user['login']:
            res=func(*args,**kwargs)
            return res
        username=input('用户名: ').strip()
        passwd=input('密码: ').strip()

        for index,user_dic in enumerate(user_list):
            if username == user_dic['name'] and passwd == user_dic['passwd']:
                current_user['username']=username

                current_user['login']=True
                res=func(*args,**kwargs)
                return res
                break
        else:
            print('用户名或者密码错误,重新登录')

    return wrapper

@auth_deco
def index():
    print('欢迎来到主页面')

@auth_deco
def home():
    print('这里是你家')

def shopping_car():
    print('查看购物车啊亲')

def order():
    print('查看订单啊亲')

print(user_list)
# index()
print(user_list)
home()
