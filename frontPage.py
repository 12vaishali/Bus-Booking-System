from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def sb():
    root.destroy()
    import jourDetails

def cb():
    root.destroy()
    import check_booking

def bd():
    root.destroy()
    import bus_detail

bus=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.3)

frame2=Frame(root)
frame2.grid(row=2)
Label(frame2,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=1)

frame3=Frame(root)
frame3.grid(row=3,pady=45)
Button(frame3,text="SEAT BOOKING",font="arial 12 bold",bg="pale green",command=sb).grid(row=3,column=1,padx=50)
Button(frame3,text="Check Booking Seat",font="arial 12 bold",bg="green3",command=cb).grid(row=3,column=2,padx=50)
Button(frame3,text="Add Bus Details",font="arial 12 bold",bg="forest green",command=bd).grid(row=3,column=3,padx=50)

frame4=Frame(root)
frame4.grid(row=4)
Label(frame4,text="For Admin Only",font="arial 12 bold",fg="red").grid(row=4,column=1,padx=w/3)

root.mainloop()
