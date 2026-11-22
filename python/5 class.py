class username:#بستری را فراهم میکند تا داده ها و توابع در کنار یکدیگر باشند
    def on(self, button):#به عنوان یک ارجاع به شی جاری درداخل متد های کلاس عمل میکنه
        self.btn = button# دکمه
        
    def off(self):
        return self.btn
    
x = username()
x.on("on")
print(x.off())



class username:
    def __init__(self,username , lastname , age):#صفات و متغیر های اشیا را مقداردهی کرد
        self.username = username
        self.lastname = lastname
        self.age = age

    def firstname(self):
        return f"{self.username} is {self.lastname} is {self.age}"

x = username("reza","shirazi","20")
print(x.firstname())




class student:
    def __init__(self,name,lastname,age,nomre):
        self.name_1 = name
        self.lastname_1 = lastname
        self.age_1 = age
        self.nomre_1 = nomre
    def username(self):
        return f"""
    name     = {self.name_1}
    lastname = {self.lastname_1}
    age      = {self.age_1}
    nomre    = {self.nomre_1}"""
while True:   
    name = input("what is your name ? ").lower()
    if name == "exit":
        break
    lastname = input("what is your lastname ? ").lower()
    if lastname == "exit":
        break
    age = input("how do you old ? ").lower()
    if age == "exit":
        break
    nomre = input("how do you nomre ? ").lower()
    if nomre == "exit":
        break
    x =student(name,lastname,age,nomre)
    print(x.username())
    
    
    

class username:
    def __init__(self,username , lastname , age):
        self.username = username
        self.lastname = lastname
        self.age = age

    def firstname(self):
        return f"{self.username} is {self.lastname} is {self.age}"
    def __str__(self):
        return f"{self.username} , {self.lastname} , {self.age}"

username_1 = input("Enter your username : ")
lastname_1 = input("Enter your lastname : ")
age_1 = int(input("Enter your age : "))
x = username(username_1 , lastname_1 , age_1)
print(x)




class username:
    def __init__(self,username , lastname , age):
        self.username = username
        self.lastname = lastname
        self.age = age

    def firstname(self):
        return f"{self.username} is {self.lastname} is {self.age}"

username_1 = input("Enter your username : ")
lastname_1 = input("Enter your lastname : ")
age_1 = int(input("Enter your age : "))
x = username(username_1 , lastname_1 , age_1)
print(x.firstname)




class username:
    def __init__(self,username , lastname , age):
        self.username = username
        self.lastname = lastname
        self.age = age

    def firstname(self):
        return f"{self.username} is {self.lastname} is {self.age}"
    def __str__(self):
        return f"{self.username} , {self.lastname} , {self.age}"
while True  :
    username_1 = input("Enter your username : ")
    if username_1 =="exit" :
        break
    lastname_1 = input("Enter your lastname : ")
    age_1 = int(input("Enter your age : "))
    x = username(username_1 , lastname_1 , age_1)
    print(x)
    
    
    
    
class username:
    def __init__(self,username , lastname , age):
        self.username = username
        self.lastname = lastname
        self.age = age
        if age_1 >18 :
            print("Your big")
        else:
            print("you small")
    def firstname(self):
        return f"{self.username} is {self.lastname} is {self.age}"
    def __str__(self):
        return f"{self.username} , {self.lastname} , {self.age}"
while True  :
    username_1 = input("Enter your username : ")
    if username_1 =="exit" :
        break
    lastname_1 = input("Enter your lastname : ")
    age_1 = int(input("Enter your age : "))
    # if age_1 >18 :
    #     print("Your big")
    # else:
    #     break
    print(username(username_1 , lastname_1 , age_1))




class car:
    def __init__(self,type_car ,close_car , sorat_car):
        self.type = type_car
        self.close = close_car
        self.sorat = sorat_car
        if sorat_1 > 180:
            print("por sorat")
        else:
            print("kam sorat")
    def firstname(self):
        return f"{self.type} is {self.close} is {self.sorat}"
    def __str__(self):
        return f"{self.type} , {self.close} , {self.sorat}"
while True:
    have_car = input("what do you have a car?")
    if have_car == "yes":
        type_1 = input("type your car? ")
        if type_1 == "exit":
            break
        close_1 = input("close your car? ")
        sorat_1 = int(input("sorat your car? "))

        print(car(type_1 , close_1, sorat_1))
    else:
        print("bye👌")
        break
    
    
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def student_list(self):
        return f" {self.name} and {self.age}"

class teacher(student):
    pass
name1 = teacher("nima", 18)
print(name1.student_list())
#به عنوان محل نگهداری برای پیاده سازی اتی توابع و حلقه ها ودیگر موارد => pass



class student:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def student_list(self):
        return f" {self.name} and {self.age}"

class teacher(student):
    def __init__(self,name,lastname,age,nomre):
        super().__init__(name,lastname)
        self.age = age
        self.nomre = nomre
# در پایتون برای فراخوانی متد ها از کلاس استفاده میشود => super
    def student_list1(self):
        return f"""
name :{self.name} 
lastname: {self.lastname}
age :{self.age}
nomre:{self.nomre}"""

x = teacher("reza","shirazi","20","18")
print(x.student_list1())



class student:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def student_list(self):
        return f" {self.name} and {self.age}"

class teacher1:
    def __init__(self,name_father):
        self.name_father = name_father


class teacher(student, teacher1):
    def __init__(self,name,lastname,age,nomre,name_father):
        student.__init__(self,name,lastname)
        teacher1.__init__(self,name_father)
    
        self.age = age
        self.nomre = nomre

    def student_list1(self):
        return f"""
name :{self.name} 
lastname: {self.lastname}
age :{self.age}
nomre:{self.nomre}
name_father:{self.name_father}"""

x = teacher("reza","shirazi","20","18","mehdi")
print(x.student_list1())


class student:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def student_list(self):
        return f" {self.name} and {self.age}"

class teacher1:
    def __init__(self,name_father):
        self.name_father = name_father


class teacher(student, teacher1):
    def __init__(self,name,lastname,age,nomre,name_father):
        student.__init__(self,name,lastname)
        teacher1.__init__(self,name_father)

        self.age = age
        self.nomre = nomre

    def student_list1(self):
        return f"""
name : {self.name} 
lastname : {self.lastname}
age : {self.age}
nomre : {self.nomre}
name_father : {self.name_father}"""

while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    lastname = input("Enter your last name: ")
    age = input("Enter your age: ")
    nomre = input("Enter your nomre: ")
    name_father = input("Enter your name father: ")

    x = teacher(name,lastname,age,nomre,name_father)
    print(x.student_list1())
    
#پلی مورفیس => بلد نیستم

class car:
    def __init__(self,model):
        self.model1 = model

    def car_list(self):
        return f" {self.model1}"

class car1:
    def __init__(self,sorat):
        self.sorat1 = sorat
        if sorat >= 150:
            print("You are sorat")


class teacher(car,car1):
    def __init__(self,model,rang,sorat):
        car.__init__(self,model)
        car1.__init__(self,sorat)
        self.rang1 = rang
    def car_list1(self):
        return f"""
model : {self.model1} 
rang : {self.rang1}
sorat : {self.sorat1}"""

while True:
    model = input("Enter your model: ")
    if model == "exit":
        break
    range = input("Enter your rang: ")
    sorat = int(input("Enter your sorat: "))
    
#ماژول 9.00
#میتوان از بقیه فانکشن های داخل فایل های دیگه استفاده کرد به عنوان مثال
#from def_list import door
#از این طریق از فانکشن دوور از فایل دف لیست در اینجا استفاده کردیم
#زمانی که از کد بالا استفاده میکنیم یک فایل با نام پای کش برای ما ایجاد میکنه
#پکیج مجموعه ای از ماژول ها است