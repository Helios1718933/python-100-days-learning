def onetofive():
    print('hello world')
    print('goodbye world')
    # 单行注释
    '''
    多行注释
    1
    2
    3
    '''
    print(0b100)  # 二进制整数
    print(0o100)  # 八进制整数
    print(100)    # 十进制整数
    print(0x100)  # 十六进制整数
    print(123.456)    # 数学写法
    print(1.23456e2)  # 科学计数法 表示$\small{1.23456 \times 10^{2}}$

    # str = "hello world" or str = 'hello world'
    # bool = True/False
    """
    惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
    惯例2：受保护的变量用单个下划线开头。
    惯例3：私有的变量用两个下划线开头。

    """

    """
    使用变量保存数据并进行加减乘除运算

    Version: 1.0
    Author: 骆昊
    """
    a = 45        # 定义变量a，赋值45
    b = 12        # 定义变量b，赋值12
    print(a, b)   # 45 12
    print(a + b)  # 57
    print(a - b)  # 33
    print(a * b)  # 540
    print(a / b)  # 3.75

    """
    使用type函数检查变量的类型

    Version: 1.0
    Author: 骆昊
    """
    a = 100
    b = 123.45
    c = 'hello, world'
    d = True
    print(type(a))  # <class 'int'>
    print(type(b))  # <class 'float'>
    print(type(c))  # <class 'str'>
    print(type(d))  # <class 'bool'>

    """
    变量的类型转换操作

    Version: 1.0
    Author: 骆昊
    """
    a = 100
    b = 123.45
    c = '123'
    d = '100'
    e = '123.45'
    f = 'hello, world'
    g = True
    print(float(a))         # int类型的100转成float，输出100.0
    print(int(b))           # float类型的123.45转成int，输出123
    print(int(c))           # str类型的'123'转成int，输出123
    print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
    print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
    print(float(e))         # str类型的'123.45'转成float，输出123.45
    print(bool(f))          # str类型的'hello, world'转成bool，输出True
    print(int(g))           # bool类型的True转成int，输出1
    print(chr(a))           # int类型的100转成str，输出'd'
    print(ord('d'))         # str类型的'd'转成int，输出100

    """
    算术运算符

    Version: 1.0
    Author: 骆昊
    """
    print(321 + 12)     # 加法运算，输出333
    print(321 - 12)     # 减法运算，输出309
    print(321 * 12)     # 乘法运算，输出3852
    print(321 / 12)     # 除法运算，输出26.75
    print(321 // 12)    # 整除运算，输出26
    print(321 % 12)     # 求模运算，输出9
    print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

    """
    算术运算的优先级

    Version: 1.0
    Author: 骆昊
    """
    print(2 + 3 * 5)           # 17
    print((2 + 3) * 5)         # 25
    print((2 + 3) * 5 ** 2)    # 125
    print(((2 + 3) * 5) ** 2)  # 625

    """
    赋值运算符和复合赋值运算符

    Version: 1.0
    Author: 骆昊
    """
    a = 10
    b = 3
    a += b        # 相当于：a = a + b
    a *= a + 2    # 相当于：a = a * (a + 2)
    print(a)      # 大家算一下这里会输出什么


    """
    海象运算符

    Version: 1.0
    Author: 骆昊
    """
    # SyntaxError: invalid syntax
    # print((a = 10))
    # 海象运算符
    print((a := 10))  # 10
    print(a)          # 10
    print(type(a := 10))    # <class 'int'>

    """
    比较运算符和逻辑运算符的使用

    Version: 1.0
    Author: 骆昊
    """
    flag0 = 1 == 1
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not flag0
    print('flag0 =', flag0)     # flag0 = True
    print('flag1 =', flag1)     # flag1 = True
    print('flag2 =', flag2)     # flag2 = False
    print('flag3 =', flag3)     # flag3 = False
    print('flag4 =', flag4)     # flag4 = True
    print('flag5 =', flag5)     # flag5 = False
    print(flag1 and not flag2)  # True
    print(1 > 2 or 2 == 3)      # False

    """
    将华氏温度转换为摄氏温度

    Version: 1.0
    Author: 骆昊
    """
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))

    """
    将华氏温度转换为摄氏温度

    Version: 1.1
    Author: 骆昊
    """
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print(f"{f:.1f}华氏度 = {c:.1f}摄氏度")

    """
    输入半径计算圆的周长和面积

    Version: 1.1
    Author: 骆昊
    """
    import math

    radius = float(input('请输入圆的半径: '))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(f'{perimeter = :.2f}')
    print(f'{area = :.2f}')
    """
    输入半径计算圆的周长和面积

    Version: 1.2
    Author: 骆昊
    """
    import math

    radius = float(input('请输入圆的半径: '))  # 输入: 5.5
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(f'{perimeter =}')  # 输出：perimeter = 34.56
    print(f'{area = :.2f}')       # 输出：area = 95.03

    year = int(input('请输入年份: '))
    anser = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    print(f'{anser:}')  # 输出：True/False

def five():
    weight = float(input('请输入体重(kg): '))
    height = float(input('请输入身高(cm): '))
    bmi = weight / (height / 100) ** 2  
    print(f'{bmi  = :.2f}')
    if 18.5 <= bmi < 24:
        print('正常范围')
    else:
        if bmi < 18.5:
            print('过轻')
        elif bmi > 27:
            print('过重')

def match_case():
    score = int(input('word input: '))
    match score % 2 == 0:
        case True:
            print('偶数')
        case False:
            print('奇数')
        case _:
            print('不及格')

def six():
    ins, ins_2 = 0, 0
    for i in range(10):
        ins += 1
        ins_2 += i
    print(f'{ins = :.2f}')
    print(f'{ins_2 =}')
    """
    range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
    range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
    range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
    range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到.
    """
    print(sum(range(0,101,2)))
    total = 0
    i = 0
    while i <= 100:
        total += i
        i += 2
    print(f'{total = }')

    for i in range(1,10):
        for j in range(1,i + 1):
            print(f'{i}x{j}={i * j}',end='\t')
        print()

    x = int(input('x = '))
    y = int(input('y = '))
    for i in range(x,0,-1):
        print(i)
        if x % i == 0 and y % i == 0:
            print(f'最大公约数:{i}')
            break
def seven():
    sum = 0
    for i in range(2,101):
        ans = True
        for j in range(2,i):
            if i % j == 0:
                ans = False
                break
        if ans:
            sum += i
    #        print(i)
    #print(sum)

    """
    输出100以内的素数

    Version: 1.0
    Author: 骆昊
    """
    sum = 0
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            sum += num 
            #print(num)
    #print(sum)
    a,b = 0,1
    for i in range(1,21):
        a,b = b,a+b
        #print(a)

    for i in range(100,1001):
        i_1 = i % 10
        i_2 = i // 10 % 10
        i_3 = i // 100 % 10
        #if i == i_1 ** 3 + i_2 ** 3 + i_3 ** 3:
            #print(f'yesnum:{i}')

    """
    找出100到999范围内的水仙花数

    Version: 1.0
    Author: 骆昊
    """
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        #if num == low ** 3 + mid ** 3 + high ** 3:
           # print(num)

    #num = int(input('input: '))
    num_1 = 0
    #while True:
        #num_1 = num_1 * 10 + num % 10
        #num //= 10
        #if num == 0:
            #print(f"output: {num_1} ")
            #break
    A = 0
    for i in range(0,20):
        for j in range(0,34):
            for k in range(0,301,3):
                if 5 * i + 3 * j + k // 3 == 100 and i + j + k == 100:
                    print(i,j,k)
    """
    百钱百鸡问题

    Version: 1.1
    Author: 骆昊
    """
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

    """
    Craps赌博游戏

    Version: 1.0
    Author: 骆昊
    """
    
def craps():
    import random
    money = 1000
    while money > 0:
        print(f'你现在的本金是：{money}')
        money_out = int(input('请下注：'))
        if money < money_out:
            money_out = int(input('请输入小于本金的金额：'))
            
        #下注金额确认；
        first_point = random.randrange(1,7) + random.randrange(1,7)
        if first_point == 7 or first_point == 11:
            money += money_out
            print('玩家获胜！游戏继续！')
            continue
        elif first_point == 2 or first_point == 3 or first_point == 12:
            money -= money_out
            print('庄家获胜！游戏继续！')
            continue
        #第一次游戏输赢判断；
        while True:
            next_point = random.randrange(1,7) + random.randrange(1,7)
            if next_point == 7:
                money -= money_out
                print('庄家获胜！游戏继续！')
                break
            elif next_point == first_point:
                money += money_out
                print('玩家获胜！游戏继续！')
                break
    print('你破产了')

def circuit():
    for i in range(1, 4):            # ① 外层循环 i = 1,2,3
        print(f'▶ [外层] i={i} 开始')
        for j in range(1, 4):        # ② 中层循环 j = 1,2,3
            print(f'  ▶ [中层] i={i} j={j} 开始')
            for k in range(1, 4):    # ③ 内层循环 k = 1,2,3
                print(f'    ▶ [内层] i={i} j={j} k={k} 进入')
                if (i == 1 and j == 2 and k == 2):   # ④ 内层 continue
                    print(f'    ✂ ④ continue 触发 → 跳回内层头部，取下一个 k')
                    continue
                if (i == 1 and j == 3):              # ⑤ 内层 break
                    print(f'    ✂ ⑤ break 触发 → 跳出内层，落回中层体内')
                    break
                print(f'    ✓ [内层] k={k} 正常执行完')
            print(f'  ▶ [中层] 内层结束，执行中层剩余代码 (i={i} j={j})')
            if (i == 2 and j == 2):                  # ⑥ 中层 continue
                print(f'  ✂ ⑥ continue 触发 → 跳回中层头部，取下一个 j')
                continue
            if (i == 2 and j == 3):                  # ⑦ 中层 break
                print(f'  ✂ ⑦ break 触发 → 跳出中层，落回外层体内')
                break
            print(f'  ✓ [中层] j={j} 正常执行完')
        print(f'▶ [外层] 中层结束，执行外层剩余代码 (i={i})')
        if (i == 3):                                 # ⑧ 外层 break
            print(f'✂ ⑧ break 触发 → 跳出外层循环')
            break
        print(f'✓ [外层] i={i} 正常执行完')
    print('■ 所有循环结束')

def list_show():
    items1 = [35, 12, 99, 68, 55, 35, 87]
    items2 = ['Python', 'Java', 'Go', 'Kotlin']
    items3 = [100, 12.3, 'Python', True]
    print(items1)  # [35, 12, 99, 68, 55, 35, 87]
    print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
    print(items3)  # [100, 12.3, 'Python', True]
    items4 = list(range(1, 10))
    items5 = list('hello')
    print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(items5)  # ['h', 'e', 'l', 'l', 'o']
    items5 = [35, 12, 99, 45, 66]
    items6 = [45, 58, 29]
    items7 = ['Python', 'Java', 'JavaScript']
    print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
    print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
    items5 += items6
    print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
    print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
    print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
    print(29 in items6)  # True
    print(99 in items6)  # False
    print('C++' not in items7)     # True
    print('Python' not in items7)  # False
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    print(items8[0])   # apple
    print(items8[2])   # pitaya
    print(items8[4])   # watermelon
    items8[2] = 'durian'
    print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
    print(items8[-5])  # 'apple'
    print(items8[-4])  # 'waxberry'
    print(items8[-1])  # watermelon
    items8[-4] = 'strawberry'
    print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
    print(items8[1:3:1])     # ['strawberry', 'durian']
    print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
    print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
    print(items8[-4:-2:1])   # ['strawberry', 'durian']
    print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
    print(items8[1:3])     # ['strawberry', 'durian']
    print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
    print(items8[::2])     # ['apple', 'durian', 'watermelon']
    print(items8[-4:-2])   # ['strawberry', 'durian']
    print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']
    items8[1:3] = ['x', 'o']
    print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']
    nums1 = [1, 2, 3, 4]
    nums2 = list(range(1, 5))
    nums3 = [3, 2, 1]
    print(nums1 == nums2)  # True
    print(nums1 != nums2)  # False
    print(nums1 <= nums3)  # True
    print(nums2 >= nums3)  # False
    languages = ['Python', 'Java', 'C++', 'Kotlin']
    for index in range(len(languages)):
        print(languages[index])
    languages = ['Python', 'Java', 'C++', 'Kotlin']
    for language in languages:
        print(language)
    """
    将一颗色子掷6000次，统计每种点数出现的次数

    Author: 骆昊
    Version: 1.1
    """
    import random

    counters = [0] * 6
    # 模拟掷色子记录每种点数出现的次数
    for _ in range(6000):
        face = random.randrange(1, 7)
        counters[face - 1] += 1
    # 输出每种点数出现的次数
    for face in range(1, 7):
        print(f'{face}点出现了{counters[face - 1]}次')

def list_way():
    languages = ['Python', 'Java', 'C++']
    languages.append('JavaScript')
    print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
    languages.insert(1, 'SQL')
    print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
    languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
    if 'Java' in languages:
        languages.remove('Java')
    if 'Swift' in languages:
        languages.remove('Swift')
    print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
    languages.pop()
    temp = languages.pop(1)
    print(temp)       # SQL
    languages.append(temp)
    print(languages)  # ['Python', C++', 'SQL']
    languages.clear()
    print(languages)  # []
    languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
    if 'Java' in languages:
        languages.remove('Java')
    if 'Swift' in languages:
        languages.remove('Swift')
    print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
    languages.pop()
    temp = languages.pop(1)
    print(temp)       # SQL
    languages.append(temp)
    print(languages)  # ['Python', C++', 'SQL']
    languages.clear()
    print(languages)  # []
    items = [1,2,1,3,1]
    print(type(items[0]))
    items.remove(1)
    print(items)
    items = ['Python', 'Java', 'C++']
    del items[1]
    print(items)  # ['Python', 'C++']
    items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
    print(items.index('Python'))     # 0
    # 从索引位置1开始查找'Python'
    print(items.index('Python', 1))  # 5
    print(items.count('Python'))     # 2
    print(items.count('Kotlin'))     # 1
    print(items.count('Swfit'))      # 0
    # 从索引位置3开始查找'Java'
    print(items.index('Java',2))    # ValueError: 'Java' is not in list
    items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
    items.sort()
    print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
    items.reverse()
    print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']
    items = []
    for i in range(1, 100):
        if i % 3 == 0 or i % 5 == 0:
            items.append(i)
    print(items)
    items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
    print(items)
    nums1 = [35, 12, 97, 64, 55]
    nums2 = []
    for num in nums1:
        nums2.append(num ** 2)
    print(nums2)
    nums1 = [35, 12, 97, 64, 55]
    nums2 = [num ** 2 for num in nums1]
    print(nums2)
    nums1 = [35, 12, 97, 64, 55]
    nums2 = []
    for num in nums1:
        if num > 50:
            nums2.append(num)
    print(nums2)
    nums1 = [35, 12, 97, 64, 55]
    nums2 = [num for num in nums1 if num > 50]
    print(nums2)
    scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
    print(scores[0])
    print(scores[0][1])
    scores = []
    for _ in range(5):
        temp = []
        for _ in range(3):
            score = int(input('请输入: '))
            temp.append(score)
        scores.append(temp)
    print(scores)
    import random
    scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
    print(scores)

def list_wor1():
    """
    双色球随机选号程序

    Author: 骆昊
    Version: 1.0
    """
    import random

    red_balls = list(range(1, 34))
    selected_balls = []
    # 添加6个红色球到选中列表
    for _ in range(6):
        # 生成随机整数代表选中的红色球的索引位置
        index = random.randrange(len(red_balls))
        # 将选中的球从红色球列表中移除并添加到选中列表
        selected_balls.append(red_balls.pop(index))
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    # 随机选择1个蓝色球
    blue_ball = random.randrange(1, 17)
    # 输出选中的蓝色球
    print(f'\033[034m{blue_ball:0>2d}\033[0m')

def rich_show():
    """
    双色球随机选号程序

    Author: 骆昊
    Version: 1.3
    """
    import random

    from rich.console import Console
    from rich.table import Table

    # 创建控制台
    console = Console()

    n = int(input('生成几注号码: '))
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]

    # 创建表格并添加表头
    table = Table(show_header=True)
    for col_name in ('序号', '红球', '蓝球'):
        table.add_column(col_name, justify='center')

    for i in range(n):
        selected_balls = random.sample(red_balls, 6)
        selected_balls.sort()
        blue_ball = random.choice(blue_balls)
        # 向表格中添加行（序号，红色球，蓝色球）
        table.add_row(
            str(i + 1),
            f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
            f'[blue]{blue_ball:0>2d}[/blue]'
        )

    # 通过控制台输出表格
    console.print(table)

def tuple_show():
    a, b, *c = range(1, 10)
    print(a, b, c)
    a, b, c = [1, 10, 100]
    print(a, b, c)
    a, *b, c = 'hello'
    print(a, b, c)
    import timeit

    print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
    print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
    infos = ('骆昊', 45, True, '四川成都')
    # 将元组转换成列表
    print(list(infos))  # ['骆昊', 45, True, '四川成都']

    frts = ['apple', 'banana', 'orange']
    # 将列表转换成元组
    print(tuple(frts))  # ('apple', 'banana', 'orange')


def str_show():
    s1 = '\'hello, world!\''
    s2 = '\\hello, world!\\'
    #print(s1)
    #print(s2)
    #s1 = '\it \is \time \to \read \now'
    s2 = r'\it \is \time \to \read \now'
    print(s1)
    print(s2)
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u9a86\u660a'
    print(s1)
    print(s2,ord('向'),ord('朝'),ord('阳'),ord('朝'))
    a = '骆昊'
    b = a.encode('utf-8')
    c = a.encode('gbk')
    print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
    print(c)                  # b'\xc2\xe6\xea\xbb'> 
    print(b.decode('utf-8'))  # 骆昊
    print(c.decode('gbk'))    # 骆昊`

def set_show():
    set1 = {1, 2, 3, 3, 3, 2}
    #print(set1)

    set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
    #print(set2)

    set3 = set('hello')
    #print(set3)

    set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
    #print(set4)

    set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
    #Wprint(set5)
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    for elem in set1:
        print(elem,len(set1))
    set1 = {1, 2, 3, 4, 5, 6, 7}
    set2 = {2, 4, 6, 8, 10}

    # 交集
    print(set1 & set2)                      # {2, 4, 6}
    print(set1.intersection(set2))          # {2, 4, 6}

    # 并集
    print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
    print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

    # 差集
    print(set1 - set2)                      # {1, 3, 5, 7}
    print(set1.difference(set2))            # {1, 3, 5, 7}

    # 对称差
    print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
    print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
    set1 &= set2
    print(set1)                             #例如：`set1 |= set2`相当于`set1 = set1 | set2`，跟`|=`作用相同的方法是`update`；`set1 &= set2`相当于`set1 = set1 & set2`，跟`&=`作用相同的方法是`intersection_update`
    set1 = {1, 3, 5}
    set2 = {1, 2, 3, 4, 5}
    set3 = {5, 4, 3, 2, 1}

    print(set1 < set2)   # True
    print(set1 <= set2)  # True
    print(set2 < set3)   # False
    print(set2 <= set3)  # True
    print(set2 > set1)   # True
    print(set2 == set3)  # True

    print(set1.issubset(set2))    # True
    print(set2.issuperset(set1))  # True
    set1 = {1, 10, 100}

    # 添加元素
    set1.add(1000)
    set1.add(10000)
    print(set1)  # {1, 100, 1000, 10, 10000}

    # 删除元素
    set1.discard(10)
    if 100 in set1:
        set1.remove(100)
    print(set1)  # {1, 1000, 10000}

    # 清空元素
    set1.clear()
    print(set1)  # set()
    set1 = {'Java', 'Python', 'C++', 'Kotlin'}
    set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
    set3 = {'HTML', 'CSS', 'JavaScript'}
    print(set1.isdisjoint(set2))  # False
    print(set1.isdisjoint(set3))  # True
    fset1 = frozenset({1, 3, 5, 7})
    fset2 = frozenset(range(1, 6))
    print(fset1)          # frozenset({1, 3, 5, 7})
    print(fset2)          # frozenset({1, 2, 3, 4, 5})
    print(fset1 & fset2)  # frozenset({1, 3, 5})
    print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
    print(fset1 - fset2)  # frozenset({7})
    print(fset1 < fset2)  # False

def dictionary_show():
    xinhua = {
        '麓': '山脚下',
        '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
        '蕗': '甘草的别名',
        '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
    }
    print(xinhua,type(xinhua))
    person = {
        'name': '王大锤',
        'age': 55,
        'height': 168,
        'weight': 60,
        'addr': '成都市武侯区科华北路62号1栋101', 
        'tel': '13122334455',
        'emergence contact': '13800998877'
    }
    print(person,type(person))
    person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
    print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

    # 可以通过Python内置函数zip压缩两个序列并创建字典
    items1 = dict(zip('ABCDE', '12345'))
    print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
    items2 = dict(zip('ABCDE', range(1, 10)))
    print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

    # 用字典生成式语法创建字典
    items3 = {x: x ** 3 for x in range(1, 6)}
    print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
    person = {
        'name': '王大锤',
        'age': 55,
        'height': 168,
        'weight': 60,
        'addr': '成都市武侯区科华北路62号1栋101'
    }
    print(len(person))  # 5
    for key in person:
        print(key,person[key])
    person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

    # 成员运算
    print('name' in person)  # True
    print('tel' in person)   # False

    # 索引运算
    print(person['name'])
    print(person['addr'])
    person['age'] = 25
    person['height'] = 178
    person['tel'] = '13122334455'
    person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
    print(person)

    # 循环遍历
    for key in person:
        print(f'{key}:\t{person[key]}')
    person1 = {'name': '王大锤', 'age': 55, 'height': 178}
    person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
    person1.update(person2)
    print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
    person1 = {'name': '王大锤', 'age': 55, 'height': 178}
    person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
    person1 |= person2
    print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
    person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
    print(person.pop('age'))  # 25
    print(person)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
    print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
    print(person)             # {'name': '王大锤', 'height': 178}
    person.clear()
    print(person)             # {}
    person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
    del person['age']
    del person['addr']
    print(person)  # {'name': '王大锤', 'height': 178}

def dict_ex():
    sentence = input('请输入一段话: ')
    counter = {}
    for ch in sentence:
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            counter[ch] = counter.get(ch, 0) + 1
    sorted_keys = sorted(counter, key=counter.get, reverse=True)
    for key in sorted_keys:
        print(f'{key} 出现了 {counter[key]} 次.')

def get_ex():
    person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
    for key in person:
        print(person.get(key)) 
    for key in person.items():
        print(f'{key}',type(key))


def make_judgement(*,a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

def add(a=0, b=0, c=0):
    """三个数相加求和"""
    print(a,b,c,end='\n')
    return a + b + c

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')

def captcha_generate(*,len = 4):
    import random
    import string

    ALL_CHARS = string.digits + string.ascii_letters
    print(ALL_CHARS)
    return ''.join(random.choices(ALL_CHARS, k=len)) 



1231231231231231

if __name__ == '__main__':
    print(captcha_generate(len = 5))