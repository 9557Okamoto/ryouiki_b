# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:16:26 2022

@author: Shoya
"""

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_rectangle(100, 100, 500, 300, outline = "Black",fill = "Black", width = 5)


root.mainloop()