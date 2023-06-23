from tkinter import *
import tkinter.messagebox as messagebox

def register_data():
    import mysql.connector

    mydb = mysql.connector.connect(host='localhost',user='root',password="", database="new form")

    cur = mydb.cursor()

    username = l1_entry.get()
    age = l2_entry.get()
    email = l3_entry.get()
    password = l4_entry.get()


    cur.execute("insert into 1st values(%s,%s,%s,%s)",(username,age,email,password))
    mydb.commit()
    messagebox.showinfo("Registration","Registered Successfully")

root = Tk()
root.geometry("400x400")
root.title("Registration Form")

l1 = Label(root, text="Username:", font=("Arial", 15,))
l1.place(x=20, y=20)
l1_entry = Entry(root, font=("Arial", 15))
l1_entry.place(x=130, y=23)

l2 = Label(root, text="Age:", font=("Arial", 15))
l2.place(x=70, y=70)
l2_entry = Entry(root, font=("Arial", 15))
l2_entry.place(x=130, y=73)

l3 = Label(root, text="Email:", font=("Arial", 15))
l3.place(x=58, y=123)
l3_entry = Entry(root, font=("Arial", 15))
l3_entry.place(x=130, y=123)

l4 = Label(root, text="Password:", font=("Arial", 15))
l4.place(x=18, y=173)
l4_entry = Entry(root, show= ("*"), font=("Arial", 15))
l4_entry.place(x=130, y=173)

l5 = Button(root, text="Register", font=("Arial", 10), command=register_data)
l5.place(x=155, y=250)

root.mainloop()

