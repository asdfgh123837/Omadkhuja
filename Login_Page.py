from tkinter import *
#Results will get using messagebox
from tkinter import messagebox

root = Tk()
root.title("Login Page")
root.geometry("500x400")

#Function
def submit():
  username = user_entry.get()
  password = pass_entry.get()
  return messagebox.showinfo("Your Data",
    f"Username: {username}\n Password: {password}")

#Let's create entry and text 
user_text = Label(root, text = "Username")
user_text.pack()
user_entry = Entry(root)
user_entry.pack()

#Password text and entry
#So, we will change password entry type to '*' this
pass_text = Label(root, text = "Password")
pass_text.pack()
pass_entry = Entry(root, show="*")
pass_entry.pack()

#And now we will write a code about button section
button = Button(root, text = "Submit", command=submit)
button.pack()

root.mainloop()