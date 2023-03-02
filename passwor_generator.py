import random as r
from tkinter import * 
from tkinter import messagebox as mb

class main:
    yon = True

def y_check():
    if not main.yon:
        y['bg'] = '#4b4b4b'
        n['bg'] = '#171717'
        main.yon = True

def n_check():
    if main.yon:
        n['bg'] = '#4b4b4b'
        y['bg'] = '#171717'
        main.yon = False

def generate():
    a = 'abcdefghigklmnopqrstuvwxyz'
    nums = '0123456789'
    symb = '@#$%&,.'
    u_d = 0
    n_w = 0
    password = ''

    try:
        cnt = int(count.get())
    except:
        mb.showerror(title='Ошибка', message='Кажется вы ввели не число, будет использовано значение по умолчанию(8)')
        count.delete(0, 'end')
        count.insert(0, 8)
        cnt = 8

    if cnt > 15 or cnt < 1:
        mb.showerror(title='Ошибка', message='Значение выходит за пределы(1-15), будет использовано значение по умолчанию(8)')
        count.delete(0, 'end')
        count.insert(0, 8)
        cnt = 8

    for i in range(cnt):
        if not main.yon:
            n_w = r.randint(0, 1)
        else:
            n_w = r.randint(0, 2)
            
        if n_w == 1:
            u_d = r.randint(0, 1)
            if u_d == 0:
                password += r.choice(a)
            elif u_d == 1:
                password += r.choice(a).upper()
        elif n_w == 0:
            password += r.choice(nums)
        else:
            password += r.choice(symb)

    res.delete(0, 'end')
    res.insert(0, password)
        
w = Tk()
w.geometry('300x200')
w.resizable(width=0, height=0)
w['bg'] = '#171717'
w.title('Password Generator 2.0')

count = Entry(w, font=('Comic Sans MS', 24, 'bold'), fg='white', width=2, bg='#212121', relief='flat')
count.place(x=65, y=30)
count.insert(0, 8)

c = Label(w, font=('Comic Sans MS', 10, 'bold'), fg='white', text='Число символов', bg='#171717')
c.place(x=30, y=5)

symb_txt = Label(w, font=('Comic Sans MS', 10, 'bold'), fg='white', text='Спец. символы?', bg='#171717')
symb_txt.place(x=155, y=5)

y = Button(w, font=('Comic Sans MS', 15, 'bold'), fg='white', text='ДА', bg='#4b4b4b', relief='flat', command=y_check)
y.place(x=155, y=30)

n = Button(w, font=('Comic Sans MS', 15, 'bold'), fg='white', text='НЕТ', bg='#212121', relief='flat', command=n_check)
n.place(x=205, y=30)

btn = Button(w, font=('Comic Sans MS', 15, 'bold'), fg='white', text='СГЕНЕРИРОВАТЬ!', bg='#212121', relief='flat', command=generate)
btn.place(x=55, y=90)

res = Entry(w, font=('Comic Sans MS', 16, 'bold'), fg='white', width=16, bg='#212121', relief='flat')
res.place(x=45, y=155)

w.mainloop()