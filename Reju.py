# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:25:44 2019

@author: Aisha.Xu
""" 

"""this enables two human players to play against each other, with a justice algorithm"""

import tkinter as tk
import justice 


root = tk.Tk()
root.title('Renju')
root.geometry('700x700')


w = tk.Canvas(root,width=700,height=700,background='white')
#l = tk.Label(root,text='haha',bg = 'white',width = 100,height =50)
#l.pack(side = tk.TOP)

for num in range(1,18):
    w.create_line(num*40, 40, num*40, 680, width =2)
for num in range(1,18):
    w.create_line(40,num*40,680,num*40,width=2)

    
position_storage = {}
step_count = 0
def add_step_count():
    global step_count
    step_count += 1

def position_to_str(x,y):
    return str(x)+','+str(y)
    

        
def paint(event):
    if step_count%2 !=1:
        colour = "black"
        colour_number = 1
    else:
        colour = 'pink'
        colour_number = -1
    
    if event.x%40 < 20:
        x = (event.x//40)*40
    else:
        x = ((event.x//40)+1)*40
    
    if event.y%40 < 20:
        y = (event.y//40)*40
    else:
        y = ((event.y//40)+1)*40
    print(x,y)
    position_str = position_to_str(x,y)
    
    
    if position_str not in position_storage.keys():
        x1,y1=(x-10),(y-10)
        x2,y2 = (x+10),(y+10)
        w.create_oval(x1,y1,x2,y2,fill = colour)
        position_storage[position_str] = colour_number
        add_step_count()

    j = justice.rule(x,y,position_storage)
    result = j.justice()
    print(result)
    
    #result = justice(x,y,position_storage)
    if result != False:
        w.create_text(300,300,font = ('Arial',50),text = result)
        
        
w.pack()
w.bind("<Button-1>",paint)

root.mainloop()
print(position_storage)


