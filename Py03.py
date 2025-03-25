# print(10+10)

# print('10'+'10')

# print('你真的'+'很棒')

# n1='你真的'
# n2='很棒'
# print(n1,n2)
# print(n1,n2,sep='')

# print('666\n'*3)           #\n可以换行
#
# print('666\t'*3)           #\t可以间隔


# name='bingbing'
# print('i' in name)
# print('m' in name)
#
# print('i' not in name)
# print('m' not in name)       #so easy man!


# name=('冰冰')
# print('冰水'not in name)




# name='bingbing'
# print(name[0])
# print(name[-1])                  #从左往右是0开始，从右往左是-1开始。
# print(name[0:3])

# st='甲乙丙丁戊己庚辛壬癸'
# print(st[0:3])                   #包前不包后，0,1,2位就是甲乙丙
# print(st[0:])
# print(st[-1:])
# print(st[-1:-5:-1])              #从后往前，需要输入步长，-1代表方向，-1的绝对值1是顺着下一位取，-2就是顺两位也就是隔一个取。
# print(st[-1::-1])                #和从0开始类似，-1开始就是从右往左数，没有输入终点那就取全部，然后步长是1，方向是-1也就是从右往左。




# name='bingbing'
# print(name.find('n'))               #从0开始数。
# print(name.find('g',4))
# print(name.find('b',2,5))
# print(name.find('ngb'))              #ngb的n是从第2位开始。
# print(name.find('b',5))              #找不到就输出-1


# name='富贵险中求'
# print(name.index('贵'))
# print(name.index('贵',3))  #和find 区别是 找不到就‘报错’，find是输出-1。


# name='bingbing'
# print(name.count('b'))               #count是数个数，有几个b在这个name里面。
# print(name.count('b',1,4))      #包前不包后


# name='bingbing'
# print(name.startswith('b'))             #返回True或False
# print(name.startswith('i'))             #容易漏s，start s with
# print(name.startswith('n',3,6))


# name='bingbing'
# print(name.endswith('g'))                #容易漏s，start s with


# name='BINGBiNG'
# print(name.isupper())             #看是否是大写
# print('FUK YOU'.isupper())        #不用命名，直接写也行。


# name='我命油我不油天'
# print(name.replace('油','由'))                 #默认全部替换
# print(name.replace('油','由',1),)       #输入次数，改变替换的个数。


# name='bing,bing'
# print(name.split(','))             #这玩意挺抽象的，没整明白！


# name='bingbing'
# print(name.capitalize())              #把开头变大写，其他小写。


# name='BiNgbing'
# print(name.lower())            #大写变小写。


# name='BiNgbing'
# print(name.upper())            #小写变大写。


# name=[1,2,3,4]
# print(type(name))
# print(name[1:3])                 #包前不包后，输出也是列表格式。
# for i in name:
#     print(i)


# n1=['one','two','three']
# n1.append('four')
# print(n1)
# n1.extend('four')
# print(n1)
# n1.insert(3,'four')          #insert需要指定下标，从0开始。
# print(n1)


# N1=[1,2,3,4]
# N1.append(5)
# print(N1)
# N1.insert(4,5)
# print(N1)


# n1=[1,2,3,4,5]
# n1[2]='中间'
# print(n1)              #直接通过下标改正列表里面的内容，也是从0开始。


# n1=['1','2','3','4','5']       #别忘了引号
# print('6' in n1)               #查询在不在里面。
# print('1' in n1)
# print('2' not in n1)           #in  和  not in


# while True:                                         #记得后面的内容用Tab缩进。
#     n1=['bingbing','zara','hm','nike']
#     x1=input('请输入你的昵称：')
#     if x1 in n1:
#         print(f'您输入的昵称{x1}已存在')
#     else:
#         print(f'您输入的昵称{x1}可以使用')
#         n1.append(x1)
#         print(n1)
#         break                                       #break打断循环。



# n1=['a','b','c','d']
# del n1[2]                                             #从0开始，删掉c就是第2位。
# print(n1)


# n1=['a','b','c','d']
# n1.pop()                                              #不写下标，默认删除最后一个。
# n1.pop(2)
# print(n1)


# n1=['a','b','c','d']
# n1.remove('a')                                          #如果不知道用[]还是（），键盘输入remove的时候等一下它会出现指引。
# print(n1)


# n1=[1,5,8,56,76,79,78]
# n1.sort()                                            #顺序。用来排序的，用列表[]，不能用（）元组。
# n1.reverse()                                         #逆序。
# print(n1)


# n1=[1,3,6,7]
# [print(i*3) for i in n1]


# n1=[]
# for i in range(1,5):
#     n1.append(i)
# print(n1)                                            #把1234加进空的列表[]，第一种方法。

# n1=[]
# [n1.append(i) for i in range(1,5)]
# print(n1)                                            #把1234加进空的列表[]，第二种方法。


# n1=[]
# [n1.append(i)  for i in range (1,11) if i%2==1]
# print(n1)                                            #取奇数。


# n1=[1,3,4,6,[7,8,9]]
# print(n1[4][2])                                        #取嵌套里的数。


# a=(1,2,3)                 #元组用（）
# print(type(a))
# b=(1,)                    #只有一个元素后面要跟都好“，”，否则会输出括号内容的类型，1-整型。
# print(type(b))


# a=(1,2,3)
# print(a[2])                 #与列表不一样，只能支持查询，不能增删改。
# print(a[1:])


# name='bingbing'
# age=18
# print('%s的年龄是：%d'% (name,age))

# name='bingbing'
# age=18
# infor=(name,age)
# print('%s的年龄是：%d'% infor)


#字典dic={键1：值1，键2：值2}
#值重复，后面覆盖前面
























