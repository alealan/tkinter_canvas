from tkinter import *
from random import random


class Tk_can:
    def __init__(self, master, width = 400, height = 400):

        self.can = Canvas(master, width = width, height = height, bg = 'black')
        self.can.pack()

        master.bind('<Motion>', lambda event, m = master: self.move(event, m))
        master.bind('<Return>', lambda event, w = width, h = height: self.move(event, w, m))

        self.start("", width, height)

    def move(self, event, master):
        x = event.x
        y = event.y
        master.title(f"{x}x{y}")

    def start(self, event, width, height):

        self.Sun(int(random() * int(self.can['width'])), width, height)

        self.createClouds(width, 80, 160, 50)
        self.createLand(width, height, 350)
        self.createGrass(width, 2, 352)
        self.createHouse(width, height, 190)

        self.createGrass(width, 11, 365)


    def Sun(self, loc, h, w):
        print(loc,h,w)
        self.can.create_rectangle(0 - 2, 2 - 2, w + 2, h + 2, fill="lightblue")

        self.can.create_oval(loc + 20, 0 + 20, loc - 20, 0 - 20, fill = 'yellow', outline = 'yellow', width = 1)

        for shine in range(180, 360, 10):
            self.can.create_arc(loc + 40, 0 + 40, loc - 40, 0 - 40, start=shine, extent=2, outline = 'yellow', style = 'arc',
                                width = 25)

    def createBall(self, x, y, r, c):
        self.can.create_oval(x + r, y + r, x - r, y - r, fill=c, outline=c)

    def createCloudsCh1(self, x, y, mass):
        for i in range(8):
            x += (random() * (mass * 2) - mass)
            y += random() * (mass) - (mass / 3)

            self.createBall(x, y, mass, "white")

    def createCloudsCh2(self, width, floor):
        for i in range(int(width * (-1)), int(width * 2), int(width / 5)):
            r = random() * 20 - 10  # -10 - 10
            m = random() * 2 - 4  # -4 - 1
            self.createCloudsCh1(i, floor + r, 20 + m)  # x,y,mass

    def createClouds(self, width, start, end, step):
        print(start, end, step)
        for i in range(start, end, step):
            print(i)
            self.createCloudsCh2(width, i)

    def createLand(self, widthF, heightF, height):
        self.can.create_rectangle(0 - 2, heightF + 2, widthF + 2, height, fill='lightgreen', width=0)

    def createRoof(self, x, y, height):
        hood = 20
        width = 150  # = x1-x2 from createHouse

        self.can.create_rectangle(x + width - 20, y - 5,
                                  x + width - 30, y - height - 10,
                                  width=0, fill='brown')

        self.can.create_polygon(x - hood, y,
                                x + 10, y - height,
                                x + width - 10, y - height,
                                x + width + hood, y)

    def createHouse(self, widthF, heightF, x):
        self.master = self.can

        x1 = x
        x2 = x1 + 150
        y1 = heightF - 40
        y2 = heightF - 100 - 40

        self.can.create_rectangle(x1, y1, x2, y2, fill='grey', width=0)

        for j in range(y1, y2, -4):
            for i in range(x1, x2, 10):
                self.can.create_rectangle(i, j - 3, i + 9, j, fill='brown', width=0)

        self.can.create_rectangle(x1 + 20, y1, x1 + 50, y1 - 60, fill='orange4', width=0)
        self.can.create_rectangle(x1 + 22, y1, x1 + 48, y1 - 58, fill='darkorange4', width=0)

        self.can.create_oval(x1 + 24, y1 - 30, x1 + 26, y1 - 32)

        self.createRoof(x1, y2 + 20, 30)

    def createPlant(self, height, x, y):
        w = height / 8
        self.can.create_polygon(x + 1 * w, y,
                                x, y - height / 3 * w,
                                x + 3 * w, y - height * w,
                                x + 1 * w, y - height / 4 * w,
                                x + 2 * w, y,
                                fill='darkgreen', width=0
                                )

    def createGrass(self, width, floors, y):
        stepx = 6
        stepy = 6
        n = 2

        for j in range(0, floors, 1):
            for i in range(-10 * width, width, stepx):
                self.createPlant(11, i + n, y + stepy * j)
            n += n


if __name__ == '__main__':
    root = Tk()
    e = Entry(root, width=20)
    b = Button(root, text="Преобразовать")
    l = Label(root, bg='black', fg='white', width=20)




    Tk_can(root)
    root.mainloop()