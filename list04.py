name = 'hlf'

def change_name():
    print('我的名字',name)
change_name()

def change_name():
    name = 'Cesare'
    print('我的名字',name)
change_name()
print(name)

def change_name():
    global name
    print('我的名字', name)
    name = 'Cesare'
    print('我的名字',name)
change_name()
print(name)