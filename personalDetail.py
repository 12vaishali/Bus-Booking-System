from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def close(e=1):
    root.destroy()
    import frontPage

bus=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.3)

frame2=Frame(root)
frame2.grid(row=2,pady=10)
Label(frame2,text="Online Bus Booking System",font="arial 23 bold",bg="light blue",fg="red").grid(row=2,column=1)

frame3=Frame(root)
frame3.grid(row=3,pady=17)
Label(frame3,text="Name: Vaishali Srivastava",font="arial 14 bold",fg="dark blue").grid(row=3,column=1)

frame4=Frame(root)
frame4.grid(row=4,pady=17)
Label(frame4,text="Er no: 211B337",font="arial 14 bold",fg="dark blue").grid(row=4,column=1)

frame5=Frame(root)
frame5.grid(row=5,pady=17)
Label(frame5,text="Mobile no: 1234567890",font="arial 14 bold",fg="dark blue").grid(row=5,column=1)

frame6=Frame(root)
frame6.grid(row=6,pady=10)
Label(frame6,text="Submitted to: Dr.Mahesh Kumar",font="arial 20 bold",bg="light blue",fg="red").grid(row=6,column=1)

frame7=Frame(root)
frame7.grid(row=7,pady=10)
Label(frame7,text="Project Based Learning",font="arial 14 bold",fg="red").grid(row=7,column=1)

#root.bind('<KeyPress>',lambda e: root.destroy())
root.bind('<KeyPress>',close)


root.mainloop()
