from tkinter import *
import time
import random

tk = Tk()
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)
tk.title("Ball Game")
canvas = Canvas(tk, height = 400, width = 500, bd=0, highlightthickness=0, bg='skyblue')
canvas.pack()
tk.update()
counter = 0
score = canvas.create_text(30, 10, text=f"Score: {counter}", font=('arial', 10), fill='black' )

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.id = self.canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 233,190)
        self.canvas.create_line(250,0,250,500, fill='blue')
        start = [-3,-2,-1,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hitBottom = False
        
    def hitPaddle1(self, pos):
        paddlePos = self.canvas.coords(self.paddle1.id)
        if pos[3]>=paddlePos[1] and pos[1]<=paddlePos[3]:
            if pos[0]>=paddlePos[0] and pos[0]<=paddlePos[2]:
                return True
        return False
        
    def hitPaddle2(self, pos):
        paddlePos = self.canvas.coords(self.paddle2.id)
        if pos[3]>=paddlePos[1] and pos[1]<=paddlePos[3]:
            if pos[2]<=paddlePos[2] and pos[2]>=paddlePos[0]:
                return True
        return False
        
    def draw(self):
        global counter
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.hitBottom = True
            self.x=0
            self.y=0
            self.canvas.create_text(250, 200, text='GAME OVER', fill='red')
        if pos[2]>=self.canvas_width:
            self.hitBottom = True
            self.x=0
            self.y=0
            self.canvas.create_text(250, 200, text='GAME OVER', fill='red')
        if self.hitPaddle1(pos)==True:
            self.x=3
            counter+=1
            self.updateScore()
        if self.hitPaddle2(pos)==True:
            self.x=-3
            counter+=1
            self.updateScore()
            
    def updateScore(self):
        canvas.itemconfig(score, text=f"Score: {counter}")
            
class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0,150, 12,250, fill=color)
        self.x=0
        self.y=0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.moveUp)
        self.canvas.bind_all('d', self.moveDown)
        self.canvas.bind_all('<KeyRelease-a>', self.stop)
        self.canvas.bind_all('<KeyRelease-d>', self.stop)
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.canvas.move(self.id, 0, -pos[1])
        if pos[3]>=self.canvas_height:
            self.canvas.move(self.id, 0, self.canvas_height-pos[3])
        
    def moveUp(self, event):
        self.y=-3
    def moveDown(self, event):
        self.y=3
    def stop(self, event):
        self.y = 0

class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(489,150,500,250, fill=color)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.moveUp)
        self.canvas.bind_all('<KeyPress-Right>', self.moveDown)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)
               
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.canvas.move(self.id, 0, -pos[1])
        if pos[3]>=self.canvas_height:
            self.canvas.move(self.id, 0, self.canvas_height-pos[3])
              
    def moveUp(self, event):
        self.y=-3
    def moveDown(self, event):
        self.y=3
    def stop(self, event):
        self.y=0
               
paddle1 = Paddle1(canvas, 'hotpink')
paddle2 = Paddle2(canvas, 'hotpink')
ball = Ball(canvas, paddle1, paddle2, 'pink')

while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
