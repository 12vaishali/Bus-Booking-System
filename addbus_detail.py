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

def add():
    bid=bus_id.get()
    bt=bus_type.get()
    c=capacity.get()
    f=Fare.get()
    oid=o_id.get()
    rid=r_id.get()
    cur.execute('select bus_id from bus')
    res=cur.fetchall()
    if (bid,) in res:
        showerror("error","bus id already exists!!!")
    else:
        data="bus_id="+bid+"     bus_type="+bt+"     capacity="+c+"     fare="+f+"     op_id="+oid+"     route_id="+rid
        cur.execute('insert into bus(bus_id,bus_type,capacity,fair,op_id,route_id) values(?,?,?,?,?,?)',(bid,bt,c,f,oid,rid))
        con.commit()
        showinfo('added', "bus detail has added succesfully")
        Label(root,text=data).grid(row=6,columnspan=12)
    con.commit()
frame1=Frame(root)
frame1.grid(row=1)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.3,pady=h/50,columnspan=15)

frame2=Frame(root)
frame2.grid(row=2)
Label(frame2,text="Online Bus Booking System",font="arial 18 bold",bg="light blue",fg="red").grid(row=2,column=1,padx=w/2.3,pady=h/50,columnspan=15)

frame3=Frame(root)
frame3.grid(row=3,pady=10)
Label(frame3,text="Add Bus Detail",font="arial 15 bold",fg="green").grid(row=3,column=1,padx=w/2.3,pady=h/50,columnspan=15)

frame4=Frame(root)
frame4.grid(row=4)
Label(frame4,text="BusID").grid(row=4,column=1)
bus_id=Entry(frame4)
bus_id.grid(row=4,column=2)

bus_type=StringVar()
bus_type.set("Bus Type")
option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non AC-Sleeper 2x1"]
menu=OptionMenu(frame4,bus_type,*option)
menu.grid(row=4,column=4)

Label(frame4,text="Capacity").grid(row=4,column=5)
capacity=Entry(frame4)
capacity.grid(row=4,column=6)
Label(frame4,text="Fare Rs").grid(row=4,column=7)
Fare=Entry(frame4)
Fare.grid(row=4,column=8)
Label(frame4,text="Operator ID").grid(row=4,column=9)
o_id=Entry(frame4)
o_id.grid(row=4,column=10)
Label(frame4,text="Route ID").grid(row=4,column=11)
r_id=Entry(frame4)
r_id.grid(row=4,column=12)


frame5=Frame(root)
frame5.grid(row=5,pady=h/20)
Button(frame5,text="Add Bus",bg="pale green",command=add).grid(row=5,column=7,padx=30)
Button(frame5,text="Edit Bus",bg="pale green").grid(row=5,column=8,padx=20)
home=PhotoImage(file='.\\home.png')


Button(frame5,image=home,command=hom).grid(row=5,column=9,padx=30)
##cur.execute('select * from bus')
##res=cur.fetchall()
##print(res)

root.mainloop()
