from tkinter import *

window = Tk()
window.title("Miles to Km Coverter")
window.minsize(width=300, height=200)


text = Label(text= "is equal to")
text.grid(row = 1, column = 0)

text2 = Label(text= "Km")
text2.grid(row = 1, column = 2)


answer = 0
def button_click():
    yes = float(input.get())
    answer = yes *1.609
    text3.config(text = answer)
    

button = Button(text="Click", command=button_click)
button.grid(row = 3,column = 1)
input = Entry()
input.grid(row = 0,column = 1)

text3 = Label(text= 0)
text3.grid(row = 1, column = 1)



window.mainloop()