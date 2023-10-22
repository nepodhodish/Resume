# -*- coding: utf-8 -*-

import tkinter as tk
import random as r
import math as m

okno = tk.Tk()
okno.title('Самолет')
okno.geometry('1200x600+50+30')
okno.configure(bg="yellow")
'''
okno.resizable(False,False)
'''
nebo = tk.PhotoImage(file='bg.gif')

win = ''
point = 0
a = 0
b = 0
cort = tk.Canvas(okno)
cort.place(width=1200, height=600)
cort.create_image(400, 300, image=nebo)
cort.create_image(800, 300, image=nebo)
Itog = cort.create_text(600, 300, text=win, font="Arial 30")


class Item:
    def __init__(self, x, y, xx, img):
        self.x = x
        self.y = y
        self.xx = xx
        self.img = tk.PhotoImage(file=img)
        self.item = cort.create_image(self.x, self.y, image=self.img)

    def draw(self):
        cort.coords(self.item, self.x, self.y)


class Cloud(Item):
    def __init__(self, x, y, xx, img):
        super().__init__(x, y, xx, img)


class Myplane(Item):
    def __init__(self, x, y, xx, yy, img):
        super().__init__(x, y, xx, img)
        self.yy = yy


class Fire(Item):
    def __init__(self, x, y, xx, img):
        super().__init__(x, y, xx, img)


class NotMyPlane(Item):
    def __init__(self, x, y, xx, img, health, shoot, radius, speed, wait):
        super().__init__(x, y, xx, img)
        self.health = health
        self.healths = []
        if (self.health > 1):
            self.helx = self.x - 50
            self.helxx = 100 / self.health
            for i in range(self.health):
                self.healths.append(
                    cort.create_rectangle(self.helx, self.y - 74, self.helx + self.helxx, self.y - 64, fill='red'))
                self.helx += self.helxx
        self.shoot = shoot
        self.firesen = []
        self.waiter = 0
        if (self.shoot == True):
            self.radius = radius
            self.speed = speed
            self.wait = wait

    def draw(self):
        cort.coords(self.item, self.x, self.y)
        if (len(self.healths) >= 1):
            self.helx = self.x - 50
            for i in range(len(self.healths)):
                cort.coords(self.healths[i], self.helx, self.y - 74, self.helx + self.helxx, self.y - 64)
                self.helx += self.helxx


class Nmfire(Item):
    def __init__(self, x, y, xx, img):
        super().__init__(x, y, xx, img)


clouds = []
for i in range(r.randint(5, 50)):
    clouds.append(Cloud(r.randint(-64, 1264), r.randint(0, 600), r.randint(1, 15), 'cloud.gif'))

mx = 0
my = 0
mplane = Myplane(140, 300, 0, 0, "plane.gif")


def MEven(event):
    global mx
    global my
    mx = event.x
    my = event.y


cort.bind("<Motion>", MEven)

fires = []


def Bul(event):
    fires.append(Fire(mplane.x + 95, mplane.y, 5, 'bullet.gif'))


cort.bind("<Button-1>", Bul)

nmplane = []


def Time():
    global mx
    global my
    global win
    global point
    global a
    cort.coords(Itog, -500, -500)

    for i in range(len(clouds)):
        clouds[i].x -= clouds[i].xx
        if (clouds[i].x <= -64):
            clouds[i].x = 1264
        clouds[i].draw()

    mplane.x += (mx - mplane.x) / 20
    mplane.y += (my - mplane.y) / 20
    mplane.draw()

    for i in range(len(fires) - 1, -1, -1):
        fires[i].x += fires[i].xx
        fires[i].draw()
        if (fires[i].x - 34 >= 1200):
            cort.delete(fires[i].item)
            del fires[i]
        else:
            for o in range(len(nmplane) - 1, -1, -1):
                if (fires[i].x + 34 >= nmplane[o].x - 66 and fires[i].x - 34 <= nmplane[o].x + 66 and nmplane[
                    o].y - 59 <= fires[i].y <= nmplane[o].y + 59):
                    if (len(nmplane[o].healths) > 1):
                        cort.delete(nmplane[o].healths[-1])
                        del nmplane[o].healths[-1]
                        nmplane[o].health -= 1
                        cort.delete(fires[i].item)
                        del fires[i]
                    else:
                        if (len(nmplane[o].healths) == 0):
                            cort.delete(fires[i].item)
                            del fires[i]
                            cort.delete(nmplane[o].item)
                            del nmplane[o]
                        else:
                            cort.delete(nmplane[o].healths[-1])
                            del nmplane[o].healths[-1]
                            cort.delete(fires[i].item)
                            del fires[i]
                            cort.delete(nmplane[o].item)
                            del nmplane[o]
                    break

    for i in range(len(nmplane) - 1, -1, -1):
        nmplane[i].x -= nmplane[i].xx
        nmplane[i].draw()
        nmplane[i].waiter += 1
        if (nmplane[i].shoot == True and nmplane[i].y - nmplane[i].radius < mplane.y < nmplane[i].y + nmplane[
            i].radius and nmplane[i].x - 66 >= mplane.x and nmplane[i].waiter >= nmplane[i].wait):
            nmplane[i].firesen.append(Nmfire(nmplane[i].x - 95, nmplane[i].y, nmplane[i].speed, 'bulleten.gif'))
            nmplane[i].waiter = 0
        for o in range(len(nmplane[i].firesen) - 1, -1, -1):
            nmplane[i].firesen[o].x -= nmplane[i].firesen[o].xx
            nmplane[i].firesen[o].draw()
            if (nmplane[i].firesen[o].x + 34 <= 0):
                cort.delete(nmplane[i].firesen[o].item)
                del nmplane[i].firesen[o]
            elif (nmplane[i].firesen[o].x - 34 <= mplane.x + 66 and nmplane[i].firesen[
                o].x + 34 >= mplane.x - 66 and mplane.y - 57 <= nmplane[i].firesen[o].y <= mplane.y + 57):
                point += 1
                a += 1
                break
            if (len(fires) > 0 and len(nmplane[i].firesen) > 0):
                for p in range(len(fires) - 1, -1, -1):
                    if (nmplane[i].firesen[o].x - 34 <= fires[p].x + 34 and nmplane[i].firesen[o].x + 34 >= fires[
                        p].x - 34 and fires[p].y - 8 <= nmplane[i].firesen[o].y <= fires[p].y + 8):
                        cort.delete(nmplane[i].firesen[o].item)
                        del nmplane[i].firesen[o]
                        cort.delete(fires[p].item)
                        del fires[p]
                        break
            if (a == 1):
                break
        if (nmplane[i].x + 70 <= 0):
            point += 1
            a += 1
            break
        elif (m.sqrt(m.pow(nmplane[i].x - mplane.x, 2) + m.pow(nmplane[i].y - mplane.y, 2)) < 120):
            point += 1
            a += 1
            break

    if (len(nmplane) == 0):
        a += 1
    if (a == 1):
        game()
    elif (a == 0):
        okno.after(16, Time)


def game():
    global point
    global win
    global a
    global b
    if (point == 0):
        b += 1
        okno.title('Самолет, раунд ' + str(b))
        for i in range(r.randint(1, b)):
            nmplane.append(
                NotMyPlane(r.randint(1470, 1600), r.randint(60, 540), r.randint(1, 5), "enemy.gif", r.randint(1, 2),
                           False, 0, 0, 0))
        for i in range(r.randint(1, b)):
            nmplane.append(
                NotMyPlane(r.randint(1370, 1500), r.randint(60, 540), r.randint(1, 3), "enemy.gif", r.randint(1, b),
                           False, 0, 0, 0))
        for i in range(r.randint(1, b)):
            nmplane.append(
                NotMyPlane(r.randint(1370, 1500), r.randint(60, 540), r.randint(1, 3), "enemy.gif", r.randint(1, b),
                           True, 10 + b * 3, r.randint(1, b), 70 - b))
        a = 0
        Time()
    elif (point == 1):
        win = 'Ты проиграл!'
        for i in range(len(clouds) - 1, -1, -1):
            cort.delete(clouds[i].item)
            del clouds[i]
        for i in range(len(nmplane) - 1, -1, -1):
            if (len(nmplane[i].healths) > 0):
                for o in range(len(nmplane[i].healths)):
                    cort.delete(nmplane[i].healths[-1])
                    del nmplane[i].healths[-1]
            cort.delete(nmplane[i].item)
            del nmplane[i]
        for i in range(len(fires) - 1, -1, -1):
            cort.delete(fires[i].item)
            del fires[i]
        cort.delete(mplane.item)
        cort.itemconfigure(Itog, text=win)
        cort.coords(Itog, 600, 300)


def Start(event):
    start.destroy()
    game()


start = tk.Button(text="Начнём?", font="Arial 30")
start.place(x=400, y=250, width=400, height=100)
start.bind("<Button>", Start)

okno.mainloop()
