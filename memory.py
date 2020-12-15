from tkinter import *
from random import *
import time

window = Tk()
window["bg"] = 'gray22'

WIDTH = 600
HEIGHT = 600
window.config(width=WIDTH,height=WIDTH)

cake = PhotoImage(file='choco_cake.png')
eclaire = PhotoImage(file='eclaire.png')
coffee = PhotoImage(file='coffee.png')
cookies = PhotoImage(file='cookies.png')
macarons = PhotoImage(file='macarons.png')
tartalette = PhotoImage(file='tartalette.png')
muffin = PhotoImage(file='muffin.png')
croissant = PhotoImage(file='croissant.png')
square = PhotoImage(file='brown_square.png')

SIZE = 4
time_given = 100
max_tries = 10

symbols = ['1','2','3','4','5','6','7','8']
colors = ['white']*8
photos = [cake,eclaire,coffee,cookies,macarons,tartalette,muffin,croissant]
t1 = time.time()

cells = []
btns = []
amount = [i for i in range(1,SIZE**2+1)]
btn_x = 0
btn_y = 0
opened = 0
prev_number1 = 0
prev_value1 = ''
prev_number2 = 0
prev_value2 = ''
tries = 0
time_color = 'green'


class Cell():
    def __init__(self):
        self.value = ''
        self.color = ''
        self.appearance = ''
        self.closed = 1
        
for i in range(SIZE**2+1):
    a = Cell()
    cells.append(a)

done = 0
def set_field():
    global done
    for i in range(8):
        a = sample(amount,2)
        for j in a:
            amount.remove(j)
            cells[j-1].value = symbols[done]
            cells[j-1].color = colors[done]
            cells[j-1].appearance = done
        done+=1
            

def change_time():
    global t1,t2,time_color,tries,max_tries,time_left
    t2 = time.time()
    time_left = round(time_given-(t2-t1))
    time_spent = Label(window,text = str(time_left)+' seconds left',fg=time_color,font='Arial 10')
    time_spent.place(x=0,y=0,width=WIDTH/SIZE,height=25)   
    window.after(1000,change_time)
    if time_left<=time_given*2/3:
        time_color = 'brown'
        if time_left<=time_given*1/3:
            time_color = 'red'
    if time_left<0:
        lose(0)
        if time_left<-4:
            exit(0)
            
    tries_left = max_tries-tries
    tries_spent = Label(window,text = str(tries_left)+' tries left',fg=time_color,font='Arial 10')
    tries_spent.place(x=WIDTH-WIDTH/SIZE,y=0,width=WIDTH/SIZE,height=25)

def lose(a):
    for i in range(200):
        a = Label(window,text=['loser','you lost','ha-ha','hahaha','HAHAHA'][randint(0,4)],fg='red',font='Arial 15')
        a.place(height=randint(40,60),width=randint(70,100),x=randint(-20,650),y=randint(-20,690))
        a.number = 1
            
def win():
    global btns,t1
    t1 = 10000
    tries = -10000

def click(event):
    global opened,prev_number1,prev_value1,prev_number2,prev_value2,tries
    number = event.widget.number-1
    if cells[number].closed and prev_number1!=number:
        event.widget["image"] = photos[cells[number].appearance]
        opened+=1
        if opened==1:
            prev_value1 = cells[number].value
            prev_number1 = number
        elif opened==2:
            if cells[number].value!=prev_value1 or prev_number1==number:
                prev_value2 = cells[number].value
                prev_number2 = number
            elif cells[number].value==prev_value1:
                cells[number].closed = 0
                cells[prev_number1].closed = 0
                g = 0
                for i in cells:
                    if i.closed==0:
                        g+=1
                if g==SIZE**2:
                    win()
                prev_number1 = -1
                prev_value1 = ''
                prev_number2 = -1
                prev_value2 = ''
                opened = 0
        elif opened==3:
            btns[prev_number1]["image"] = square
            btns[prev_number2]["image"] = square
            opened = 1
            prev_number1 = -1
            prev_value1 = ''
            prev_number2 = -1
            prev_value2 = ''
            
            prev_value1 = cells[number].value
            prev_number1 = number
            
            tries+=1
            if tries>=max_tries:
                lose(0)
    
window.bind("<Button-1>",click)

set_field()

for i in range(1,SIZE**2+1):
    btn = Button(window,text=' ',font='Arial 15',bg='white',image=square)
    btn.number = i
    btn.place(width=WIDTH//SIZE,height=HEIGHT//SIZE,x=btn_x,y=btn_y)
    btns.append(btn)

    if btn_x==WIDTH-(WIDTH//SIZE):
        btn_x = 0
        btn_y += HEIGHT//SIZE
    else:
        btn_x += WIDTH//SIZE

        
window.after(1000,change_time())

window.mainloop()