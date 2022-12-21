# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:11:51 2022

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
        canvas.create_rectangle(self.x,self.y,self.x+10*self.size,self.y+5*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_rectangle(self.x-5*self.size,self.y+5*self.size,self.x+15*self.size,self.y+10*self.size,outline=self.color,fill=self.color,width=0)
        canvas.create_oval(self.x-3*self.size,self.y+10*self.size,self.x+2*self.size,self.y+15*self.size,outline="black",fill="black",width=0)
        canvas.create_oval(self.x+8*self.size,self.y+10*self.size,self.x+13*self.size,self.y+15*self.size,outline="black",fill="black",width=0)
        


root = tk.Tk()
root.geometry("400x400")
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

for i in range(10):
    for j in range(10):
        if(i%2==0):
            if(j%2==0):
                color = "blue"
            else:
                color = "red"
        else:
            if(j%2==0):
                color = "red"
            else:
                color = "blue"

        a = Car(20+(i*30),20+(j*30),1,color)
        a.car_create(canvas)

root.mainloop()
