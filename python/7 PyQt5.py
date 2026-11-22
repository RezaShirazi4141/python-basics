from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("reza")

text1 = QLabel("بسم تعالی       ",window)
text1.move(125,100)#عدد اول فاصله چپ  عدد دوم فاصله از بالا
btn1 = QPushButton("کلاس های درسی",window)# ساخت دکمه کلیک
btn1.move(90,125)

def klick():
    # print("وارد کلاس شد")# اگر از پرینت استفاده بشه متن مورد نظر دداخل وی اس کد چاپ میکنه
    text1.setText("وارد کلاس شد ")#زمانی که روی کلید مورد نظر کلیک میشود متن داخل دابل کوتیشن در جای مورد نظر ایجاد 
    btn1.setDisabled(True)
btn1.clicked.connect(klick)#دکمه مورد نظر 

window.setGeometry(500,300,300,400)#اندازه صفحه اصلی
#عدد اول برای فاصله پنجره از گوشه چپ
#عدد دوم برای فاصله پنجره از بالا
#عدد سوم برای عرض صفحه
#عدد چهارم برای طول صفحه

window.show()
sys.exit(app.exec_())



from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello World")

layout = QVBoxLayout(window)#بر اساس اندازه صفحه تنظیم میکنه و دیگر نیاز به اندازه دادن نیست

text1 = QLabel("بسم تعالی")
# text1.move(50,50)
btn1 = QPushButton("ok")
# btn1.move(5,250)
# window.setGeometry(500,300,300,400)
text2 = QLabel("name",)
# text2.move(5,130)
text3 =QLabel("lastname",)
# text3.move(5,190)
line1 = QLineEdit()
# line1.move(5,160)
line2 = QLineEdit()
# line2.move(5,210)

layout.addWidget(text1)
layout.addWidget(text2)
layout.addWidget(line1)
layout.addWidget(text3)
layout.addWidget(line2)
layout.addWidget(btn1)
#ترتیب قرار گیری مهم است زیرا بر اساس ان قرار میگیرند

def clicked():
    btn1.setText("تایید شد")
    btn1.setDisabled(True)
btn1.clicked.connect(clicked)
def clicked2():
    new_text = line1.text()
    new_text1 = line2.text()
    print(new_text,new_text1)
btn1.clicked.connect(clicked2)

window.setLayout(layout)#برای ایجاد لیوت واجب است

window.show()
sys.exit(app.exec_())




#_____فراخوانی کتابخانه PyQt5 _____
from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)#ساخت صفحه در ویندوز
window = QWidget()#ساخت صفحه در pyqt5
window.setWindowTitle("کتاب فروشی")#اسم صفحه اصلی
layout = QVBoxLayout(window)

#_____ایجاد صفحه های فرعی _____
name_Layout = QHBoxLayout()
price_Layout = QHBoxLayout()
input_Layout = QVBoxLayout()
btn_Layout = QHBoxLayout()
show_book_layout = QVBoxLayout()
show_price_layout = QVBoxLayout()
lastname_Layout = QHBoxLayout()

#_____ایجاد اسم های کتاب _____
text1 = QLabel("book1")
text2 = QLabel("book2")
text3 = QLabel("book3")
#_____ریختن اسم کتاب ها داخل صفحه فرعی _____
name_Layout.addWidget(text1)
name_Layout.addWidget(text2)
name_Layout.addWidget(text3)

#_____نوشتن قیمت کتاب ها _____
price1 = QLabel("100$")
price2 = QLabel("100$")
price3 = QLabel("100$")
#_____ریختن قیمت کتاب ها داخل صفحه فرعی _____
price_Layout.addWidget(price1)
price_Layout.addWidget(price2)
price_Layout.addWidget(price3)

#_____ایجاد فضای نوشته برای کاربر _____
text4 = QLabel("کتاب مورد نظر را انتخاب کنید :")
line1 = QLineEdit()
line1.setPlaceholderText("مثلا book1")
#_____ریختن فضای نوشته داخل صفحه فرعی _____
input_Layout.addWidget(text4)
input_Layout.addWidget(line1)

#_____ایجاد دکمه های انتخابی _____
btn1 =QRadioButton("پرداخت نقدی")
btn2 = QRadioButton("پرداخت قسطی")
#_____ریختن دکمه ها داخل صفحه فرعی _____
btn_Layout.addWidget(btn1)
btn_Layout.addWidget(btn2)

#_____ساخت دکمه ثبت _____
btn3 = QPushButton("نمایش")
btn4 = QPushButton("ثبت اطلاعات")

#_____ایجاد نمایش کتاب های انتخاب شده _____
text5 = QLabel("کتاب های انتخاب شده :")
text6 = QLabel("                        ")
#_____ریختن نمایش کتاب ها داخل صفحه فرعی _____
show_book_layout.addWidget(text5)
show_book_layout.addWidget(text6)

#_____ایجاد نمایش قیمت کل کتاب ها _____
text7 = QLabel("قیمت کل کتاب های انتخاب شده :")
text8 = QLabel("                        ")
#_____ریختن قیمت کل داخل صفحه فرعی_____
show_price_layout.addWidget(text7)
show_price_layout.addWidget(text8)

#_____ایجاد جایگاهی برای ثبت نام _____
line2 = QLineEdit("")
line2.setPlaceholderText("name :")
line3 = QLineEdit("")
line3.setPlaceholderText("last name :")
#_____ریختن جایگاه ثبت نام در صفحه فرعی_____
lastname_Layout.addWidget(line2)
lastname_Layout.addWidget(line3)

#_____جایگاه اطلاعات ثبت نامی _____
text9 = QLabel("                        ")
text10 = QLabel("                       ")

#_____قرار دادن صفحه های فرعی به ترتیب _____
layout.addLayout(name_Layout)
layout.addLayout(price_Layout)
layout.addLayout(input_Layout)
layout.addLayout(btn_Layout)
layout.addWidget(btn3)
layout.addLayout(show_book_layout)
layout.addLayout(show_price_layout)
layout.addLayout(lastname_Layout)
layout.addWidget(btn4)
layout.addWidget(text9)
layout.addWidget(text10)

#_____ایجاد حالت تغیر برای دکمه ثبت اطلاعات_____
def click():
    btn4.setText("اطلاعات با موفیقت ثبت گردید")
    btn4.setEnabled(True)

#_____ثبت اطلاعات در پاین صفحه _____
def click1():
    x = line2.text()
    y = line3.text()
    text9.setText(f"{x} {y}")
    btn4.setEnabled(True)

#_____ایجاد قوانینی برای سایت _____
my_list = []
list_book = ["book1", "book2", "book3"]
def click2():
    new_text = line1.text()
    if new_text :
        if new_text in list_book:
            if new_text in my_list:
                QMessageBox.warning(window,"Error","تکراری!")
            else:
                my_list.append(new_text)
                text6.setText(str(my_list))
        else:
            QMessageBox.warning(window,"Error","کتابی به این اسم وجود ندارد!")
    else:
        QMessageBox.warning(window,"Error","یک مقداری وارد کنید .")

#_____ایجاد شرایط پرداخت_____
def click3():
    text10.setText("پرداخت نقدی")
def click4():
    text10.setText("پرداخت قسطی")

#_____وصل کردن دکمه به فانکشن مورد نظر_____
btn1.clicked.connect(click3)
btn2.clicked.connect(click4)
btn3.clicked.connect(click2)
btn4.clicked.connect(click)
btn4.clicked.connect(click1)

window.setLayout(layout)
window.show()#نمایش صفحه
sys.exit(app.exec_())#برای بستن صفحه برای کاربر




from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("سلام و درود")
layout = QVBoxLayout()

name_layout = QVBoxLayout()
list_layout = QHBoxLayout()
input_layout = QVBoxLayout()
time_layout = QHBoxLayout()
radio_layout = QHBoxLayout()
sho_book_layout = QVBoxLayout()
lastname_layout = QHBoxLayout()
lastname1_layout = QHBoxLayout()

text1 = QLabel("کتابخانه القدیر")
text2 = QLabel("لیست کتاب های کتابخانه :")
name_layout.addWidget(text1)
name_layout.addWidget(text2)

text3 = QLabel("book1")
text4 = QLabel("book2")
text5 = QLabel("book3")
text6 = QLabel("book4")
text7 = QLabel("book5")
list_layout.addWidget(text3)
list_layout.addWidget(text4)
list_layout.addWidget(text5)
list_layout.addWidget(text6)
list_layout.addWidget(text7)

text8 = QLabel("کتاب مورد نظر :")
line1 = QLineEdit()
line1.setPlaceholderText("مثلا book3")
input_layout.addWidget(text8)
input_layout.addWidget(line1)

text9 = QLabel("مدت زمان تحویل =>")
line2 = QLineEdit()
line2.setPlaceholderText("چند روز")
time_layout.addWidget(line2)
time_layout.addWidget(text9)

text10 = QLabel("هدف از انتخاب :")

btn = QRadioButton("افزایش اطلاعات عمومی")
btn1 = QRadioButton("برای انجام پروژه")
btn2 = QRadioButton("سایر موارد")
radio_layout.addWidget(btn2)
radio_layout.addWidget(btn1)
radio_layout.addWidget(btn)

btn4 = QPushButton("افزودن کتاب")

text12 = QLabel("کتاب های انتخاب شده :")
text13 = QLabel("                       ")
sho_book_layout.addWidget(text12)
sho_book_layout.addWidget(text13)

text11 = QLabel("مشخصات فردی :")

line3 = QLineEdit()
line3.setPlaceholderText("name :")
line4 = QLineEdit()
line4.setPlaceholderText("lastname :")
line5 = QLineEdit()
line5.setPlaceholderText("age :")
lastname_layout.addWidget(line3)
lastname_layout.addWidget(line4)
lastname_layout.addWidget(line5)

line6 = QLineEdit()
line6.setPlaceholderText("name_father :")
line7 = QLineEdit()
line7.setPlaceholderText("codemeli :")
line8 = QLineEdit()
line8.setPlaceholderText("name_mather :")
lastname1_layout.addWidget(line6)
lastname1_layout.addWidget(line7)
lastname1_layout.addWidget(line8)

btn5 = QPushButton("ثبت نام")

text14 = QLabel("""name :
lastname :
age :
name_father :
codemeli :
name_mather :""")
text15 = QLabel("                       ")

btn6 = QPushButton("خروج")

layout.addLayout(name_layout)
layout.addLayout(list_layout)
layout.addLayout(input_layout)
layout.addLayout(time_layout)
layout.addWidget(text10)
layout.addLayout(radio_layout)
layout.addWidget(btn4)
layout.addLayout(sho_book_layout)
layout.addWidget(text11)
layout.addLayout(lastname_layout)
layout.addLayout(lastname1_layout)
layout.addWidget(btn5)
layout.addWidget(text15)
layout.addWidget(text14)
layout.addWidget(btn6)

my_list = []
list_book = ["book1", "book2", "book3", "book4", "book5"]
def click():
    new_tex = line1.text()
    if new_tex:
        if new_tex in list_book:
            if new_tex in my_list:
                QMessageBox.warning(window,"Error","تکراری!")
            else:
                my_list.append(new_tex)
                text13.setText(str(my_list))
        else:
            QMessageBox.warning(window, "Error", "این اسم وجود ندارد!")
    else:
        QMessageBox.warning(window, "Error", "یک مقدار وارد کنید!")

def click1():
    new_tex1 = line2.text()
    if new_tex1:
        if int(new_tex1) > 7 :
            QMessageBox.warning(window,"Error","بیش از یک هفته مجاز نیست")
    else:
        QMessageBox.warning(window,"Error","یک مقدار وارد کنید")

def click2():
    new_tex2 = line3.text()
    new_tex3 = line4.text()
    new_tex4 = line5.text()
    new_tex5 = line6.text()
    new_tex6 = line7.text()
    new_tex7 = line8.text()
    text14.setText(f"""name : {new_tex2}
lastname : {new_tex3}
age : {new_tex4}
name_father : {new_tex5}
codemeli : {new_tex6}
name_mather : {new_tex7}""")

def click3():
    text15.setText("افزایش اطلاعات عمومی")
def click4():
    text15.setText("برای انجام پروژه")
def click5():
    text15.setText("سایر موارد")

def click6():
    btn5.setText("اطلاعات با موفقیت ثبت گردید")
def click7():
    window.close()


btn4.clicked.connect(click)
btn4.clicked.connect(click1)
btn5.clicked.connect(click2)
btn.clicked.connect(click3)
btn1.clicked.connect(click4)
btn2.clicked.connect(click5)
btn5.clicked.connect(click6)
btn6.clicked.connect(click7)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())



from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("رستوران")
layout = QVBoxLayout()

food_Layout = QHBoxLayout()
price_Layout = QHBoxLayout()
input_Layout = QHBoxLayout()
btn_Layout = QHBoxLayout()
show_price_Layout = QHBoxLayout()

text = QLabel("کباب")
text1 = QLabel("  مرغ")
text2 = QLabel("  کله پاچه")
text3 = QLabel("  قیمه")
text4 = QLabel("100")
text5 = QLabel("200")
text6 = QLabel("300")
text7 = QLabel("400")
text8 = QLabel("                       ")
text9 = QLabel("قیمت نهایی :")
text10 = QLabel("سفارش ثبت")
text11 = QLineEdit()
text11.setPlaceholderText("مثلا کباب")
btn1 = QPushButton("ثبت")
btn2 = QPushButton("حذف")
my_list = QListWidget()


food_Layout.addWidget(text)
food_Layout.addWidget(text1)
food_Layout.addWidget(text2)
food_Layout.addWidget(text3)

price_Layout.addWidget(text4)
price_Layout.addWidget(text5)
price_Layout.addWidget(text6)
price_Layout.addWidget(text7)

input_Layout.addWidget(text11)
input_Layout.addWidget(text10)

btn_Layout.addWidget(btn2)
btn_Layout.addWidget(btn1)

show_price_Layout.addWidget(text8)
show_price_Layout.addWidget(text9)

layout.addLayout(food_Layout)
layout.addLayout(price_Layout)
layout.addLayout(input_Layout)
layout.addLayout(btn_Layout)
layout.addWidget(my_list)
layout.addLayout(show_price_Layout)

def btn1_clicked():
    user_food = text11.text()
    my_list.addItem(user_food)
def btn2_clicked():
    pass
my_list1 = []
list_food = ["کباب","مرغ","کله پاچه","قیمه"]
def btn3_clicked():
    new_text = text11.text()
    if new_text :
        if new_text in list_food:
            if new_text in my_list1:
                QMessageBox.warning(window,"error","تکراری")
            else:
                my_list1.append(new_text)
                text8.setText(str(my_list1))
        else:
            QMessageBox.warning(window,"error","غذایی به این اسم وجود نداره")
    else:
        QMessageBox.warning(window,"error","یک مقداری وارد کنید")

btn1.clicked.connect(btn3_clicked)
btn1.clicked.connect(btn1_clicked)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())



from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("سفارش")
layout = QVBoxLayout()

# --------------------------
# داده‌ها
# --------------------------
food_prices = {
    "کباب": 100,
    "مرغ": 200,
    "کله پاچه": 300,
    "قیمه": 400
}

list_food = list(food_prices.keys())   # لیست غذاهای مجاز
my_list1 = []                          # لیست غذاهای انتخاب‌شده
total_price = 0                        # مجموع کل قیمت
# --------------------------

# لایه‌ها
food_layout = QHBoxLayout()
price_layout = QHBoxLayout()
input_layout = QHBoxLayout()
btn_layout = QHBoxLayout()
show_price_layout = QHBoxLayout()

# لیبل‌ها
text = QLabel("غذاها:")
text1 = QLabel("کباب")
text2 = QLabel("مرغ")
text3 = QLabel("کله پاچه")
text4 = QLabel("قیمه")

text5 = QLabel("100")
text6 = QLabel("200")
text7 = QLabel("300")
text8 = QLabel("400")

text_price_title = QLabel("قیمت نهایی:")
text_price_value = QLabel("0")

# ورودی
text11 = QLineEdit()
text11.setPlaceholderText("نام غذا را وارد کنید")

# دکمه‌ها
btn_add = QPushButton("افزودن")
btn_show = QPushButton("نمایش لیست")

# لیست گرافیکی
my_list = QListWidget()

# --------------------------
# اضافه کردن ویجت‌ها
# --------------------------

# غذاها
food_layout.addWidget(text)
food_layout.addWidget(text1)
food_layout.addWidget(text2)
food_layout.addWidget(text3)
food_layout.addWidget(text4)

price_layout.addWidget(text5)
price_layout.addWidget(text6)
price_layout.addWidget(text7)
price_layout.addWidget(text8)

input_layout.addWidget(text11)

btn_layout.addWidget(btn_show)
btn_layout.addWidget(btn_add)

show_price_layout.addWidget(text_price_title)
show_price_layout.addWidget(text_price_value)

layout.addLayout(food_layout)
layout.addLayout(price_layout)
layout.addLayout(input_layout)
layout.addLayout(btn_layout)
layout.addWidget(my_list)
layout.addLayout(show_price_layout)

# --------------------------
# توابع
# --------------------------

def btn_add_clicked():
    global total_price

    new_food = text11.text().strip()

    if not new_food:
        QMessageBox.warning(window, "خطا", "لطفاً نام غذا را وارد کنید")
        return

    if new_food not in list_food:
        QMessageBox.warning(window, "خطا", "غذایی با این نام وجود ندارد")
        return

    if new_food in my_list1:
        QMessageBox.warning(window, "خطا", "این غذا قبلاً اضافه شده")
        return

    # افزودن غذا
    my_list1.append(new_food)
    my_list.addItem(new_food)

    # افزودن به مجموع قیمت
    total_price += food_prices[new_food]
    text_price_value.setText(str(total_price))

def btn_show_clicked():
    QMessageBox.information(window, "لیست غذاها", str(my_list1))

# --------------------------
# اتصال دکمه‌ها
# --------------------------
btn_add.clicked.connect(btn_add_clicked)
btn_show.clicked.connect(btn_show_clicked)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())


from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("python")
layout = QVBoxLayout()

meno = window.menuBar()
meno.addAction("help")
meno.addAction("about")
meno.addAction("quit")

window.setLayout(layout)
window.show()
sys.exit(app.exec_())


from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("python")
layout = QVBoxLayout()

meno = window.menuBar()
file = meno.addMenu("File")
help_ = meno.addMenu("Help")

act_file = QAction("open")
act_file1 = QAction("save")
act_file2 = QAction("exit")

act_help = QAction("about")
act_help1 = QAction("help")
act_help2 = QAction("quit")

file.addAction(act_file)
file.addAction(act_file1)
file.addAction(act_file2)

help_.addAction(act_help)
help_.addAction(act_help1)
help_.addAction(act_help2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())


from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window_meno = QMainWindow()
window.setWindowTitle("سفارش")
layout = QVBoxLayout(window)

# --------------------------
# داده‌ها
# --------------------------
food_prices = {
    "کباب": 100,
    "مرغ": 200,
    "کله پاچه": 300,
    "قیمه": 400
}

list_food = list(food_prices.keys())   # لیست غذاهای مجاز
my_list1 = []                          # لیست غذاهای انتخاب‌شده
total_price = 0                        # مجموع کل قیمت
# --------------------------

# لایه‌ها
food_layout = QHBoxLayout()
price_layout = QHBoxLayout()
input_layout = QHBoxLayout()
btn_layout = QHBoxLayout()
show_price_layout = QHBoxLayout()

meno = window_meno.menuBar()
file = meno.addMenu("File")
help1 = meno.addMenu("Help")

act_file = QAction("open")
act_file1 = QAction("save")
act_file2 = QAction("exit")

act_help = QAction("about")
act_help1 = QAction("help")
act_help2 = QAction("quit")

file.addAction(act_file)
file.addAction(act_file1)
file.addAction(act_file2)

help1.addAction(act_help)
help1.addAction(act_help1)
help1.addAction(act_help2)

# لیبل‌ها
text = QLabel("غذاها:")
text1 = QLabel("کباب")
text2 = QLabel("مرغ")
text3 = QLabel("کله پاچه")
text4 = QLabel("قیمه")

text5 = QLabel("100")
text6 = QLabel("200")
text7 = QLabel("300")
text8 = QLabel("400")

text_price_title = QLabel("قیمت نهایی:")
text_price_value = QLabel("0")

# ورودی
text11 = QLineEdit()
text11.setPlaceholderText("نام غذا را وارد کنید")

# دکمه‌ها
btn_add = QPushButton("افزودن")
btn_show = QPushButton("نمایش لیست")

# لیست گرافیکی
my_list = QListWidget()

# --------------------------
# اضافه کردن ویجت‌ها
# --------------------------
# غذاها
food_layout.addWidget(text)
food_layout.addWidget(text1)
food_layout.addWidget(text2)
food_layout.addWidget(text3)
food_layout.addWidget(text4)

price_layout.addWidget(text5)
price_layout.addWidget(text6)
price_layout.addWidget(text7)
price_layout.addWidget(text8)

input_layout.addWidget(text11)

btn_layout.addWidget(btn_show)
btn_layout.addWidget(btn_add)

show_price_layout.addWidget(text_price_title)
show_price_layout.addWidget(text_price_value)

layout.addLayout(food_layout)
layout.addLayout(price_layout)
layout.addLayout(input_layout)
layout.addLayout(btn_layout)
layout.addWidget(my_list)
layout.addLayout(show_price_layout)

# --------------------------
# توابع
# --------------------------

def btn_add_clicked():
    global total_price

    new_food = text11.text().strip()

    if not new_food:
        QMessageBox.warning(window, "خطا", "لطفاً نام غذا را وارد کنید")
        return

    if new_food not in list_food:
        QMessageBox.warning(window, "خطا", "غذایی با این نام وجود ندارد")
        return

    if new_food in my_list1:
        QMessageBox.warning(window, "خطا", "این غذا قبلاً اضافه شده")
        return

    # افزودن غذا
    my_list1.append(new_food)
    my_list.addItem(new_food)

    # افزودن به مجموع قیمت
    total_price += food_prices[new_food]
    text_price_value.setText(str(total_price))

def btn_show_clicked():
    QMessageBox.information(window, "لیست غذاها", str(my_list1))

def exit_clicked():
    app.quit()


act_file2.triggered.connect(exit_clicked)
# --------------------------
# اتصال دکمه‌ها
# --------------------------
btn_add.clicked.connect(btn_add_clicked)
btn_show.clicked.connect(btn_show_clicked)


window_meno.setCentralWidget(window)
window_meno.setLayout(layout)
window_meno.show()
sys.exit(app.exec_())



from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window_meno = QMainWindow()
window.setWindowTitle("رستوران")
layout = QVBoxLayout(window)

food_prices = {
    "کباب": 100,
    "مرغ": 200,
    "کله پاچه": 300
}

list_food = list(food_prices.keys())
my_list1 = []
total_price = 0

food_layout = QHBoxLayout()
price_layout = QHBoxLayout()
input_layout = QHBoxLayout()
btn_layout = QHBoxLayout()
show_price_layout = QHBoxLayout()

meno = window_meno.menuBar()
file = meno.addMenu("File")
help1 = meno.addMenu("Help")
edit = meno.addMenu("Edit")
address = meno.addMenu("List")
meno1 = meno.addMenu("meno")

act_file = QAction("open")
act_file1 = QAction("save")
act_file2 = QAction("exit")

act_help = QAction("about")
act_help1 = QAction("help")
act_help2 = QAction("quit")

act_edit = QAction("edit")
act_edit1 = QAction("text")
act_edit2 = QAction("cambak")

act_address = QAction("address")
act_address1 = QAction("address1")
act_address2 = QAction("address2")
act_address3 = QAction("address3")

act_meno = QAction("meno")
act_meno1 = QAction("meno1")
act_meno2 = QAction("meno2")
act_meno3 = QAction("meno3")

file.addAction(act_file)
file.addAction(act_file1)
file.addAction(act_file2)

help1.addAction(act_help)
help1.addAction(act_help1)
help1.addAction(act_help2)

edit.addAction(act_edit)
edit.addAction(act_edit1)
edit.addAction(act_edit2)

address.addAction(act_address)
address.addAction(act_address1)
address.addAction(act_address2)
address.addAction(act_address3)

meno1.addAction(act_meno)
meno1.addAction(act_meno1)
meno1.addAction(act_meno2)
meno1.addAction(act_meno3)

text = QLabel("غذاها:")
text1 = QLabel("کباب")
text2 = QLabel("مرغ")
text3 = QLabel("کله پاچه")
# text4 = QLabel("قیمه")

text5 = QLabel("100")
text6 = QLabel("200")
text7 = QLabel("300")
# text8 = QLabel("400")

text_price_title = QLabel("قیمت نهایی:")
text_price_value = QLabel("0")

text11 = QLineEdit()
text11.setPlaceholderText("نام غذا را وارد کنید")

btn_add = QPushButton("افزودن")
btn_show = QPushButton("نمایش لیست")

text12 = QLabel("           ")

combo = QComboBox()
# combo.addItem("text1")
# combo.addItem("text2")
# combo.addItem("text3")
combo.addItems(["text1","text2","text3","text4","text5"])

chek = QCheckBox("صبحانه")
chek1 = QCheckBox("نهار")
chek2 = QCheckBox("شام")

my_list = QListWidget()

food_layout.addWidget(text)
food_layout.addWidget(text1)
food_layout.addWidget(text2)
food_layout.addWidget(text3)
# food_layout.addWidget(text4)

price_layout.addWidget(text5)
price_layout.addWidget(text6)
price_layout.addWidget(text7)
# price_layout.addWidget(text8)

input_layout.addWidget(text11)

btn_layout.addWidget(btn_show)
btn_layout.addWidget(btn_add)

show_price_layout.addWidget(text_price_title)
show_price_layout.addWidget(text_price_value)


def btn_add_clicked():
    global total_price

    new_food = text11.text().strip()

    if not new_food:
        QMessageBox.warning(window, "خطا", "لطفاً نام غذا را وارد کنید")
        return

    if new_food not in list_food:
        QMessageBox.warning(window, "خطا", "غذایی با این نام وجود ندارد")
        return

    if new_food in my_list1:
        QMessageBox.warning(window, "خطا", "این غذا قبلاً اضافه شده")
        return

    my_list1.append(new_food)
    my_list.addItem(new_food)

    total_price += food_prices[new_food]
    text_price_value.setText(str(total_price))

def btn_show_clicked():
    QMessageBox.information(window, "لیست غذاها", str(my_list1))

def exit_clicked():
    app.quit()

def combo_func():
    combo_text = combo.currentText()
    text12.setText(combo_text)

def ceck_box():
    if chek.isChecked():
        text12.setText("صبحانه")
        text11.setText("کله پاچه")
        chek.setChecked(False)
    elif chek1.isChecked():
        text12.setText("نهار")
        text11.setText("مرغ")
        chek1.setChecked(False)
    elif chek2.isChecked():
        text12.setText("شام")
        text11.setText("کباب")
        chek2.setChecked(False)
    else:
        text12.setText("??????????")


layout.addWidget(combo)
layout.addWidget(text12)
layout.addLayout(food_layout)
layout.addLayout(price_layout)
layout.addLayout(input_layout)
layout.addLayout(btn_layout)
layout.addWidget(my_list)
layout.addLayout(show_price_layout)
layout.addWidget(chek)
layout.addWidget(chek1)
layout.addWidget(chek2)

chek.stateChanged.connect(ceck_box)
chek1.stateChanged.connect(ceck_box)
chek2.stateChanged.connect(ceck_box)

combo.currentIndexChanged.connect(combo_func)
act_file2.triggered.connect(exit_clicked)

btn_add.clicked.connect(btn_add_clicked)
btn_show.clicked.connect(btn_show_clicked)

window_meno.setCentralWidget(window)
window_meno.setLayout(layout)
window_meno.show()
sys.exit(app.exec_())



from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window_meno = QMainWindow()
window.setWindowTitle("رستوران")
layout = QVBoxLayout(window)

food_prices = {
    "کباب": 100,
    "مرغ": 200,
    "کله پاچه": 300
}

list_food = list(food_prices.keys())
my_list1 = []
total_price = 0

food_layout = QHBoxLayout()
price_layout = QHBoxLayout()
input_layout = QHBoxLayout()
btn_layout = QHBoxLayout()
show_price_layout = QHBoxLayout()

meno = window_meno.menuBar()
file = meno.addMenu("File")
help1 = meno.addMenu("Help")
edit = meno.addMenu("Edit")
address = meno.addMenu("List")
meno1 = meno.addMenu("meno")

act_file = QAction("open")
act_file1 = QAction("save")
act_file2 = QAction("exit")

act_help = QAction("about")
act_help1 = QAction("help")
act_help2 = QAction("quit")

act_edit = QAction("edit")
act_edit1 = QAction("text")
act_edit2 = QAction("cambak")

act_address = QAction("address")
act_address1 = QAction("address1")
act_address2 = QAction("address2")
act_address3 = QAction("address3")

act_meno = QAction("meno")
act_meno1 = QAction("meno1")
act_meno2 = QAction("meno2")
act_meno3 = QAction("meno3")

file.addAction(act_file)
file.addAction(act_file1)
file.addAction(act_file2)

help1.addAction(act_help)
help1.addAction(act_help1)
help1.addAction(act_help2)

edit.addAction(act_edit)
edit.addAction(act_edit1)
edit.addAction(act_edit2)

address.addAction(act_address)
address.addAction(act_address1)
address.addAction(act_address2)
address.addAction(act_address3)

meno1.addAction(act_meno)
meno1.addAction(act_meno1)
meno1.addAction(act_meno2)
meno1.addAction(act_meno3)

text = QLabel("غذاها:")
text1 = QLabel("کباب")
text2 = QLabel("مرغ")
text3 = QLabel("کله پاچه")

text5 = QLabel("100")
text6 = QLabel("200")
text7 = QLabel("300")

text_price_title = QLabel("قیمت نهایی:")
text_price_value = QLabel("0")

text11 = QLineEdit()
text11.setPlaceholderText("نام غذا را وارد کنید")

btn_add = QPushButton("افزودن")
btn_show = QPushButton("نمایش لیست")

text12 = QLabel("           ")

combo = QComboBox()
combo.addItems(["text1","text2","text3","text4","text5"])

chek = QCheckBox("صبحانه")
chek1 = QCheckBox("نهار")
chek2 = QCheckBox("شام")

my_list = QListWidget()

food_layout.addWidget(text)
food_layout.addWidget(text1)
food_layout.addWidget(text2)
food_layout.addWidget(text3)

price_layout.addWidget(text5)
price_layout.addWidget(text6)
price_layout.addWidget(text7)

input_layout.addWidget(text11)

btn_layout.addWidget(btn_show)
btn_layout.addWidget(btn_add)

show_price_layout.addWidget(text_price_title)
show_price_layout.addWidget(text_price_value)

def btn_add_clicked():
    global total_price

    new_food = text11.text().strip()

    if not new_food:
        QMessageBox.warning(window, "خطا", "لطفاً نام غذا را وارد کنید")
        return

    if new_food not in list_food:
        QMessageBox.warning(window, "خطا", "غذایی با این نام وجود ندارد")
        return

    if new_food in my_list1:
        QMessageBox.warning(window, "خطا", "این غذا قبلاً اضافه شده")
        return

    my_list1.append(new_food)
    my_list.addItem(new_food)

    total_price += food_prices[new_food]
    text_price_value.setText(str(total_price))

def btn_show_clicked():
    QMessageBox.information(window, "لیست غذاها", str(my_list1))

def exit_clicked():
    try:
        exit_massage = QMessageBox.quesstion(window, "tex", "test", QMessageBox.Ok)
    except Exception as e:
        print(e)
    # if exit_massage == QMessageBox.Yes:
    #     app.quit()
def combo_func():
    combo_text = combo.currentText()
    text12.setText(combo_text)

def ceck_box():
    if chek.isChecked():
        text12.setText("صبحانه")
        text11.setText("کله پاچه")
        chek.setChecked(False)
    elif chek1.isChecked():
        text12.setText("نهار")
        text11.setText("مرغ")
        chek1.setChecked(False)
    elif chek2.isChecked():
        text12.setText("شام")
        text11.setText("کباب")
        chek2.setChecked(False)
    else:
        text12.setText("??????????")

def file_mood():
    QMessageBox.information(window,"کمک","همچین فایلی وجود نداره !")



layout.addWidget(combo)
layout.addWidget(text12)
layout.addLayout(food_layout)
layout.addLayout(price_layout)
layout.addLayout(input_layout)
layout.addLayout(btn_layout)
layout.addWidget(my_list)
layout.addLayout(show_price_layout)
layout.addWidget(chek)
layout.addWidget(chek1)
layout.addWidget(chek2)

chek.stateChanged.connect(ceck_box)
chek1.stateChanged.connect(ceck_box)
chek2.stateChanged.connect(ceck_box)
act_file.triggered.connect(file_mood)

combo.currentIndexChanged.connect(combo_func)
act_file2.triggered.connect(exit_clicked)

btn_add.clicked.connect(btn_add_clicked)
btn_show.clicked.connect(btn_show_clicked)

window_meno.setCentralWidget(window)
window_meno.setLayout(layout)
window_meno.show()
sys.exit(app.exec_())



from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window_meno = QMainWindow()
window.setWindowTitle("رستوران")
layout = QVBoxLayout(window)

food_prices = {
    "کباب": 100,
    "مرغ": 200,
    "کله پاچه": 300,
    "قیمه": 400
}

list_food = list(food_prices.keys())
my_list1 = []
total_price = 0

food_layout = QHBoxLayout()
price_layout = QHBoxLayout()
input_layout = QHBoxLayout()
btn_layout = QHBoxLayout()
show_price_layout = QHBoxLayout()

meno = window_meno.menuBar()
file = meno.addMenu("File")
help1 = meno.addMenu("Help")
edit = meno.addMenu("Edit")
address = meno.addMenu("List")
meno1 = meno.addMenu("meno")

act_file = QAction("open")
act_file1 = QAction("save")
act_file2 = QAction("exit")

act_file2.setShortcut("Ctrl+A")

act_help = QAction("about")
act_help1 = QAction("help")
act_help2 = QAction("quit")

act_edit = QAction("edit")
act_edit1 = QAction("text")
act_edit2 = QAction("cambak")

act_address = QAction("address")
act_address1 = QAction("address1")
act_address2 = QAction("address2")
act_address3 = QAction("address3")

act_meno = QAction("meno")
act_meno1 = QAction("meno1")
act_meno2 = QAction("meno2")
act_meno3 = QAction("meno3")

file.addAction(act_file)
file.addAction(act_file1)
file.addAction(act_file2)

help1.addAction(act_help)
help1.addAction(act_help1)
help1.addAction(act_help2)

edit.addAction(act_edit)
edit.addAction(act_edit1)
edit.addAction(act_edit2)

address.addAction(act_address)
address.addAction(act_address1)
address.addAction(act_address2)
address.addAction(act_address3)

meno1.addAction(act_meno)
meno1.addAction(act_meno1)
meno1.addAction(act_meno2)
meno1.addAction(act_meno3)

text = QLabel("غذاها:")
text1 = QLabel("کباب")
text2 = QLabel("مرغ")
text3 = QLabel("کله پاچه")
text4 = QLabel("قیمه")
text5 = QLabel("100")
text6 = QLabel("200")
text7 = QLabel("300")
text8 = QLabel("400")

text_price_title = QLabel("قیمت نهایی:")
text_price_value = QLabel("0")

text11 = QLineEdit()
text11.setPlaceholderText("نام غذا را وارد کنید")
text12 = QLabel("                   ")

btn_add = QPushButton("افزودن")
btn_show = QPushButton("نمایش لیست")

my_list = QListWidget()

food_layout.addWidget(text)
food_layout.addWidget(text1)
food_layout.addWidget(text2)
food_layout.addWidget(text3)
food_layout.addWidget(text4)
price_layout.addWidget(text5)
price_layout.addWidget(text6)
price_layout.addWidget(text7)
price_layout.addWidget(text8)
input_layout.addWidget(text11)
btn_layout.addWidget(btn_show)
btn_layout.addWidget(btn_add)
show_price_layout.addWidget(text_price_title)
show_price_layout.addWidget(text_price_value)



def btn_add_clicked():
    global total_price

    new_food = text11.text().strip()
    my_list1.append(new_food)
    my_list.addItem(new_food)

    total_price += food_prices[new_food]
    text_price_value.setText(str(total_price))

def btn_show_clicked():
    QMessageBox.information(window, "لیست غذاها", str(my_list1))

def help_clicked():
    QMessageBox.information(window, "help", "این صفحه به منظور کمک به شماست ")

def exit_clicked():
    exit_massage=QMessageBox.question(window,"exit","exit?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if exit_massage==QMessageBox.Yes:
        app.quit()

def open_clicked():
    file,_ = QFileDialog.getOpenFileName(window, "open file", "", "*.txt;; *.py")

    if file:
        QMessageBox.information(window,"file",f"your file is {file} .")

combo = QComboBox()
combo.addItems(["text1", "text2", "text3"])

check1 = QCheckBox("صبحانه")
check2= QCheckBox("ناهار")
check3 = QCheckBox("شام")

def combo_func():
    combo_text = combo.currentText()
    text12.setText(combo_text)


def check_box():
    if check1.isChecked():
        text12.setText("صبحانه")
        check1.setChecked(False)
    elif check2.isChecked():
        text12.setText("ناهار")
        text11.setText("قیمه")
        check2.setChecked(False)
    elif check3.isChecked():
        text12.setText("شام")
        check3.setChecked(False)
    else:
        text12.setText("?????")


layout.addWidget(combo)
layout.addWidget(text12)
layout.addWidget(check1)
layout.addWidget(check2)
layout.addWidget(check3)
layout.addLayout(food_layout)
layout.addLayout(price_layout)
layout.addLayout(input_layout)
layout.addLayout(btn_layout)
layout.addWidget(my_list)
layout.addLayout(show_price_layout)

act_file2.triggered.connect(exit_clicked)
btn_add.clicked.connect(btn_add_clicked)
btn_show.clicked.connect(btn_show_clicked)
combo.currentIndexChanged.connect(combo_func)
check1.stateChanged.connect(check_box)
check2.stateChanged.connect(check_box)
check3.stateChanged.connect(check_box)
act_help1.triggered.connect(help_clicked)
act_file.triggered.connect(open_clicked)

window_meno.setCentralWidget(window)
window_meno.setLayout(layout)
window_meno.show()
sys.exit(app.exec_())


from PyQt5.QtWidgets import *
import sys
from openpyxl import load_workbook, Workbook

try:
    wb = load_workbook("test.xlsx")
    sheet = wb.active
except Exception as e:
    wb = Workbook()
    sheet = wb.active
    sheet.append(["نام","فامیل","کلاس"])

app = QApplication(sys.argv)
window_menu = QMainWindow()
window = QWidget()
window_menu.setWindowTitle("ثبت")
layout = QVBoxLayout(window)

name_Layout = QHBoxLayout()
last_name_layout = QHBoxLayout()
class_Layout = QHBoxLayout()

meno = window_menu.menuBar()
file = meno.addMenu("File")
help1 = meno.addMenu("Help")

act_file1 = QAction("open")
act_file2 = QAction("save")
act_file3= QAction("exit")

act_file3.setShortcut("Ctrl+a")

act_help1 = QAction("help")
act_help2 = QAction("about")
act_help3 = QAction("quit")

file.addAction(act_file1)
file.addAction(act_file2)
file.addAction(act_file3)

help1.addAction(act_help1)
help1.addAction(act_help2)
help1.addAction(act_help3)

text = QLabel("نام :   ")
line = QLineEdit()

text1 = QLabel("فامیل:")
line1 = QLineEdit()

text2 = QLabel("کلاس:")
combo = QComboBox()
combo.addItems(["نهم","دهم","یازدهم"])

btn = QPushButton("ثبت")
list1 = QListWidget()

name_Layout.addWidget(line)
name_Layout.addWidget(text)
last_name_layout.addWidget(line1)
last_name_layout.addWidget(text1)
class_Layout.addWidget(combo)
class_Layout.addWidget(text2)


layout.addLayout(name_Layout)
layout.addLayout(last_name_layout)
layout.addLayout(class_Layout)
layout.addWidget(btn)
layout.addWidget(list1)

def btn_clicked():
    text_name = line.text()
    text_last_name = line1.text()
    text_class_name = combo.currentText()

    sheet.append([text_name,text_last_name,text_class_name])
    wb.save("test.xlsx")
    line.clear()
    list1.clear()
    QMessageBox.information(window,"ذخیره شده","اطلاعات ثبت شد")

btn.clicked.connect(btn_clicked)

window_menu.setCentralWidget(window)
window_menu.setLayout(layout)
window_menu.show()
sys.exit(app.exec_())


from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window_meno = QMainWindow()
window_meno.setWindowTitle(" برنامه ریزی غذایی ")
layout = QVBoxLayout(window)

meno = window_meno.menuBar()
file = meno.addMenu("فایل ها")
help1 = meno.addMenu("کمک")
edit = meno.addMenu("تغیر")
address = meno.addMenu("لیست")
meno1 = meno.addMenu("منو")

act_file = QAction("بازکردن")
act_file1 = QAction("ذخیره کردن")
act_file2 = QAction("خارج شدن")

act_file2.setShortcut("Ctrl+A")

act_help = QAction("موضوع ها")
act_help1 = QAction("کمک سیستمی")
act_help2 = QAction("بی صدا")

act_edit = QAction("ادیت هت")
act_edit1 = QAction("نوشته ها")
act_edit2 = QAction("بازگشت")

act_address = QAction("برنامه اول")
act_address1 = QAction("برنامه دوم")
act_address2 = QAction("برنامه سوم")
act_address3 = QAction("برنامه چهارم")

act_meno = QAction("منوی اول")
act_meno1 = QAction("منوی دوم")
act_meno2 = QAction("منوی سوم")
act_meno3 = QAction("منوی چهارم")

file.addAction(act_file)
file.addAction(act_file1)
file.addAction(act_file2)

help1.addAction(act_help)
help1.addAction(act_help1)
help1.addAction(act_help2)

edit.addAction(act_edit)
edit.addAction(act_edit1)
edit.addAction(act_edit2)

address.addAction(act_address)
address.addAction(act_address1)
address.addAction(act_address2)
address.addAction(act_address3)

meno1.addAction(act_meno)
meno1.addAction(act_meno1)
meno1.addAction(act_meno2)
meno1.addAction(act_meno3)

text = QLabel("لیست غذای های موجود :")
list = QListWidget()
list.addItems(["گوشت گاو","سبزیجات","تخم مرغ","ماهی","مرغ","کراتین","مغزیجات"])
list.addItems(["لازانیا","همبرگر","پیتزا","فلافل","هات داگ","بندری"])

text1 = QLabel("نوع غذا :")
btn = QPushButton("ثبت")
btn1 = QRadioButton("ایرانی")
btn2 = QRadioButton("عربی")
btn3 = QRadioButton("ایتالیای")

layout_btn = QHBoxLayout()
layout_btn.addWidget(btn1)
layout_btn.addWidget(btn2)
layout_btn.addWidget(btn3)

text2 = QLabel("برنامه غذایی مورد نظر شما :")
list2 = QListWidget()
layout.addWidget(text)
layout.addWidget(list)
layout.addWidget(btn)
layout.addWidget(text1)
layout.addLayout(layout_btn)
layout.addWidget(text2)
layout.addWidget(list2)

window_meno.setCentralWidget(window)
window_meno.setLayout(layout)
window_meno.show()
app.exec_()