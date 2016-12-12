# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:09:28 2016

@author: adamjaku
"""
import tkinter
from tkinter import Frame, BOTH, Canvas

class Pong(Frame):
    
    canvas = 0
    winHEIGHT = 600;
    winWIDTH = 800;
 
    ball = 0
    paddle1 = 0
    paddle2 = 0
 
    player1Points = 0
    player2Points = 0
    textLabel = 0
    
    ballDX = 2
    ballDY = -2
    paddleSpeed = 30
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.title("Pong")
        self.initUI()
 
    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.ball = self.canvas.create_oval(400,400,410,410, fill="red")
        self.paddle1 = self.canvas.create_rectangle(0,0,10,50, fill="yellow")
        self.paddle2 = self.canvas.create_rectangle(780,0,790,50, fill="blue")
        self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
        self.canvas.pack(fill=BOTH, expand=1)
        self.doMove()
        self.parent.bind("<Key>", self.key)

        
    def key(self, event):
        if event.char == 'w':
            self.canvas.move(self.paddle1,0,-self.paddleSpeed)
        if event.char == 's':
            self.canvas.move(self.paddle1,0,self.paddleSpeed)
        if event.char == 'o':
            self.canvas.move(self.paddle2,0,-self.paddleSpeed)
        if event.char == 'l':
            self.canvas.move(self.paddle2,0,self.paddleSpeed)
            
    def doMove(self):
        self.canvas.move(self.ball,self.ballDX, self.ballDY)
        if self.canvas.coords(self.ball)[1] <= 0 or self.canvas.coords(self.ball)[3] >= self.winHEIGHT:
            self.ballDY = -self.ballDY
        if self.canvas.coords(self.ball)[0] <= 0 or self.canvas.coords(self.ball)[2] >= self.winWIDTH:
            if self.canvas.coords(self.ball)[0] <= 0:
                self.player2Points+=1
            else:
                self.player1Points+=1
            self.ballDX = -self.ballDX
            self.canvas.delete(self.textLabel)
            self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
            self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        if self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle1)) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle2)):
            self.ballDX = -self.ballDX
        self.after(10, self.doMove)
        
    def doCollide(self,coords1,coords2):
        height1 = coords1[3]-coords1[1]
        width1 = coords1[2]-coords1[0]
        height2 = coords2[3]-coords2[1]
        width2 = coords2[2]-coords2[0]
        return not (coords1[0] + width1 < coords2[0] or coords1[1] + height1 < coords2[1] or coords1[0] > coords2[0] + width2 or coords1[1] > coords2[1] + height2)
        
        

root = tkinter.Tk()
Pong(root)
root.geometry("800x600")
root.mainloop()