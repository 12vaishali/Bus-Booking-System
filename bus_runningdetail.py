from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection("bus_db")
cur=con.cursor()
root=Tk()

def hom():
    root.destroy()
    import frontPage

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.7)

frame2=Frame(root)
frame2.grid(row=2)
Label(frame2,text=" Online Bus Booking System ",font="arial 22 bold",bg="light blue",fg="red").grid(row=2,column=1,padx=w/2.7)

frame3=Frame(root)
frame3.grid(row=3)
Label(frame3,text="Add Bus Running Detail",font="arial 15 bold",fg="green").grid(row=3,column=1,padx=w/2.3,pady=h/50,columnspan=10)

frame4=Frame(root)
frame4.grid(row=4)
Label(frame4,text="Bus ID").grid(row=4,column=1,padx=5)
bus_id=Entry(frame4)
bus_id.grid(row=4,column=2,padx=5)
Label(frame4,text="Running Date").grid(row=4,column=3,padx=5)
Running_Date=Entry(frame4)
Running_Date.grid(row=4,column=4,padx=5)
Label(frame4,text="Seat Available").grid(row=4,column=5,padx=5)
Seat_Available=Entry(frame4)
Seat_Available.grid(row=4,column=6,padx=5)

def add():
    bid=bus_id.get()
    date=Running_Date.get()
    seat=Seat_Available.get()
    cur.execute('insert into running(b_id,run_date,seat_avail) values (?,?,?)',(bid,date,seat))
    con.commit()
    showinfo('Added','Done')
def delete():
    showinfo('Delete','Done')

Button(frame4,text="Add Run",bg="pale green",font="arial 10 bold",command=add).grid(row=4,column=7,padx=5)
Button(frame4,text="Delete Run",bg="pale green",font="arial 10 bold",command=delete).grid(row=4,column=8,padx=5)

frame5=Frame(root)
frame5.grid(row=5,pady=10)
home=PhotoImage(file='.\\home.png')
Button(frame5,image=home,command=hom).grid(row=5,column=1)

cur.execute('select * from running')
res=cur.fetchall()
print(res)

root.mainloop()
