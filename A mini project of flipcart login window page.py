from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()

    if(email=='vijaypjt@gmail.com' and password=='vijay@111'):
        messagebox.showinfo('yeah','login successful')
    else:
        messagebox.showerror('error','login failed')

root=Tk()                                               # for blank window

root.title('Login Form')
root.geometry("350x500")                                             # page size 
root.configure(background='blue')                          # page colour

# use flipcart text page

text_level=Label(root,text='Flipcart',fg='yellow',bg='#0096DC')
text_level.pack(pady=(20,5))                                           # pady()=text up-down 
text_level.config(font=('vardana',24))

# use enter email 

email_level=Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_level.pack(pady=(80,5))
email_level.config(font=('vardana',24))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

# use enter password 

password_level=Label(root,text='Enter Passwprd',fg='white',bg='#0096DC')
password_level.pack(pady=(20,5))
password_level.config(font=('vardana',24))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

# login_button

login_button=Button(root,text='Login Here',fg='black',bg='#0096DC',command=handle_login)
login_button.pack(pady=(20,5))
login_button.config(font=('vardana',24))

root.mainloop()                                               # for window hold on output screen