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
Label(frame1,image=bus).grid(row=1,column=1,padx=w/3)

frame2=Frame(root)
frame2.grid(row=2,pady=10)
Label(frame2,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=1,padx=w/2.3,pady=h/50,columnspan=20)

frame3=Frame(root)
frame3.grid(row=3,pady=10)
Label(frame3,text="Add Bus Operator Detail",font="arial 15 bold",fg="green").grid(row=3,column=1,padx=w/2.3)

frame4=Frame(root)
frame4.grid(row=4,pady=10)
Label(frame4,text="Operator id").grid(row=4,column=1)
Op_id=Entry(frame4)
Op_id.grid(row=4,column=2)


Label(frame4,text="Name").grid(row=4,column=3)
Name=Entry(frame4)
Name.grid(row=4,column=4)


Label(frame4,text="Address").grid(row=4,column=5)
Address=Entry(frame4)
Address.grid(row=4,column=6)


Label(frame4,text="Phone").grid(row=4,column=7)
Phone=Entry(frame4)
Phone.grid(row=4,column=8)


Label(frame4,text="Email").grid(row=4,column=9)
Email=Entry(frame4)
Email.grid(row=4,column=10)

def done():
    oid=Op_id.get()
    n=Name.get()
    a=Address.get()
    p=Phone.get()
    em=Email.get()
    cur.execute('select opr_id from operator')
    res=cur.fetchall()
    if len(oid) > 0 and len(oid) <= 5 and oid.isnumeric():
        if  len(n) < 20 and len(n):
            if len(a) < 50 and len(a) > 0:
                if p.isnumeric() and len(p) == 10:
                    if len(em) > 0 and len(em) < 30:
                        if (oid,) in res:
                            showerror("ERROR","operator id already exists!!")
                        else:
                            cur.execute('insert into operator (opr_id,name,address,phone,email)values(?,?,?,?,?)',(oid, n, a, p, em))
                            con.commit()
                            showinfo('success', "operator added successfully!!")
                    else:
                        showerror("invalid input", "enter email correctly")
                else:
                    showerror("invalid input", "enter phone correctly")
            else:
                showerror("invalid input", "enter address correctly")
        else:
            showerror("invalid input", "enter name correctly")
    else:
         showerror("invalid input", "enter id correctly")
                
    con.commit()
    Label(frame5,text=oid+n+a+p+em).grid(row=5,column=1)
def edit():
    showinfo('operator entry update','operator record updated succesfully')

Button(frame4,text="Add",bg="pale green",command=done).grid(row=4,column=11,padx=10)
Button(frame4,text="Edit",bg="pale green",command=edit).grid(row=4,column=12,padx=10)

frame5=Frame(root)
frame5.grid(row=5)

frame6=Frame(root)
frame6.grid(row=6)
home=PhotoImage(file='.\\home.png')
Button(frame6,image=home,command=hom).grid(row=6,column=1)

##cur.execute("select * from operator")
##res=cur.fetchall()
##print(res)

root.mainloop()
