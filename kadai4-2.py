# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:32:46 2022

@author: Shoya
"""

import tkinter as tk
import time

class Cannon:

    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.setPos(x, y)
        
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+5*self.size,self.y+5*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_rectangle(self.x-5*self.size,self.y+5*self.size,self.x+10*self.size,self.y+10*self.size,outline=self.color,fill=self.color,width=0)
        

class CannonBall:

    bt = 100
    bb = 450
    bl = 0
    br = 600
    
    def __init__(self, x, y, vx, vy, color, size):
        self.size = size
        self.color = color
        self.setPos(x,y)
        self.setMovement(vx, vy)
        
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def setMovement(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def out(self):
        return (self.x < self.bl) | (self.x > self.br) | (self.y < self.bt) | (self.y - 40 > self.bb)
    
    def draw(self, canvas):
        canvas.create_oval(self.x,self.y,self.x+4*self.size,self.y+4*self.size,outline="black",fill="black",width=0)
        
    
def key_handler(event):
    key = event.keysym
    if(key == "Up"):
        cannonballs.append(CannonBall(cannon.x + 5, cannon.y - 40, 0, -5, "black",10))

root = tk.Tk()
root.geometry('600x600')
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)
root.bind("<KeyPress>", key_handler)
root.active = True

cannon = Cannon(10,"GREEN",275,500)
cannonballs = []

while(root.active):
    try:
        canvas.delete("all")
        cannon.draw(canvas)
        cannonballs_out = []
        for i in range(len(cannonballs)):
            cannonballs[i].move()
            if(cannonballs[i].out()):
                cannonballs_out.append(i)
                continue
            cannonballs[i].draw(canvas)
        for i in range(len(cannonballs_out)):
            cannonballs.pop(cannonballs_out[i])
        root.update()
        time.sleep(1/30)
    except Exception as e:
        print(str(e))
        break
