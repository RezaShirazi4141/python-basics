x = input(":")#اینپوت برای درخواست از کاربر و جواب به صورت اس تی ار
y = x + x
print(y)
#چون به شکل اس تی ار عدد گرفته شده بغل هم اجرا میکنه 

x = int(input(" x :"))#اینجا به شکل اینت ریجر تبدیل کرده
y = x + x
print(y)
#سپس جوتب را طبق دستور انجام داده

x = input(" x : ")
y = int(x) + 9
print(f"x : {x} , y :{y}")

first_name1 = input("you first_name :")
last_name1 = input("you last_name :")
print(f"hi {first_name1} {last_name1}")

home = int(input("number home :"))
if home >=35:# کلمه ایف برای ایجاد شرط اجرا میشود
    print("big mal")
elif home > 25:# کلمه ایلایف برای ایجاد شرط های بعدی 
    print("small mal")
else:# کلمه الس برای پایان شروط
    print("faghir")
    
# if =>اگر 
# elif => در غیر این صورت /اگر
# else =>در غیر اینصورت 

water =int (input())
print("reza" if water >25 else "ali")
#میتوان شرط ها را به صورت خلاصه بالا نوشت

age = int(input("x :"))
if age>18 and 20 >age:
    print("open")

username =input("enter your username :" )
pssword = input("enter your password :")

if username == "admin": # دو مساوی به معنای برار بودن
    print("True username")
    if pssword == "a123":
        print("True pssword")
    else:
        print("False password")
else:
     print("False username")
#در کد بالا به خاطر دو درخواستی بودن از دو ایف در پشت هم استفاده کرده

username =input("enter your username :" )
pssword = input("enter your password :")

if username == "admin" and pssword == "a123":
    print("True")
else:
    print("False")
#در این کد اگر اشتباه هر کدام را بزنیم جواب غلط میده
#ولی اشکال از کدام جواب را به ما نمیده

mather = input("mather => False and True :")     
father = input("father => False and True :")     
sister = input("sister => False and True :")     
brather = input("brather => False and True :")
     
if mather and (father or brather):
    print("parents god")
elif not father and (sister or mather):
    print("parents bad")
    

number_friend =int(input("you how much friend :"))
if number_friend >20 and number_friend <30:
    print("you ejtemaii")

#data type
     
# int => شامل تمام اعداد صحیح 
# str => به شکل متن یا رشته 
# float => شامل تمام اعداد اعشاری
# bool => جواب درست و غلط
#complex =>

