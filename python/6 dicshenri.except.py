w= dict(a=10,b=11)
print(w)
#به شکل دیکشنری در میاره => dict
y = {"x" : 10,"y":11 }
print(y["x"])
y["x"] = 15 #مقدار ایکس را تغیر میده 
print(y)
y["z"] = 20 #یک کلید به اسم زد به دیکشنری اضافه میکنه
print(y)
if "x" in y :
    print(y["x"])
print(y.get("x"))#مقدار ایکس را نشان میدهد در صورت وجود
print(y.get("i"))#مقدار ای را نشان میدهد در صورت وجود
#در غیر اینصورت مقدار => none
print(y.get("x" , 5))
print(y.get("i" , 5))
#در صورت داشتن مقدار داخل کوتیشن ان را اجرا و در غیر این صورت مقدار جلو را اجرا
del y ["z"]
print(y)#از دل برای حذف در مجموعه 
#1
for i in y :
    print(i)#متقیر هارا به ما میدهد
#2    
for i in y :
    print(y[i])#مقدار متغیر ها را میدهد
#3  
for i in y :
    print(i,y[i])#مقدار متغیر و خود متغیر
#به 3 روش بالا میتوان مجموعه را پیمایش کرد

for i in y.items() :
    print(i)
#مجموعه را به صورت تاپل ایجاد کرد

for a,b in y.items() :
    print(a,b)
#این کد همانند روش 3 بالا است

#کد زیر مضرب عدد مورد نظر مثل 2 را میدهد
x = []
for i in range(5):
    x.append(i*2)
print(x)

#کد پایین کوچک شده بالایی
x = [i*2 for i in range(3)]
print(x)

#تبدیل کد بالا به یک دیکشنری
x = {i:i*2 for i in range(3)}
print(x)

#generator 6.00
x = (i*2 for i in range(5))
print(x)
#نشان میدهد که یک کولد است =><generator object <genexpr> at 0x0000012551D3A4D0>
#برای دریافت مقادیر از حلقه فور استفاده کرد
x = (i*2 for i in range(5))
for i in x :
    print(i)
    
from sys import getsizeof#مقدار جایی که کد زیر در رم میگیره
x = (i*2 for i in range(1000))#اینجا به شکل تاپل => ()
print("generator" , getsizeof(x))
#در این کد هرچه مقدار بالا بره سایز فال تغیر نمیکنه
from sys import getsizeof
x = [i*2 for i in range(1000)]#اینجا به شکل => []
print("generator" , getsizeof(x))
#با افزایش مقدار حجم داده نیز افزایش پیدا میکند

#unpacking operator 6.06
x = [1,2,3,"reza"]
print(*x)
#محتوای لیست رو برای ما خالی میکنه 
x = [1,2,3]
y = [4,6,7]
z = [*x,5,*y,"reza",*"reza"]
print(z)
#برای اجرای دستور بالا در لیست ها باید از 2 ضربدر استفاده کرد
x = {"x" : 7}
y = {"x" : 10 , "y" :15}
z = {**x,**y}
print(z)
#در دیکشنری ها اعداد تکراری قرار نمیگیرد و اخرین مقدار استفاده میشود


#استثنا6.16
#هندل کردن استثنا ها 6.20

try:
    age = int(input("age :"))
    
except:#ValueError
    print(" danger ")
    
print("good age ")



try:
    age = int(input("age :"))
    
except:
    print(" danger ")
else:
    print("no except")
    
print("good age ")


try:
    age = int(input("age :"))
    
except ValueError as ex :
    print(ex)
    # print(type(ex))
    print(" danger ")
else:
    print("no except")
    
print("good age ")


#هندل کردن استثنا ها
try:
    age = int(input("age :"))
    x = 10/age
except ValueError:
    print("danger (int)")
except ZeroDivisionError:
    print("not age = 0")
else:
    print("no except")


# try:
#     file = open("reza.txt")
#     age = int(input("age : "))
#     x = 10/age
# except (ValueError,ZeroDivisionError):
#     print("dfsfsfsdfs")
# else:
#     print("no prablem")
# finally:
#     file.close()

#پرتاب استثنا6.38

def student(age):
    if age <= 0 :
        raise ValueError ("not age = 0  ")
    return 10/age
try:
    x = int(input("age : "))
    print(student(x))
except ValueError as ex:
    print(ex)
    
    
    
