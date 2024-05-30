from tkinter import *
root=Tk()

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')

def close1():
    root.destroy()
    import Add_operatorD

def close2():
    root.destroy()
    import addbus_detail

def close3():
    root.destroy()
    import Bus_route_detail

def close4():
    root.destroy()
    import bus_runningdetail

frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/3.5,pady=20)

frame2=Frame(root)
frame2.grid(row=2)
Label(frame2,text="Online Bus Booking System",font="arial 18 bold",bg="light blue",fg="red").grid(row=2,column=1,padx=w/2.3,pady=h/50,columnspan=4)

frame3=Frame(root)
frame3.grid(row=3)
Label(frame3,text="Add New Detail to Database",font="arial 15 bold",fg="green").grid(row=3,column=1,padx=w/2.3,pady=h/50,columnspan=4)

frame4=Frame(root)
frame4.grid(row=4,pady=10)
Button(frame4,text="New Operator",bg="pale green",font="arial 15 bold",command=close1).grid(row=4,column=1,padx=30)
Button(frame4,text="New Bus",bg="firebrick2",font="arial 15 bold",command=close2).grid(row=4,column=2,padx=30)
Button(frame4,text="New Route",bg="DodgerBlue2",font="arial 15 bold",command=close3).grid(row=4,column=3,padx=30)
Button(frame4,text="New Run",bg="LightPink4",font="arial 15 bold",command=close4).grid(row=4,column=4,padx=30)



root.mainloop()
