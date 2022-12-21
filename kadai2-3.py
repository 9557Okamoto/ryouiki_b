# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:12:01 2022

@author: Shoya
"""
import tkinter as tk


root = tk.Tk()
root.geometry("400x400")
canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

class Car:
    def __init__(self,x,y,size,color,tag):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.tag = tag
        
    def car_create(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+10*self.size,self.y+5*self.size,outline=self.color,fill=self.color,width=0,tag="tag{}".format(tag))
        canvas.create_rectangle(self.x-5*self.size,self.y+5*self.size,self.x+15*self.size,self.y+10*self.size,outline=self.color,fill=self.color,width=0,tag="tag{}".format(tag))
        canvas.create_oval(self.x-3*self.size,self.y+10*self.size,self.x+2*self.size,self.y+15*self.size,outline="black",fill="black",width=0,tag="tag{}".format(tag))
        canvas.create_oval(self.x+8*self.size,self.y+10*self.size,self.x+13*self.size,self.y+15*self.size,outline="black",fill="black",width=0,tag="tag{}".format(tag))


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
        
        tag = j*10+i
        a = Car(20+(i*30),20+(j*30),1,color,tag)
        a.car_create(canvas)

root.update()

while(True):
    number = input("10の位を行の番号，1の位を列の番号とし，削除したい番号(0~99)を入力してください >>")    
    try:
        if number == "quit":
            root.destroy()
            break
        if 0 <= int(number) <= 99:
            canvas.delete("tag{}".format(number))
            root.update()
        elif int(number) < 0 or 99 < int(number):
            print("0~99の数字を入力してください")
    except(Exception):
        print("error")