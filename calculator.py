from tkinter import *

class Calc:
    def __init__(self, master):
        self.plus = Button(master, text='+')
        self.sub = Button(master, text='-')
        self.div = Button(master, text='/')
        self.mult = Button(master, text='*')
        self.label = Label(master, width=15, fg='black', bg='white')
        self.enter = Entry(width=20)
        self.enter_2 = Entry(width=20)

        self.plus['command'] = self.sum1
        self.sub['command'] = self.sub1
        self.div['command'] = self.div1
        self.mult['command'] = self.mult1

        self.enter.pack()
        self.enter_2.pack()

        self.plus.pack()
        self.sub.pack()
        self.div.pack()
        self.mult.pack()

        self.label.pack()

    def sum1(self):
        a = float(self.enter.get()) + float(self.enter_2.get())
        self.label['text'] = a

    def div1(self):
        x1 = self.enter.get()
        x2 = self.enter_2.get()
        self.label['text'] = str(float(x1) / float(x2))

    def sub1(self):
        x1 = self.enter.get()
        x2 = self.enter_2.get()
        self.label['text'] = float(x1) - float(x2)

    def mult1(self):
        x1 = self.enter.get()
        x2 = self.enter_2.get()
        self.label['text'] = float(x1) * float(x2)


root = Tk()
Calc(root)
root.title('Калькулятор')
root.mainloop()
