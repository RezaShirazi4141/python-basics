#برای ایجاد فانکشن از (دف)
def door(first_name , last_name):
    print(f"hi {first_name , last_name}")
door("reza", "shirazi")

def get_greeting(first_name):
    return f"hi {first_name}"
#کاربرد کلیدی کلمه بالا برای بازگشت به نتایج یا مقادیری که تابع تولید کرده است 
message = get_greeting("neon")
print(message)
#ارگومان دیفالت ها
def howmuch(number , by=2 , how=3):
    return number + by + how
print(howmuch(19,3))

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total
print(multiply(2,4,6))

def first_name(name):
    if name == 'reza':
        return ("hello reza")
    else:
        return f"hi {name}"
while True:
    name = input("what is your name? ").lower()
    if name == "exit":
        print("bye 👌")
        break
    else:
        print(first_name(name))


# مثلث سمت چپ برنامه
# برای دباگ کردن کد ها است

teacher = [[0,3],[4,6]]
student = ["ali","reza","mamad","taha"]
print(student) #در اینجا لیست را فقط چاپ میکنه
print(student[1])
#میتوان از طریق بالا به عناصر لیست دست یافت
print(teacher + student)
#جمع دو لیست باهم و رعایت تقدم
number = list(range(20))
print(number)
#میتوان از روش بالا هر بازه عددی را بدست اورد
number_1 = list("reza")
print(number_1)
#میتوان از طریق لیست کلمه را بخش بخش کرد
number_2 =["a","b","c","d"]
number_2[1] = 3
print(number_2)
#میتوان در لیست چیزی حذف و جای ان چیزی قرار داد
print(number[::2])#به صورت دو تا دو تا پیمایش میکنه
print(number[::-1])#از صفر تا بیست رو برعکس اجرا میکنه
for i in student:
    print(i)#برای جدا کردن اجزای داخل لیست
for i in enumerate(student):
    print(i)#هرکدام از اجزای لیست دارای چه شماره ای
for i in enumerate (student):
    print(i[0])#شماره یه اجزای داخل لیست
for i in enumerate (student):
    print(i[1])#خود اجزای داخل لیست
for i in enumerate (student):
    print(i[0],i[1])#مخلوط دو کد بالا
student.append("a")
print(student)#حرف مورد نظر را اخر لیست قرار میده
student.insert(0,"a")
print(student)#حرف مورد نظر را در هر جایی از لیست میتوان قرار داد
number_2.pop(1)#جایگاه هر عددی داخل کلوشه باشد حذف 
print(number_2)
if "a" in number_2:
    number_2.remove("a")
    print(number_2)#به شرطی که داخل لیست باشد ان را حذف
del number_2 [1]
print(number_2)#روش دیگر حذف در لیست
number_2.clear()
print(number_2)#تمام لیست رو حذف میکنه

number_3 = [2,21,1,3,3.9,43,4,34]
number_3.sort()
print(number_3)
#اعداد لیست رو به ترتیب مرتب میکنه
number_3.sort(reverse=True)
print(number_3)
#اعداد را برعکس مرتب میکنه 

item = [#یه لیست داریم که دارای چند تاپل
    ("book1",12),
    ("book2",10),
    ("book3",14)
]#برای مرتب کردن ان باید یک فانکشن ایجاد کرد
def sort_item(item):
    return item[1]#عددی که داخل اینجا قرار گیرد بر اساس ان مرتب میشود لیست 
item.sort(key=sort_item)
print(item)

item = [
    ("pen1",12),
    ("pen2",18),
    ("pen3",13)
]
#میتوان با کلمه کلیدی لامبدا کد دستوری بالا را به صورت خلاصه تر نوشت
item.sort(key=lambda item:item[1])
print(item)
#یک روش ساده برای تعریف تابع در پایتون => lambda
item = [
    ("door1",21),
    ("door2",23),
    ("door3",19),
    ("door4",25)
]
item1 = []
#با جایگذاری هر عدد داخل لیست حلقه ابتدا ان را در لیست بالا پیدا و
#سپس ان را به تعداد اجزای لیست اجرا میکنه
for i in item:
    item1.append(item[1])
print(item1)

item = [
    ("door1",21),
    ("door2",23),
    ("door3",19),
    ("door4",25)
]
item1 = []
#با تغیر در حلقه اجزای داخل ستون 1 را جدا اجرا میکند
for item in item:
    item1.append(item[1])
print(item1)

item = [
    ("home1",13),
    ("home2",21),
    ("home3",11)
]
#ستون داخل عدد لیست ایکس را جدا میکنه
x = map(lambda item: item[1] , item)
for item in x:
    print(item)
#در پایتون به عنوان یک ابزار سریع و کار امد امکان اعمال یک تابع بر روی تمام اعضای 
#یک مجموعه داده بدون نوشتن حلقه های طولانی اجرا کرد =>map
item = [
    ("home1",13),
    ("home2",21),
    ("home3",11)
]
#ستون داخل عدد لیست پایین را چدا و در یک ردیف اجرا میکنه
x = list(map(lambda item: item[1] , item))
print(x)

item = [
    ("home1",13),
    ("home2",21),
    ("home3",26)
]
#با کلمه فیتتر میتوان اجزای مورد نظر جدا واجرا کرد
x = filter(lambda item:item[1] >=20 , item)
for item in x:
    print(item)
# یک شئ ارایه مثل لیست و... میگیرد واعضای ان را بر اساس یکتابع دیگر فیلتر میکند => filter
item = [
    ("home1",13),
    ("home2",21),
    ("home3",26)
]
x = list(filter(lambda item:item[1] >=20 , item))
print(x)


item = [
    ("bag1",15),
    ("bag2",23),
    ("bag3",18),
    ("bag4",28)
]
# x = list(map(lambda item: item[1],item))
x =[item[1] for item in item]
print(x)

# y = list(filter(lambda item: item[1] >= 20,item))
y = [item for item in item if item[1] >=20]
print(y)
# میتوان با expression خلاصه کد های بالا را به شکل پایین نوشت
#به ترکیبی از مقادیر.متغیرها . عملگر ها . و توابعی گفته میشود
# یه پس از ارزیابی به یک مقدار منجر میشود => expression
list1 = [1,2,3]
list2 = [10,20,30]
print(list(zip(list1,list2)))
#با کمک کلمه زیپ میتوان دو لیست را به شکل تاپل دراورد
list1 = [1,2,3]
list2 = [10,20,30]
print(list(zip(list1,list2,"abc")))
#یک شئ از زیپ که ارایه ای تااپل ها است که در خروجی بر میگرداند => zip
#استک => stack
#LIFO => last in first out
safhe = []
safhe.append(1)
safhe.append(2)
safhe.append(3)
#در اینجا ما به صفحه های جلو تر میریم
safhe.pop()
safhe.pop()
safhe.pop()
#در اینجا ما به صفحه های قبل برمیگردیم
if safhe == []:
    print("go out")
print(safhe)

#صف => queue
#FIFO => first in first out
from collections import deque
#import,from,as سه دستور اصلی برای افزودن ماژول ها در پایتون
deque = deque([])
deque.append(1)
deque.append(2)
deque.append(3)
#در اینجا ما به صغحه های جلوتر میریم 
deque.popleft()
deque.popleft()
deque.popleft()
# در اینجا صفحه های اولی هی حذف میشوند
if not deque:#در صورت خالی بودن
    print("go out")

print(deque)


# تاپل ها

x = (2,5)
y = 2,3
z = 2,
# سه روش بالا نوعی تاپل هستند
print(type(z))
print(type(x))
print(type(y))

x = (2,3)*3
print(x)#ضرب تاپل در n
y = (2,3) + (3,2)
print(y)#جمع دو تاپل باهم
z = [2,3]#تبدیل دیکشنری به تاپل
print(tuple(z))
print (tuple("reza"))
#تبدیل استرینگ به تاپل
w = (1,2,3,)
x,y,z = w
print(x,y,z)

x = 20
y = 10
#تغیر جواب متغیر با هم
#روش اول 
z = x
x = y
y = z
#روش دوم
x,y = y,x
#روش سوم
x,y =(10,20)
print(x,y)
#ارایه ها 
from array import array
x = array("i",[1,2,3])
print(type(x))
#میتوان از دستور هایی که در لیست بود در ارایه استفاده کرد

x = [3,1,4,9]
y = set(x)
y.add(8)
y.add(4)
y.remove(3)
print(y)
#علامت مجموعه => {}
z = {7,6,5,4}
print(y | z)
#مجموع دو مجموعه را میگیرد
print(y & z)
#اشتراک دو مجموعه
print(y - z)
print(z - y)
#مجموعه اول را از مجموعه دوم کم میکنه
x = {1,3,5,6}
y = {2,4,6,8}
print(x^y)
#همه اعداد دو مجموعه غقط غیر از عدد تکرار
