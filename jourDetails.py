from tkinter import *
import sqlite3
con=sqlite3.Connection("bus_db")
cur=con.cursor()
from tkinter.messagebox import *
root=Tk()

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def show_bus():
    tp=to_place.get()
    fp=from_place.get()
    jd=journey_date.get()
    if tp.isalpha() and fp.isalpha():
        if not jd=='':
            tp = tp.lower()
            fp = fp.lower()
            cur.execute('select r_id from route where s_name=? and e_name=?', (fp, tp))
            res_route = cur.fetchall()
            if len(res_route)==0:
                showerror('no route found','we are currently not running on this route')
            else:
                for i in res_route:
                    for j in i:
                        val_route = str(j)
                cur.execute('select bus_id from bus where route_id=?', (val_route))
                res_bid = cur.fetchall()
                
                if len(res_bid)==0:
                    showerror('no bus found','we have not started any bus on this route yet!!')
                else:
                    val_bid = []
                    for i in res_bid:
                        for j in i:
                            val_bid.append(j)
                    res_new_bid=[]
                    for i in range(len(val_bid)):
                        cur.execute('select b_id from running where run_date=? and b_id=? ',(jd, val_bid[i]))
                        res_new_bid.append(cur.fetchall())
                    #print(res_new_bid)
                    b=[]
                    for i in res_new_bid:
                        for j in i:
                            b.append(j[0])
                    
                    #print(b)
                    if len(b)==0:
                        showerror('no running bus',"try another date!!")
                    else:
                        Label(root,text='select bus ',font='Arial 10 bold').grid(row=6,column=3)
                        Label(root, text='operator ', font='Arial 10 bold').grid(row=6, column=4)
                        Label(root, text='bus_type ', font='Arial 10 bold').grid(row=6, column=5)
                        Label(root, text='Available Capacity ', font='Arial 10 bold').grid(row=6, column=6)
                        Label(root, text='fare ', font='Arial 10 bold').grid(row=6, column=7)
                        r=7
                        bus_no=IntVar()
                        bus_select = IntVar()
                        serial_no=1
                        for i in b:
                            bus_no=i
                            cur.execute('select op_id from bus where bus_id=?',(i))
                            res_opr_id=cur.fetchall()
                            for j in res_opr_id:
                                opr_id=j[0]
                            
                            cur.execute('select name from operator where opr_id=?',(opr_id))
                            res_opr_name=cur.fetchall()
                            for j in res_opr_name:
                                opr_name=j[0]

                            cur.execute('select bus_type from bus where bus_id=?',(i))
                            res_bus_type=cur.fetchall()
                            for j in res_bus_type:
                                bus_type=j[0]

                            cur.execute('select seat_avail from running where run_date=? and b_id=?',(jd,i))
                            res_seat_avail=cur.fetchall()
                            for j in res_seat_avail:
                                seat_avail=j[0]
                            
                            cur.execute('select fair from bus where bus_id=?',(i))
                            res_fare=cur.fetchall()
                            for j in res_fare:
                                fare=j[0]
                            r=7
                            def show_button():
                                Button(root, text='PROCEED', bg='green', fg='black', font='Arial 12 bold',command=proceed).grid(row=10, column=9, padx=30)

                            Label(root, text=opr_name, font='Arial 10 bold').grid(row=r, column=4)
                            Label(root, text=bus_type, font='Arial 10 bold').grid(row=r, column=5)
                            Label(root, text=seat_avail, font='Arial 10 bold').grid(row=r, column=6)
                            Label(root, text=fare, font='Arial 10 bold').grid(row=r, column=7)

                            #r+=1
                            var=Radiobutton(root,value=bus_no,variable=bus_select,command=show_button)
                            var.grid(row=r,column=3)    
                            
                                
                                #serial_no+=1

                        def proceed():
                            f_bus_id = bus_select.get()

                            Label(root,text="\n").grid(row=10,columnspan=12)
                            Label(root,text='Fill passenger details to book the bus', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=11,columnspan=12)
                            Label(root, text="\n").grid(row=12,columnspan=12)

                            Label(root,text='name',font='Arial 8 bold').grid(row=13,column=1)
                            pname = Entry(root, font='Arial 8 bold', fg='black')
                            pname.grid(row=13,column=2)

                            gender = StringVar()
                            gender.set("Select Gender")
                            opt = ["M", "F", "T"]
                            g_menu = OptionMenu(root, gender, *opt)
                            g_menu.grid(row=13, column=3)

                            Label(root, text='no of seats', font='Arial 8 bold').grid(row=13, column=4)
                            pseat=Entry(root, font='Arial 8 bold', fg='black')
                            pseat.grid(row=13,column=5)

                            Label(root, text='mobile', font='Arial 8 bold').grid(row=14, column=1)
                            pmobile = Entry(root, font='Arial 8 bold', fg='black')
                            pmobile.grid(row=14, column=2)

                            Label(root, text='age', font='Arial 8 bold').grid(row=14, column=3)
                            page = Entry(root, font='Arial 12 bold', fg='black')
                            page.grid(row=14, column=4)
                            #def confirm():
                                
                                #import ticket_detail
                            def book_seat():
                                def close(e=1):
                                    root.destroy()
                                    import ticket_detail
                                name=pname.get()
                                gen=gender.get()
                                seats=pseat.get()
                                seats=int(seats)
                                age=page.get()
                                age=int(age)
                                mobile=pmobile.get()
                                bid=bus_select.get()
                                print(name, gen, age, mobile, seats, bid)
                                if len(mobile)==10:
                                    if len(name)>0 and len(name)<20:
                                        if age>0 and age<150:
                                            if seats>0 and seats<10:
                                                print(name, gen, age, mobile, seats, bid)
                                                booking_ref=1
                                                cur.execute('select booking_ref from booking_history')
                                                res_ref=cur.fetchall()
                                                ref=[]
                                                for i in res_ref:
                                                    ref.append(i[0])
                                                booking_ref=len(ref)+1
                                                #print(booking_ref)
                                                cur_date='2022-12-01'
                                                cur.execute('insert into booking_history(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                con.commit()
                                                cur.execute('select * from booking_history')
                                                resu=cur.fetchall()
                                                con.commit()
                                                print(resu)
                                                cur.execute('select seat_avail from running where b_id=? and run_date=?',(bid,jd))
                                                res_s=cur.fetchall()
                                                
                                                s=res_s[0][0]
                                                s=s-seats
                                                cur.execute('update running set seat_avail=? where b_id=? and run_date=?',(s,bid,jd))
                                                con.commit()
                                                showinfo("succefull","Fare to be paid:"+str(seats*fare))

                                            else:
                                                showerror("exceed","you can book upto 10 seats")
                                        else:
                                            showerror("incorrect age","enter correct age")
                                    else:
                                        showerror("incorrect name","enter correct name")
                                else:
                                    showerror("invalid mobile no","enter valid mobile no")
                                root.bind('<KeyPress>',close)
                            Button(root, text='BOOK SEAT', bg='green', fg='black', font='Arial 12 bold',command=book_seat).grid(row=14, column=5, padx=30)


            
bus = PhotoImage(file='Bus_for_project.png')
Label(root, image=bus).grid(row=0, column=3, columnspan=12)
Label(root, text="Online Bus Booking System", font='Arial 28 bold', bg='sky blue', fg='red').grid(row=2,column=3,pady=20,columnspan=12)
Label(root, text='Enter Journey Details', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=3,column=3,columnspan=12,pady=20)
Label(root, text='To', fg='black', font='Arial 12 bold').grid(row=4, column=3, padx=30)
to_place = Entry(root, font='Arial 12 bold', fg='black')
to_place.grid(row=4, column=4, padx=50)
Label(root, text='From', fg='black', font='Arial 12 bold').grid(row=4, column=5, padx=30)
from_place = Entry(root, font='Arial 12 bold', fg='black')
from_place.grid(row=4, column=6, padx=50)
Label(root, text='Journey date', fg='black', font='Arial 12 bold').grid(row=4, column=7, padx=30)
journey_date = Entry(root, font='Arial 12 bold', fg='black')
journey_date.grid(row=4, column=8, padx=50)
Label(root,text="date formate YYYY-MM-DD").grid(row=5,column=8)
Button(root, text='Show Bus', bg='green', fg='black', font='Arial 12 bold',command=show_bus).grid(row=4, column=9, padx=30)
home = PhotoImage(file='home.png')
Button(root, image=home,command=show_bus).grid(row=4, column=10)
root.mainloop()
