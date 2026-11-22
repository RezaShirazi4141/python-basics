# انواع حلقه ها 
# for => محدود
#به ازای هر 
# while => نامحدود 
#تا زمانی که 

for hello in range(5):
    print("hello")# در این کد به دلیل کتیشن اون را 5 بار چاپ

for hello in range(2):
    print(hello)#در این کد به تعداد عدد داخل پرانتز از صفر شروع 

for hello in range(1,20,2):
    print(hello)
 #عدد اول عدد شروع عدد دوم عدد پایان عدد سوم عدد پیمایش          

masege =False#در صورت ارسال فقط یکبار اجرا میشه در غیر این صورت 3 بار
for apple in range(3):
    print('i lave you')
    if masege:
        print("you good")
        break#به معنای پایان دستورات هست  
else:
    print("ass kisser")

for i in range(3):
    #حلقه ی ایجاد شده به تعداد خواسته ما بازی رااجرا میکند
    player_1 = int(input("youser (1,2,3) :"))
    if player_1 == 1:
        print("you win")
    elif player_1 == 2:
        print("do agene...")
    elif player_1 == 3:
        print("danger")
    else:#قرار گیری شرط ها باید بعد از حلقه فور باشد
        print("1,2,3")

for x in range(3):
    for y in range(2):
        print(f'({x} , {y})')
#میتوان با دو حلقه فور مختصات تشکیل داد 

for i in "python":
    print(i)
#حروف را جدا و هر کدام را در یک لاین قرار میدهد

number = 200
while number >0:#حلقه وایل یک حلقه بی پایان و وقتی به دستور روبه رو برسه پایان 
    print(number)
    number //= 2
print("the end")

number = ""# یک حلقه بی پایان که فقط با اکسیت خارج میشود
while number !="exit":
    number = input(">>>")
    print(number)
    
x = int (input(" start number :"))
y = int (input("ende number :"))
z = int (input("stop number :"))

while x <= y:
    print(x)
    x += z

#یک حلقه بی پایان تشکیل شده
while True:
    name = input("your name :")
    
    if name == "exit":
        print("good bay 👌")
        break #بریک برای اینکه در صورت خروج دیگر وارد نشود
    else:
        print(f"your name is {name}")