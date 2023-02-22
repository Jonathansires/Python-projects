
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
reps = 0
times = "Timer"
LONG_BREAK_MIN = 20
from tkinter import *
import math
timero = None
# ---------------------------- TIMER RESET ------------------------------- # 
import time
count="00:00"
def count_down(count):
    canvas.itemconfig(timer, text=count)
    if count > 0: 
        window.after(1000,count_down,count - 1)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_click():
    global reps
    
    reps += 1
    if reps % 8 == 0 :
        title_text.config(text="Break", fg= RED)
        count_down(600)
        reps-=8
    elif reps % 2 == 0:
        count_down(300)
        title_text.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(1200)
        title_text.config(text="WORK", fg=GREEN)
def reset_click():
    window.after_cancel(timero)
    title_text.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer, text='00:00')
    global reps
    reps=0
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count >0:
            global timero
            timero = window.after(1000, count_down, count-1)
    else:
        start_click()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer app")
window.minsize(width=400, height=400)
window.config(bg=YELLOW,padx=100,pady=50)

canvas=Canvas(height=220,width=224,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file=r"C:\Desktop\Python projects\25-30\25 min timer app\tomato.png")
canvas.create_image(120,85, image=tomato)


timer = canvas.create_text(120,120,text=count,font=(FONT,25))
canvas.grid(row=1,column=1)



title=times
title_text = Label(text = title, font=(FONT,35,'bold'))
title_text.grid(row = 0,column = 1, pady=10)
title_text['background']=YELLOW


start = Button(text="start", command=start_click)
start.grid(row = 3,column = 0, padx= 10)

reset = Button(text="reset", command=reset_click)
reset.grid(row = 3,column = 2,padx=10)


window.mainloop()