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
    rid=Route_id.get()
    sname=startStation_name.get()
    sid=startStation_id.get()
    ename=endStation_name.get()
    eid=endStation_id.get()
    cur.execute('select r_id from route')
    res=cur.fetchall()
    if (rid,) in res:
        showerror('ERROR',"Route id already exists")
    else:
        sname=sname.lower()
        ename=ename.lower()
        cur.execute('insert into route(r_id,s_name,s_id,e_name,e_id) values(?,?,?,?,?)',(rid,sname,sid,ename,eid))
        con.commit()
        showinfo('added',"sucessfully added route")
bus=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.7)

frame2=Frame(root)
frame2.grid(row=2)
Label(frame2,text=" Online Bus Booking System ",font="arial 22 bold",bg="light blue",fg="red").grid(row=2,column=1,padx=w/2.7)

frame3=Frame(root)
frame3.grid(row=3)
Label(frame3,text="Add Bus Route Detail",font="arial 15 bold",fg="green").grid(row=3,column=1,padx=w/2.3,pady=h/50,columnspan=10)

frame4=Frame(root)
frame4.grid(row=4,pady=30)
Label(frame4,text="Route Id").grid(row=4,column=1,padx=5)
Route_id=Entry(frame4)
Route_id.grid(row=4,column=2,padx=5)
Label(frame4,text="Station Name").grid(row=4,column=3,padx=5)
startStation_name=Entry(frame4)
startStation_name.grid(row=4,column=4,padx=5)
Label(frame4,text="Station id").grid(row=4,column=5,padx=5)
startStation_id=Entry(frame4)
startStation_id.grid(row=4,column=6,padx=5)

Button(frame4,text="Add Route",font="arial 10 bold",bg="pale green",command=add).grid(row=4,column=7,padx=10)
Button(frame4,text="Delete Route",font="arial 10 bold",fg="red",bg="pale green").grid(row=4,column=8,padx=10)

frame5=Frame(root)
frame5.grid(row=5)
Label(frame5,text="End Station Name").grid(row=5,column=3,padx=5)
endStation_name=Entry(frame5)
endStation_name.grid(row=5,column=4,padx=5)
Label(frame5,text=" End Station id").grid(row=5,column=5,padx=5)
endStation_id=Entry(frame5)
endStation_id.grid(row=5,column=6,padx=5)


frame6=Frame(root)
frame6.grid(row=6)
home=PhotoImage(file='.\\home.png')
Button(frame6,image=home,command=hom).grid(row=6,column=9,padx=30)

cur.execute('select * from route')
res=cur.fetchall()
print(res)



root.mainloop()
