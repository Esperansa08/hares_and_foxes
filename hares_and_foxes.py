"""Игра по угадыванию количества зайцев"""

from tkinter import Text, Button, Label, Frame, PhotoImage, Tk
from tkinter import CENTER, LEFT, END
import random
import time
N = 0


def bros():
    global N
    x = random.choice(['fox.png', 'hare.png'])
    if x == 'hare.png':
        N += 1
    return x


def ish_pos(event=0):
    global b1, b2, b3, b4
    b1 = PhotoImage(file=('back.png'))
    b2 = PhotoImage(file=('back.png'))
    b3 = PhotoImage(file=('back.png'))
    b4 = PhotoImage(file=('back.png'))
    lab1['image'] = b1
    lab2['image'] = b2
    lab3['image'] = b3
    lab4['image'] = b4


def img(event=0):
    global b1, b2, b3, b4, N
    s = text.get(1.0, END)
    if type(s) != int and int(s) > 4:
        lab['text'] = "Значение должно быть целое от 0 до 4!!"

    else:
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        b3 = PhotoImage(file=(bros()))
        b4 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        lab3['image'] = b3
        lab4['image'] = b4

        if N == int(s):
            lab['fg'] = 'green'
            lab['text'] = "Победа!!"
        else:
            lab['fg'] = 'red'
            lab['text'] = ("Неудача!!")

    N = 0
    text.delete(1.0, END)
    root.update()
    time.sleep(2.5)
    ish_pos()


root = Tk()
Title = Label(text="Сколько будет зайцев?", width=22, height=2)
Title['font'] = ("Verdana", 20)
Title.pack()
text = Text(width=1, height=1)
text.pack()
frame = Frame()
frame.pack()
root.geometry('550x830')
root.title('Зайцы и лисы')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file=('icon.png')))
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.27, rely=0.35, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.27, rely=0.73, anchor=CENTER)
lab3 = Label(root)
lab3.place(relx=0.75, rely=0.35, anchor=CENTER)
lab4 = Label(root)
lab4.place(relx=0.75, rely=0.73, anchor=CENTER)
ish_pos()

Button(frame, text="Запуск", command=img).pack(side=LEFT)
lab = Label(width=40, height=3)
lab['font'] = ("Verdana", 16, 'bold')
lab.pack()

root.mainloop()
