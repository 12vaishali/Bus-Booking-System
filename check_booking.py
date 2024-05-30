from tkinter import *
import sqlite3
con=sqlite3.Connection("bus_db")
cur=con.cursor()

root=Tk()

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def ch():
    frame4=LabelFrame(root,relief='groove',bd=5)
    frame4.grid()
    mobile=Mobile_no.get()
    if len(mobile)==10 and mobile.isdigit():
     cur.execute('select * from booking_history where phone=?',[mobile])
     res_tkt=cur.fetchall()
    for i in res_tkt:
        name=i[0]
        print(name)
        gen=i[1]
        seat=i[2]
        phone=i[3]
        age=i[4]
        ref=i[5]
        book_date=i[6]
        travel_date=i[7]
        b_i_d=i[8]
        cur.execute('select fair,route_id from bus where bus_id=?',[b_i_d])
        res_bus=cur.fetchall()
        fare=res_bus[0][0]
        route_id=res_bus[0][1]
        cur.execute('select s_name,e_name from route where r_id=?',[route_id])
        res_route=cur.fetchall()
        s_name=res_route[0][0]
        e_name=res_route[0][1]
        cur.execute('select booking_ref from booking_history where phone=?',[phone])
        res_ref=cur.fetchall()
        b_ref=res_ref[0][0]
    Label(frame4,text="Passenger:"+str(name)).grid(row=4,column=1)
    Label(frame4,text="Gender:"+gen).grid(row=4,column=3)
    Label(frame4,text="No of seat:" + str(seat)).grid(row=5,column=1)
    Label(frame4,text="Phone:"+ str(mobile)).grid(row=5,column=3)
    Label(frame4,text="Age:"+ str(age)).grid(row=6,column=1)
    Label(frame4,text="Fare Rs:" + str(fare)).grid(row=6,column=3)
    Label(frame4,text="Booking Ref:"+b_ref).grid(row=7,column=1)
    
    Label(frame4,text="Travel On:" + travel_date).grid(row=8,column=1)
    Label(frame4,text="Booked On:"+ book_date).grid(row=8,column=3)
    
    Label(frame4,text="Boarding Point:"+s_name).grid(row=9,column=3)

bus=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=1)
Label(frame1,image=bus).grid(row=1,column=1,padx=w/2.3)

frame2=Frame(root)
frame2.grid(row=2,pady=15)
Label(frame2,text="Online Bus Booking System",font="arial 20 bold",bg="light blue",fg="red").grid(row=2,column=1)

frame3=Frame(root)
frame3.grid(row=3,pady=10)
Label(frame3,text="Check Your Booking",font="arial 15 bold",bg="pale green",fg="green").grid(row=3,column=1)

frame4=Frame(root)
frame4.grid(row=4,pady=10)
Label(frame4,text='Enter Your Mobile No.',font="arial 10 bold").grid(row=4,column=1,padx=30)
Mobile_no=Entry(frame4)
Mobile_no.grid(row=4,column=2,padx=30)
Button(frame4,text='Check Booking',font="arial 10 bold",command=ch).grid(row=4,column=3,padx=30)


root.mainloop()
