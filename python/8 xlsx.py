from openpyxl import Workbook
wb = Workbook()#داریم اکسل را فراخوانی میکنیم
sheet = wb.active#با کد اکتیو میتوان از ان استفاده کرد
sheet["A1"] = "reza"
sheet["B1"] = "shirazi"
sheet["A2"] = "ali"
sheet["B2"] = "shirazi"
sheet["C1"] = "❤"
#هر حروف بزرگ انگیلیسی نشانه یک ستون
#هر عدد جلوی ان نشان ردیف در اکسل است
wb.save("test.xlsx")



from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet.append(["Name", "lastname","age"])#با این کار همشیه این خط اول در اکسل است

while True:
    first_name = input("Enter first name: ")
    if first_name == 'exit':
        break
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    sheet.append([first_name, last_name, age])
wb.save("test.xlsx")



from openpyxl import Workbook,load_workbook
wb = load_workbook("test.xlsx")
sheet = wb.active#هرچیزی که وارد کنیم در ان ذخیره میشود
# sheet.append(["Name", "lastname","age"])
#کد دستوری بالا را غیر فعال کرده تا هر سری نخواهد اجرا شود 
while True:
    first_name = input("Enter first name: ")
    if first_name == 'exit':
        break
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    sheet.append([first_name, last_name, age])
wb.save("test.xlsx")



from openpyxl import Workbook, load_workbook
try:#بدون باگ بودن کد
    wb = load_workbook('test.xlsx')
except:#در صورت داشتن باگ
    wb = Workbook()
    
sheet = wb.active
sheet.append(["name","last_name",])
wb.save('test.xlsx')



from openpyxl import Workbook, load_workbook
try:
    wb = load_workbook('test.xlsx')
    sheet = wb.active
except:
    wb = Workbook()
    sheet = wb.active
    sheet.append(["name","last_name",])

while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    last_name = input("Enter your last name: ")
    sheet.append([name,last_name,])
wb.save('test.xlsx')



from openpyxl import Workbook, load_workbook
try:
    wb = load_workbook('test.xlsx')
    sheet = wb.active
except:
    wb = Workbook()
    sheet = wb.active
    sheet.append(["name","last_name",])

while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    last_name = input("Enter your last name: ")
    sheet.append([name,last_name,])
wb.save('test.xlsx')
#برای ایتره کردن روی ردیف‌های یک دیتافریم استفاده می‌شوداین تابع یک ژنراتور برمی‌گردد 
#  iter_rows => دکه در هر مرحله یک تاپل شامل شماره ردیف و مقادیر مربوط به آن ردیف را برمی‌گرداند
for i in sheet.iter_rows(min_row=2, max_col=2,values_only=True):
    print(i)
#شروع سطر =>min_row 
#پایان سطر =>max_row
#شروع ستون =>min_col 
#پایان ستون =>max_col
#فقط مقدار =>valuse_only    
    
    
    
from openpyxl import Workbook, load_workbook
try:
    wb = load_workbook('test.xlsx')
    sheet = wb.active
except:
    wb = Workbook()
    sheet = wb.active
    sheet.append(["name","last_name",])

while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    last_name = input("Enter your last name: ")
    sheet.append([name,last_name,])
wb.save('test.xlsx')

for i in sheet.iter_rows(min_row=2, max_col=2,values_only=True):
    name,last_name = i
    print(name)
    print(last_name)
#مقادیر را به صورت تاپل میده و به شکل جدا
    
    
       
from openpyxl import Workbook, load_workbook
try:
    wb = load_workbook('test.xlsx')
    sheet = wb.active
except:
    wb = Workbook()
    sheet = wb.active

    sheet.append(["name","last_name",])

while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    last_name = input("Enter your last name: ")
    sheet.append([name,last_name,])
wb.save('test.xlsx')

for i in sheet.iter_rows(min_row=2, max_col=2,values_only=True):
    name,last_name = i
    
    if name == "ali":
        print(f"{last_name} is Ali")
#اینجا فقط مشخصات علی رو به ما میده        



from openpyxl import Workbook, load_workbook
try:
    wb = load_workbook('test.xlsx')
    sheet = wb.active
except:
    wb = Workbook()
    sheet = wb.active
    sheet.append(["name","last_name","age","name_father"])

while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    name_father = input("Enter your father name: ")
    sheet.append([name,last_name,age,name_father])
wb.save('test.xlsx')

name_again = input("Enter another name: ")
#اگر مشخصات یک فرد را از ما بخواد کاربر
for i in sheet.iter_rows(min_row=2, max_col=4,values_only=True):
    name, last_name, age, name_father = i
    
    if name == name_again:
        #break
        #با قرار دادن بریک درصورت داشتن مشخصات دیگه اونا اجرا نمیکنه
        print(f"name : {name}, last name : {last_name}, age : {age}, name_father : {name_father}")
