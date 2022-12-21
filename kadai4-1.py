# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:32:46 2022

@author: Shoya
"""

import tkinter as tk
import time

class Cannon:

    def __init__(self, size, color):
        self.size = size
        self.color = color
        
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+5*self.size,self.y+5*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_rectangle(self.x-5*self.size,self.y+5*self.size,self.x+10*self.size,self.y+10*self.size,outline=self.color,fill=self.color,width=0)
        

class CannonBall:

    def __init__(self, size, color):
        self.size = size
        self.color = color
        
    def setPos(self, x, y):
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

    def draw(self, canvas):
        canvas.create_oval(self.x,self.y,self.x+4*self.size,self.y+4*self.size,outline="black",fill="black",width=0)
        



root = tk.Tk()
root.geometry('600x600')
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)
root.active = True

cannon = Cannon(10,"GREEN")
cannon.setPos(275, 500)


cannonball = CannonBall(10,"BLACK")
cannonball.setPos(280, 460)
cannonball.setBorder(0, 600, 100, 450)
cannonball.setMovement(0, -5)

while(root.active):
    if(cannonball.bt > cannonball.y):
        cannonball.setPos(280,460)
    try:
        canvas.delete("all")
        cannon.draw(canvas)
        cannonball.move()
        cannonball.draw(canvas)
        root.update()
        time.sleep(1/30)
    except Exception as e:
        print(str(e))
        break
