# TRUEorFALSE
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Правда или Ложь')
image = ImageTk.PhotoImage(file = "C:\\Users\\olesya\\Pictures\\Screenshots\\RkNC2XOxYdM.png")
root.geometry('400x400')
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 
count=0
root.mainloop()

def clear():
    list=root.pack_slaves()
    for l in list:
        l.destroy()

def que1():
    question = Label(root, text = "Детёныши жирафов рождаются без пятен")
    btn_tr = Button(root, text = "Правда", bg="OliveDrab2", fg="black", command=lambda: next_w(que2))
    btn_fa = Button(root, text = "Ложь", bg="red3", fg="black", command=lambda: next_r(que2))
    question.pack()
    btn_tr.pack()
    btn_fa.pack()

    def next_r(que2):
        global count
        count+=1
        clear()
        que2()
    
    def next_w(que2):
        clear()
        que2()

def que2():
    question = Label(root, text = "Вы не чувствуете запахов, пока спите")
    btn_tr = Button(root, text = "Правда", bg="OliveDrab2", fg="black", command=lambda: next_r(que3))
    btn_fa = Button(root, text = "Ложь", bg="red3", fg="black", command=lambda: next_w(que3))
    question.grid(row=3)
    btn_tr.grid(row=5)
    btn_fa.grid(row=6)

    def next_r(que3):
        global count
        count+=1
        clear()
        que3()
    
    def next_w(que3):
        clear()
        que3()

def que3():
    question = Label(root, text= "Утиное крякание не дает эхо")
    btn1 = Button (root, text="Правда", bg="OliveDrab2", fg="black", command=lambda: next_r(que4))
    btn2 = Button (root, text="Ложь", bg="OliveDrab2", fg="black", command=lambda: next_w(que4))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que4):
        global count 
        count += 1 
        clear()
        que4()
    def next_w(que4):
        clear()
        que4()

def que4():
    question = Label(root, text= "Самое ядовитое существо на планете змея")
    btn1 = Button (root, text="Правда",font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_w(que2))
    btn2 = Button (root, text="Ложь", font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_r(que2))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que5):
        global count 
        count += 1 
        clear()
        que5()
    def next_w(que5):
        clear()
        que5()