from tkinter import * 
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import json
baseemail = "Jonnysires@yahoo.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    passwordentry.delete(0,END) 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]   
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)  
    password = "".join(password_list)
    passwordentry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def success():
    webfile = web.get()
    emailuserfile = emailuser.get()
    passwordfile = passwordentry.get()
    new_data = {
        webfile: {
            'email': emailuserfile,
            'password': passwordfile,
        }
    }

    if len(webfile) == 0 or len(passwordfile) == 0:
        messagebox.showinfo(title= 'oops', message='yuour forgot to type retard')

    else:
        with open("passwords.json", 'r') as data_file:
            data = json.load(data_file)
            ye=data+new_data
            
        with open("passwords.json", 'w') as data_file:
            json.dump(ye,new_data,indent=4)
            

            web.delete(0,END)
            emailuser.delete(0,END)
            passwordentry.delete(0,END)
            web.focus()
            emailuser.insert(0,baseemail)

def search():
    with open("passwords.json", 'r') as save_file:
        json_search = load(save_file)
        print(json_search)
# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Timer app")
window.minsize(width=200, height=200)
window.config(padx=50,pady=50)
canvas=Canvas(height=200,width=200,highlightthickness=0)
tomato = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=tomato)
canvas.grid(row=0, column=1)

# buttons
button = Button(text="Generate Password", command=generate_password)
button.grid(row = 3,column = 2,padx= 3)

button3 = Button(text="Search", command=search)
button3.grid(row = 1,column = 2,padx= 3)

button2 = Button(width= 43,text="Add", command=success)
button2.grid(row = 4,column = 1,columnspan=2,pady=5)
# inputs
web = Entry(width=31)
web.grid(row = 1,column = 1,pady=5)
web.focus()

emailuser = Entry(width=50)
emailuser.grid(row = 2,column = 1, columnspan=2,pady=5)
emailuser.insert(0,baseemail)

passwordentry = Entry(width=31)
passwordentry.grid(row = 3,column = 1,pady=5)

# text

websitetxt = Label(text= "Website: ")
websitetxt.grid(row = 1, column = 0)

emailusertxt = Label(text= "Email/Username:")
emailusertxt.grid(row = 2, column = 0)

password = Label(text= "Password:")
password.grid(row = 3, column = 0)

window.mainloop()