# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:11:33 2022

@author: Shoya
"""

import tkinter as tk

class Car:
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        
    def car_create(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+30*self.size,self.y+20*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_rectangle(self.x-30*self.size,self.y+20*self.size,self.x+60*self.size,self.y+40*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_oval(self.x-15*self.size,self.y+40*self.size,self.x+5*self.size,self.y+60*self.size,outline="black",fill="black",width=0)
        canvas.create_oval(self.x+25*self.size,self.y+40*self.size,self.x+45*self.size,self.y+60*self.size,outline="black",fill="black",width=0)
        
a = Car(30,30,1,"red")
b = Car(100,100,2,"blue")


root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

a.car_create(canvas)
b.car_create(canvas)

root.mainloop()

