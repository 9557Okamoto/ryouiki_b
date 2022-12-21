# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:19:25 2022

@author: Shoya
"""

import tkinter as tk
import time

class Car:

    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.x = x
        self.y = y

    def setBorder(self, bleft, bright, btop, bbottom):
        self.bl = bleft
        self.br = bright
        self.bt = btop
        self.bb = bbottom

    def setMovement(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if((self.x -5*self.size < self.bl) | (self.x + self.size*15 > self.br)):
            self.vx *= -1
            self.x += self.vx*2
        if((self.y < self.bt) | (self.y + self.size > self.bb)):
            self.vy *= -1
            self.y += self.vy*2

    def draw(self, canvas):

        canvas.create_rectangle(self.x,self.y,self.x+10*self.size,self.y+5*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_rectangle(self.x-5*self.size,self.y+5*self.size,self.x+15*self.size,self.y+10*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_oval(self.x-3*self.size,self.y+10*self.size,self.x+2*self.size,self.y+15*self.size,outline="black",fill="black",width=0)
        canvas.create_oval(self.x+8*self.size,self.y+10*self.size,self.x+13*self.size,self.y+15*self.size,outline="black",fill="black",width=0)
        

root = tk.Tk()
root.geometry('600x400')
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)
root.active = True

car = Car(5, "BLUE",250,150)
car.setBorder(0, 600, 0, 400)
car.setMovement(5, 0)

while(root.active):
    try:
        canvas.delete("all")
        car.move()
        car.draw(canvas)
        root.update()
        time.sleep(1/60)
    except Exception as e:
        print(str(e))
        break