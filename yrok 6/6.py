from tkinter import*
window = Tk()
window.title('пр_6')
window.geometry('1500x860')

def one(): 
    a = okno_1.get()
    n = int(a)
    k = 1
    i = ''
    while k**2<=n:
        i += str(k**2)
        k += 1
        i += ' '
    a1.configure(text = i)

zadacha_1 = Label(window, text='1. По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.', font=("calibri", 11, 'italic', ))
zadacha_1.place(x=15, y=20)

n_1 = Label(window, text='Ввести число - ', font=("calibri", 10))
n_1.place(x=15, y=50)

okno_1 = Entry(window, width=10)
okno_1.place(x=105, y=52)

b1 = Button(window, text='решить', command=one)
b1.place(x=180, y=48)

c1 = Label(window, text='ответ - ')
c1.place(x=240, y=50)

a1 = Label(window, text='')
a1.place(x=280, y=50)


def two(): 
    a = okno_2.get()
    n = int(a)
    k = 2
    while n % k != 0:
        k += 1

    a2.configure(text = k)

zadacha_2 = Label(window, text='2. Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.', font=("calibri", 11, 'italic', ))
zadacha_2.place(x=15, y=100)

n_2 = Label(window, text='Ввести число - ', font=("calibri", 10))
n_2.place(x=15, y=130)

okno_2 = Entry(window, width=10)
okno_2.place(x=105, y=132)

b2 = Button(window, text='решить', command=two)
b2.place(x=180, y=128)

c2 = Label(window, text='ответ - ')
c2.place(x=240, y=130)

a2 = Label(window, text='')
a2.place(x=280, y=130)

def three():
    a = okno_3.get()
    n = int(a)
    d = 1
    s = 0
    i = ''
    while d <= n:
        d =d * 2
        s = s + 1
    i ="показатель степени - " + str(s-1) +" "+"число - " + str(d//2)
    a3.configure(text = i)

zadacha_3 = Label(window, text='3. По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. \r Выведите показатель степени и саму степень. Операцией возведения в степень пользоваться нельзя!', font=("calibri", 11, 'italic', ))
zadacha_3.place(x=15, y=180)

n_3 = Label(window, text='Ввести число - ', font=("calibri", 10))
n_3.place(x=15, y=230)

okno_3 = Entry(window, width=10)
okno_3.place(x=105, y=232)

b3 = Button(window, text='решить', command=three)
b3.place(x=180, y=228)

c3 = Label(window, text='ответ - ')
c3.place(x=240, y=230)

a3 = Label(window, text='')
a3.place(x=280, y=230)

def four():
    a1 = okno_14.get()
    y = int(a1)
    a2 = okno_12.get()
    x = int(a2)
    k = 0
    i = ''
    if (y or x) >=0:
        while x <= y:
            if x==y:
                break
            x+=x/10
            k+=1
        i = (k)      
    a4.configure(text = i)

zadacha_4 = Label(window, text='4. В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. \r По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров. \r Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.', font=("calibri", 11, 'italic', ))
zadacha_4.place(x=15, y=280)

n_4 = Label(window, text='Ввести число - ', font=("calibri", 10))
n_4.place(x=15, y=345)

okno_14 = Entry(window, width=10)
okno_14.place(x=105, y=345)

okno_12 = Entry(window, width=10)
okno_12.place(x=180, y=345)

b4 = Button(window, text='решить', command=four)
b4.place(x=256, y=341)

c4 = Label(window, text='ответ - ')
c4.place(x=315, y=343)

a4 = Label(window, text='')
a4.place(x=380, y=345)

i= 0
def five():
    global i
    a = okno_5.get()
    n=int(a)
    
    while int(okno_5.get())!=0:
        i = i + 1
        okno_5.delete(0,END)
        
    else:
        
        a5.configure(text = i)       
     
        

zadacha_5 = Label(window, text='5. Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. Последовательность завершается числом 0, при считывании \rкоторого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.', font=("calibri", 11, 'italic', ))
zadacha_5.place(x=15, y=390)

n_5 = Label(window, text='Ввести число - ', font=("calibri", 10))
n_5.place(x=15, y=435)

okno_5 = Entry(window, width=10)
okno_5.place(x=105, y=438)

b5 = Button(window, text='решить', command=five)
b5.place(x=180, y=435)

c5 = Label(window, text='ответ - ')
c5.place(x=240, y=436)

a5 = Label(window, text='')
a5.place(x=290, y=437)

sum = 0
length = 0
def six():
    global length
    a = okno_6.get()
    print(a)
    global sum
    if a != "0":
        length+=1
        sum +=int(a)
    else:   
        a6.configure(text = sum / length)        
    okno_6.delete(0,END)
        

zadacha_6 = Label(window, text='6. Определите среднее значение всех элементов последовательности, завершающейся числом 0.', font=("calibri", 11, 'italic', ))
zadacha_6.place(x=15, y=500)

n_6 = Label(window, text='Ввести число - ', font=("calibri", 10))
n_6.place(x=15, y=540)
okno_6 = Entry(window, width=10)
okno_6.place(x=105, y=540)

b6 = Button(window, text='решить', command=six)
b6.place(x=180, y=538)

c6 = Label(window, text='ответ - ')
c6.place(x=240, y=540)

a6 = Label(window, text='')
a6.place(x=290, y=540)

window.mainloop()