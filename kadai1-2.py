# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:26:42 2022

@author: Shoya
"""

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_rectangle(75, 100, 325, 200, outline = "Black",fill = "Black", width = 5)
canvas.create_rectangle(150, 50, 250, 100, outline = "Black",fill = "Black", width = 5)
canvas.create_oval(100, 200, 150, 250, outline = "Black",fill = "Black", width = 5)
canvas.create_oval(250, 200, 300, 250, outline = "Black",fill = "Black", width = 5)
canvas.create_text(75, 300, text = "Shoya Okamoto", font = ("",20), anchor = "nw", fill = "Black")

root.mainloop()