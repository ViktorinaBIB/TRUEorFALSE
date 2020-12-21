# TRUEorFALSE
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Правда или Ложь')
image = ImageTk.PhotoImage(file = "i8yDHtpi2K4.png")
root.geometry('1200x800')
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 
count=0


def clear():
    '''Очищает окно tkinter от виджетов'''
    list=root.pack_slaves()
    for l in list:
        l.destroy()

def que1():
    '''Отображает первый вопрос и кнопки для ответа'''
    question = Label(root, text = "Детёныши жирафов рождаются без пятен", font = ("KacstArt", 30))
    btn_tr = Button(root, text = "Правда", font = ("KacstArt", 30), bg="OliveDrab2", fg="black", command=lambda: next_w(que2))
    btn_fa = Button(root, text = "Ложь", font = ("KacstArt", 30), bg="red3", fg="black", command=lambda: next_r(que2))
    question.pack()
    btn_tr.pack()
    btn_fa.pack()

    def next_r(que2):
        '''Очищает окно и обращается ко второму вопросу, увеличивает счетчик на 1'''
        global count
        count+=1
        clear()
        que2()
    
    def next_w(que2):
        '''Очищает окно и обращается ко второму вопросу'''
        clear()
        que2()

def que2():
    '''Отображает второй вопрос и кнопки для ответа'''
    question = Label(root, text = "Вы не чувствуете запахов, пока спите", font = ("KacstArt", 30))
    btn_tr = Button(root, text = "Правда", font = ("KacstArt", 30), bg="OliveDrab2", fg="black", command=lambda: next_r(que3))
    btn_fa = Button(root, text = "Ложь", font = ("KacstArt", 30), bg="red3", fg="black", command=lambda: next_w(que3))
    question.pack()
    btn_tr.pack()
    btn_fa.pack()

    def next_r(que3):
        '''Очищает окно и обращается к третьему вопросу, увеличивает счетчик на 1'''
        global count
        count+=1
        clear()
        que3()
    
    def next_w(que3):
        '''Очищает окно и обращается к третьему вопросу'''
        clear()
        que3()

def que3():
    '''Отображает 3 вопрос и кнопки для ответа'''
    question = Label(root, text= "Утиное крякание не дает эхо",font = ("KacstArt",30))
    btn1 = Button (root, text="Правда", font = ("KacstArt",30), bg="OliveDrab2", fg="black", command=lambda: next_r(que4))
    btn2 = Button (root, text="Ложь", font = ("KacstArt",30), bg="red3", fg="black", command=lambda: next_w(que4))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que4):
        '''Очищает окно от виджетов,обращается к четвертому вопросу и увеличивает счетчик на 1'''
        global count 
        count += 1 
        clear()
        que4()
    def next_w(que4):
        '''Очищает окно от виджетов и обращается к четвертому вопросу'''
        clear()
        que4()

def que4():
    '''Отображает 4 вопрос и кнопки для ответа'''
    question = Label(root, text= "Самое ядовитое существо на планете является змеёй",font = ("KacstArt",30))
    btn1 = Button (root, text="Правда",font = ("KacstArt",30), bg="OliveDrab2", fg="black", command=lambda: next_w(que5))
    btn2 = Button (root, text="Ложь", font = ("KacstArt",30), bg="red3", fg="black", command=lambda: next_r(que5))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que5):
        '''Очищает окно от виджетов,обращается к пятому вопросу и увеличивает счетчик на 1'''
        global count 
        count += 1 
        clear()
        que5()
    def next_w(que5):
        '''Очищает окно от виджетов и обращается к пятому вопросу'''
        clear()
        que5()

def que5():
    '''Отображает пятый вопрос и кнопки для ответа'''
    question = Label(root, text= "Жираф может прожить без воды дольше, чем верблюд", font = ("KacstArt", 30))
    btn1 = Button (root, text="Правда", font = ("KacstArt", 30), bg="OliveDrab2", fg="black", command=lambda: next_r(que6))
    btn2 = Button (root, text="Ложь", font = ("KacstArt", 30), bg="red3", fg="black", command=lambda: next_w(que6))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que6):
        '''Очищает окно и обращается к шестому вопросу, увеличивает счетчик на 1'''
        global count 
        count += 1 
        clear()
        que6()
    def next_w(que6):
        '''Очищает окно и обращается к шестому вопросу'''
        clear()
        que6()

def que6():
    '''Отображает шестой вопрос и кнопки для ответа'''
    question = Label(root, text= "Несмоторя на внушительные размеры белого кита,", font = ("KacstArt", 30))
    question2 = Label(root, text = "его сердце всего лишь в 2 раза больше человеческого", font = ("KacstArt", 30))
    btn1 = Button (root, text="Правда", font = ("KacstArt", 30), bg="OliveDrab2", fg="black", command=lambda: next_w(que7))
    btn2 = Button (root, text="Ложь", font = ("KacstArt", 30), bg="red3", fg="black", command=lambda: next_r(que7))
    question.pack()
    question2.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que7):
        '''Очищает окно и обращается к седьмому вопросу, увеличивает счетчик на 1'''
        global count 
        count += 1 
        clear()
        que7()
    def next_w(que7):
        '''Очищает окно и обращается к седьмому вопросу'''
        clear()
        que7()

def que7():
    '''Отображает седьмой вопрос и кнопки для ответа'''
    question = Label(root, text= "Галапагосские черепахи - единственные существа в мире,", font = ("KacstArt", 30))
    question2 = Label(root, text = "у которых самцы выращивают потомство", font = ("KacstArt", 30))
    btn1 = Button (root, text="Правда", font = ("KacstArt", 30), bg="OliveDrab2", fg="black", command=lambda: next_w(que8))
    btn2 = Button (root, text="Ложь", font = ("KacstArt", 30), bg="red3", fg="black", command=lambda: next_r(que8))
    question.pack()
    question2.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que8):
        '''Очищает окно и обращается к седьмому вопросу, увеличивает счетчик на 1'''
        global count 
        count += 1 
        clear()
        que8()
    def next_w(que8):
        '''Очищает окно и обращается к седьмому вопросу'''
        clear()
        que8()

def que8():
    '''Отображает 8 вопрос и кнопки для ответа'''
    question = Label(root, text="Самая короткая война в мире длилась около двух дней",font = ("KacstArt",30))
    btn1=Button(root,text="Правда",font = ("KacstArt",30), bg="OliveDrab2",fg="black",command=lambda:next_w(que9))
    btn2=Button(root,text="Ложь",font = ("KacstArt",30), bg="red3",fg="black",command=lambda:next_r(que9))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que9):
        '''Очищает окно от виджетов,обращается к девятому вопросу и увеличивает счетчик на 1'''
        global count
        count +=1
        clear()
        que9()
    def next_w(que9):
        '''Очищает окно от виджетов и обращается к девятому вопросу'''
        clear()
        que9()

def que9():
    '''Отображает 9 вопрос и кнопки для ответа'''
    question = Label(root, text="Существуют рыбы, которые могут жить на суше",font = ("KacstArt",30))
    btn1=Button(root,text="Правда",font = ("KacstArt",30), bg="OliveDrab2",fg="black",command=lambda:next_r(que10))
    btn2=Button(root,text="Ложь",font = ("KacstArt",30), bg="red3",fg="black",command=lambda:next_w(que10))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(que9):
        '''Очищает окно от виджетов,обращается к десятому вопросу и увеличивает счетчик на 1'''
        global count
        count +=1
        clear()
        que10()
    def next_w(que9):
        '''Очищает окно от виджетов и обращается к десятому вопросу'''
        clear()
        que10()

def que10():
    '''Отображает 10 вопрос и кнопки для ответа'''
    question = Label(root, text="Больше всего озер расположено в Канаде",font = ("KacstArt",30))
    btn1=Button(root,text="Правда",font = ("KacstArt",30), bg="OliveDrab2",fg="black",command=lambda:next_r(res))
    btn2=Button(root,text="Ложь",font = ("KacstArt",30), bg="red3",fg="black",command=lambda:next_w(res))
    question.pack()
    btn1.pack()
    btn2.pack()
    def next_r(res):
        '''Очищает окно от виджетов, вызывает функцию результат и увеличивает счетчик на 1'''
        global count
        count +=1
        clear()
        res()
    def next_w(res):
        '''Очищает окно от виджетов, вызывает функцию результат'''
        clear()
        res()

def res():
    ''' Отображает результат'''
    result = Label(root, text='Результат: '+ str(count) + ' из 10',font = ("KacstArt",30))
    if (count<=10) and (count>=8):
        description = "Поздравляем! Прекрасный результат!"
    elif (count<=7) and (count>=5):
        description = "Неплохо! Вы достаточно много знаете."
    elif (count<=4) and (count>=0):
        description = "Не расстраивайтесь! Вы можете попробовать ещё раз."
    result.pack()
    description=Label(root, text=str(description),font = ("KacstArt",30))
    description.pack()
    btn=Button(root,text="Начать заново",font = ("KacstArt",30),fg="black",command=lambda:repeat())
    btn.pack()

def repeat():
    '''Обнуляет счет, очищает экран и начинает тест заново'''
    global count
    count=0
    clear()
    que1()
que1()
root.mainloop()
