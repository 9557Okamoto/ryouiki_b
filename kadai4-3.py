# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:18:23 2022

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

    bt = 0
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

class Car:

    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.setPos(x, y)
        #self.x = x
        #self.y = y
        
    def setPos(self,x,y):
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
            
    def hit(self,cx,cy,csize):
        if(self.x - 5*self.size < cx + 4*csize):
            if(self.x + 15*self.size > cx):
                if(self.y + 10*self.size > cy):
                    if(self.y < cy + 4*csize):
                        return True
        return False
                

    def draw(self, canvas):

        canvas.create_rectangle(self.x,self.y,self.x+10*self.size,self.y+5*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_rectangle(self.x-5*self.size,self.y+5*self.size,self.x+15*self.size,self.y+10*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_oval(self.x-3*self.size,self.y+10*self.size,self.x+2*self.size,self.y+15*self.size,outline="black",fill="black",width=0)
        canvas.create_oval(self.x+8*self.size,self.y+10*self.size,self.x+13*self.size,self.y+15*self.size,outline="black",fill="black",width=0)        
    
def key_handler(event):
    key = event.keysym
    if(key == "Up"):
        cannonballs.append(CannonBall(cannon.x + 15, cannon.y - 40, 0, -10, "black",5))

root = tk.Tk()
root.geometry('600x600')
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)
root.bind("<KeyPress>", key_handler)
root.active = True

car = Car(3, "BLUE",50,50)
car.setBorder(0, 600, 0, 400)
car.setMovement(10, 0)
cannon = Cannon(10,"GREEN",275,500)
cannonballs = []

while(root.active):
    try:
        canvas.delete("all")
        car.move()
        car.draw(canvas)
        cannon.draw(canvas)
        cannonballs_out = []
        for i in range(len(cannonballs)):
            cannonballs[i].move()
            if(cannonballs[i].out()):
                cannonballs_out.append(i)
                continue
            if(car.hit(cannonballs[i].x,cannonballs[i].y,cannonballs[i].size)):
                car.setPos(50,50)
            cannonballs[i].draw(canvas)
        for i in range(len(cannonballs_out)):
            cannonballs.pop(cannonballs_out[i])
        root.update()
        time.sleep(1/30)
    except Exception as e:
        print(str(e))
        break