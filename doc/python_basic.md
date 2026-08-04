# Python 基础语法

本文面向刚开始学习 Python 的读者，示例默认适用于 Python 3。学习时建议在终端执行 `python3 文件名.py`，或在 Jupyter Notebook 中逐段运行代码并观察输出。

## 语法基础

### 注释与文档字符串

注释（comment）是写给读代码的人看的说明，Python 解释器不会执行 `#` 后的内容。应解释“为什么这样做”，不要重复代码本身已经清楚表达的事情。

```python
# 使用摄氏温度计算，避免与华氏温度混用
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
```

`#` 用于单行注释，也可以写在一行代码末尾，但行尾注释不宜过长。


```python
count = 0  # 已处理的记录数
```

三个引号包围的文本是**字符串**，不是严格意义上的“多行注释”。当它位于模块、类或函数的第一条语句时，它是文档字符串（docstring），可被 `help()` 等工具读取：

```python
def add(x, y):
    """返回两个数的和。

    参数:
        x: 第一个数
        y: 第二个数
    """
    return x + y
    


print(add(1.5, 2))  # 3.5
```

### 缩进与代码块

Python 用缩进表示代码块，不使用花括号。冒号 `:` 后通常需要一个缩进代码块。统一使用 **4 个空格**，不要混用 Tab 和空格。

```python
score = 85

if score >= 60:
    print("及格")
    if score >= 90:
        print("优秀")
else:
    print("需要继续练习")
```

缩进不一致会出现 `IndentationError`。编辑器中开启“显示空白字符”有助于排查这类问题。

### 变量、对象与类型

变量名是指向对象的标签；赋值用 `=`。Python 是动态类型语言：无需事先声明类型，变量也可以随后绑定到另一种类型的对象。

```python
name = "Alice"       # str（字符串）
age = 18              # int（整数）
height = 1.68         # float（浮点数）
is_student = True     # bool（布尔值）
nothing = None        # NoneType，表示“没有值”

print(type(name))
age = "十八岁"        # 合法，但通常不建议随意改变同一变量的含义
```

常用的基本类型包括 `int`、`float`、`str`、`bool` 和 `None`。使用 `type(value)` 查看类型；使用 `isinstance(value, 类型)` 判断对象是否属于某种类型：

```python
print(isinstance(3, int))       # True
print(isinstance(3, (int, float)))  # True
```

#### 命名规则与约定

- 变量名可由字母、数字和下划线组成，且不能以数字开头。
- 名称区分大小写：`total` 和 `Total` 是两个不同的名称。
- 不能使用关键字，例如 `if`、`class`、`for`；可用 `help("keywords")` 查看关键字。
- 变量和函数使用 `snake_case`，例如 `total_price`；类使用 `PascalCase`，例如 `StudentRecord`；常量通常使用全大写，例如 `MAX_RETRY`。
- 名称应表达含义。`student_count` 通常比 `n` 更清楚；循环下标等范围很小的场景可使用 `i`。

```python
student_count = 30
MAX_RETRY = 3

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

### 输入、输出与 f-string

`print()` 用于输出。`input()` 总是返回字符串；需要数值时要显式转换，并注意非法输入会引发 `ValueError`。

```python
name = input("请输入姓名：")
age = int(input("请输入年龄："))
print(f"你好，{name}！明年你将 {age + 1} 岁。")
```

f-string（以 `f` 开头的字符串）是格式化文本的推荐方式。花括号内可放变量或简单表达式：

```python
price = 12.5
quantity = 3
print(f"总价：{price * quantity:.2f} 元")  # 总价：37.50 元
```

### 运算符与比较

算术运算常用 `+`、`-`、`*`、`/`、`//`（整除）、`%`（取余）、`**`（幂）。比较运算的结果是布尔值。

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(2 ** 3)   # 8

print(3 == 3)   # True：比较值
print(3 != 4)   # True
print(3 > 4)    # False
```

比较值相等使用 `==`，赋值才使用 `=`。判断是否为 `None` 时使用 `is None`，不要写成 `== None`。

```python
result = None
if result is None:
    print("尚无结果")
```

## 容器与流程控制

### 列表、元组、字典和集合

```python
fruits = ["apple", "banana"]              # list：有序、可修改
point = (10, 20)                           # tuple：有序、通常不可修改
student = {"name": "Alice", "age": 18}  # dict：键值对
tags = {"python", "data", "python"}      # set：元素唯一、无固定顺序

fruits.append("orange")
print(fruits[0])           # apple，索引从 0 开始
print(student["name"])    # Alice
print(len(tags))           # 2
```

访问字典中可能不存在的键时，优先用 `get()` 提供默认值：

```python
city = student.get("city", "未知")
```

### 条件与循环

```python
temperature = 28
if temperature >= 30:
    message = "炎热"
elif temperature >= 20:
    message = "舒适"
else:
    message = "偏冷"

for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

`for` 适合遍历序列；`while` 适合“不满足条件就持续执行”的场景，必须确保条件最终会改变：

```python
attempt = 0
while attempt < 3:
    attempt += 1
```

## 函数

函数把可复用的操作封装起来。参数是函数接收的输入，`return` 把结果交还给调用者；没有 `return` 时函数默认返回 `None`。

```python
def greet(name, greeting="你好"):
    """返回一条问候语。"""
    return f"{greeting}，{name}！"


message = greet("小明")
print(message)
print(greet("Alice", greeting="Hello"))
```

避免把可变对象作为默认参数，因为默认值只会创建一次：

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## 模块、包与依赖

模块通常是一个 `.py` 文件；包是组织多个模块的目录。使用 `import` 导入所需内容，推荐导入明确的名称，避免 `from module import *`，因为它会污染命名空间。

```python
import math
import numpy as np
from pathlib import Path

print(math.sqrt(9))
print(np.arange(3))
print(Path("data") / "input.csv")
```

第三方包建议安装到虚拟环境中，避免不同项目的依赖互相影响：

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install numpy
```

## 常见问题速查

- `NameError`：变量或函数名尚未定义，检查拼写、大小写和执行顺序。
- `TypeError`：操作的类型不匹配，例如字符串不能直接与整数相加。
- `IndexError`：列表索引超出范围；有效索引范围是 `0` 到 `len(list) - 1`。
- `KeyError`：字典不存在该键；可先用 `in` 判断或改用 `dict.get()`。
- `SyntaxError`：语法有误，常见原因是漏写冒号、括号或引号。

学习建议：先运行小示例，再刻意修改一个值或一行代码，观察错误信息与输出的变化。Python 的报错回溯通常会指出文件、行号和出错类型，是定位问题的重要线索。



## Python 数据类型

### 数字

- `int`：整数，例如 `88`、`-88`、`0`，没有长度限制。
- `float`：浮点数，例如 `3.14`、`-0.5`。它以二进制近似存储小数，因此不适合直接比较金额等精确数值。
- `complex`：复数，例如 `3 + 4j`；`z.real` 和 `z.imag` 分别取得实部与虚部。

```python
x = 88
y = -8.88
z = 8 + 8j

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
print(abs(z))   # 复数的模长
```

常用类型转换如下。转换失败时，例如 `int("hello")`，会抛出 `ValueError`。

```python
print(int(3.9))       # 3：向 0 截断，不是四舍五入
print(int(-3.9))      # -3
print(float("3.14"))  # 3.14
print(complex(2, 3))  # (2+3j)
print(str(True))      # 'True'
```

浮点数比较应考虑误差；可使用 `math.isclose()`：

```python
import math

print(0.1 + 0.2 == 0.3)              # False
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### 字符串

字符串（`str`）是一串 Unicode 字符。可用单引号或双引号定义；三引号通常用于多行文本或文档字符串。字符串不可变，任何“修改”操作都会产生新字符串。

```python
message = "Python 很有趣"
print(message[0])      # P
print(message[-1])     # 趣
print(message[0:6])    # Python
print(message[:6])     # 从开头到索引 6（不包含 6）
print(message[::-1])   # 反转字符串
```

常用字符串方法：

```python
raw_name = "  Alice Smith  "
print(raw_name.strip())                 # 去除首尾空白
print(raw_name.strip().lower())         # 转为小写
print("a,b,c".split(","))              # ['a', 'b', 'c']
print("-".join(["2026", "08", "03"]))  # 2026-08-03
print("hello world".replace("world", "Python"))
```

字符串中的反斜杠用于转义，例如 `"\n"` 表示换行、`"\t"` 表示制表符。文件路径等不希望转义的内容可写成原始字符串：`r"C:\\data\\file.txt"`。

### 列表

列表（`list`）是有序、可变的序列，索引和切片规则与字符串相同。

```python
scores = [85, 92, 76]
scores.append(88)       # 末尾添加一个元素
scores.extend([90, 95]) # 添加多个元素
scores[0] = 86          # 按索引修改
last_score = scores.pop()  # 删除并返回最后一个元素

print(scores)
print(scores[1:3])
```

#### 打包、拆包与复制

```python
point = 10, 20          # 打包为元组
x, y = point            # 拆包
first, *middle, last = [1, 2, 3, 4]

original = [[1, 2], [3, 4]]
shallow_copy = original.copy()  # 只复制外层列表
shallow_copy[0].append(99)
print(original)  # 内层列表仍被共享
```

嵌套对象需要完全独立时，用 `copy.deepcopy()`：

```python
from copy import deepcopy

independent_copy = deepcopy(original)
```

### 元组、集合与字典

元组（`tuple`）有序但不可修改，适合固定的一组值；只有一个元素的元组必须带逗号：`single = (42,)`。

集合（`set`）不保留顺序且元素不重复，适合去重和集合运算：

```python
students_a = {"Alice", "Bob", "Chen"}
students_b = {"Bob", "David"}

print(students_a | students_b)  # 并集
print(students_a & students_b)  # 交集
print(students_a - students_b)  # 差集
```

字典（`dict`）保存键值对。键必须是可哈希的不可变对象，例如字符串、数字、元组；列表不能作为键。

```python
book = {"title": "Python 入门", "pages": 320}
book["author"] = "张三"
book["pages"] = 350

for key, value in book.items():
    print(f"{key}: {value}")

print(book.get("publisher", "未提供"))
```

### 推导式

推导式可简洁地从可迭代对象创建容器。逻辑复杂时应改用普通循环，以保证可读性。

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
lengths = {word: len(word) for word in ["Python", "AI", "data"]}
unique_lengths = {len(word) for word in ["cat", "dog", "Python"]}
```

## 异常处理与文件读写

### 异常处理

当程序遇到异常会中断。只捕获你能妥善处理的具体异常，避免使用空的 `except:` 或宽泛的 `except Exception:` 来掩盖程序错误。

```python
def read_positive_integer(text):
    try:
        value = int(text)
    except ValueError:
        return None

    if value <= 0:
        return None
    return value


print(read_positive_integer("12"))
print(read_positive_integer("abc"))
```

`finally` 中的代码无论是否发生异常都会执行，常用于清理资源。对于文件，优先使用 `with`，它会在代码块结束时自动关闭文件。

### 文件读写

使用 `pathlib.Path` 处理路径，比手写字符串拼接更可靠。读写中文文本时显式使用 `encoding="utf-8"`。

```python
from pathlib import Path

path = Path("notes") / "hello.txt"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text("第一行\n第二行\n", encoding="utf-8")

content = path.read_text(encoding="utf-8")
print(content)
```

大文件宜逐行读取，避免一次加载到内存：

```python
with Path("notes/hello.txt").open(encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

## 作用域与调试

函数内创建的变量是局部变量，函数外不能直接访问。函数可以读取外层变量；若要在函数内重新绑定全局变量，应尽量重新设计接口，避免滥用 `global`。

```python
tax_rate = 0.06

def final_price(price):
    discount = 0.9
    return price * discount * (1 + tax_rate)


print(final_price(100))
```

排查问题的基本顺序是：阅读异常回溯中最靠近自己代码的一行，确认输入值和类型，再缩小能复现问题的最小代码。临时使用 `print()` 查看状态很实用；较复杂的程序可使用标准库调试器：

```python
def divide(a, b):
    breakpoint()  # 程序在这里暂停，可输入 a、b 等表达式查看变量
    return a / b
```

在调试器中输入 `n` 执行下一行，输入 `c` 继续运行，输入 `q` 退出。提交代码前应删除不再需要的 `breakpoint()` 和临时输出。

## 数据分析中的常见对象

数学中，标量是单个数；向量是一维有序数据；矩阵是二维表格数据。在 Python 数据分析中，常用 NumPy 和 pandas 表示它们。

```python
import numpy as np
import pandas as pd

vector = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
table = pd.DataFrame(
    {"name": ["Alice", "Bob"], "score": [90, 85]}
)

print(vector.shape)  # (3,)
print(matrix.shape)  # (2, 2)
print(table["score"].mean())
```

`numpy.ndarray` 擅长高效的数值数组运算；`pandas.DataFrame` 适合带列名、可能包含不同类型数据的二维表格。使用前分别安装：`python -m pip install numpy pandas`。
