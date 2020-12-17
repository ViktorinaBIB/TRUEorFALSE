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
    question.pack()
    btn_tr.pack()
    btn_fa.pack()

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
    btn1 = Button (root, text="Правда", font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_r(que4))
    btn2 = Button (root, text="Ложь", font = "Calibri", bg="red3", fg="black", command=lambda: next_w(que4))
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
    btn1 = Button (root, text="Правда",font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_w(que5))
    btn2 = Button (root, text="Ложь", font = "Calibri", bg="red3", fg="black", command=lambda: next_r(que5))
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

def que5():
    question = Label(root, text= "Жираф может прожить без воды ")
    btn1 = Button (root, text="Правда",font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_r(que6))
    btn2 = Button (root, text="Ложь", font = "Calibri", bg="red3", fg="black", command=lambda: next_w(que6))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que6):
        global count 
        count += 1 
        clear()
        que6()
    def next_w(que6):
        clear()
        que6()

def que6():
    question = Label(root, text= "Несмоторя на внушительные размеры белого кита,")
    question2 = Label(root, text = "его сердце всего лишь в 2 раза больше человеческого")
    btn1 = Button (root, text="Правда",font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_w(que7))
    btn2 = Button (root, text="Ложь", font = "Calibri", bg="red3", fg="black", command=lambda: next_r(que7))
    question.pack()
    question2.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que7):
        global count 
        count += 1 
        clear()
        que7()
    def next_w(que7):
        clear()
        que7()

def que7():
    question = Label(root, text= "Галапагосские черепахи - единственные существа в мире,")
    question2 = Label(root, text = "у которых самцы выращивают потомство")
    btn1 = Button (root, text="Правда",font = "Calibri", bg="OliveDrab2", fg="black", command=lambda: next_w(que8))
    btn2 = Button (root, text="Ложь", font = "Calibri", bg="red3", fg="black", command=lambda: next_r(que8))
    question.pack()
    question2.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que8):
        global count 
        count += 1 
        clear()
        que8()
    def next_w(que8):
        clear()
        que8()

def que8():
    question = Label(root, text="Самая короткая война в мире длилась около двух дней")
    btn1=Button(root,text="Правда",font="Calibri", bg="OliveDrab2",fg="black",command=lambda:next_w(que9))
    btn2=Button(root,text="Ложь",font="Calibri", bg="red3",fg="black",command=lambda:next_r(que9))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que9):
        global count
        count +=1
        clear()
        que9()
    def next_w(que9):
        clear()
        que9()

def que9():
    question = Label(root, text="Существуют рыбы, которые могут жить на суше")
    btn1=Button(root,text="Правда",font="Calibri", bg="OliveDrab2",fg="black",command=lambda:next_r(que10))
    btn2=Button(root,text="Ложь",font="Calibri", bg="red3",fg="black",command=lambda:next_w(que10))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que9):
        global count
        count +=1
        clear()
        que10()
    def next_w(que9):
        clear()
        que10()

def que10():
    question = Label(root, text="Больше всего озер расположено в Канаде")
    btn1=Button(root,text="Правда",font="Calibri", bg="OliveDrab2",fg="black",command=lambda:next_r(res))
    btn2=Button(root,text="Ложь",font="Calibri", bg="red3",fg="black",command=lambda:next_w(res))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(res):
        global count
        count +=1
        clear()
        res()
    def next_w(res):
        clear()
        res()

def res():
    result = Label(root, text='Результат: '+ str(count) + ' из 10')
    if (count<=10) and (count>=8):
        description = "Поздравляем! Прекрасный результат!"
    elif (count<=7) and (count>=5):
        description = "Неплохо! Вы достаточно много знаете."
    elif (count<=4) and (count>=0):
        description = "Не расстраивайтесь! Вы можете попробовать ещё раз."
    result.pack()
    description.pack()
que1()
root.mainloop()