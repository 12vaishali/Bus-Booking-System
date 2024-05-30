import sqlite3
con=sqlite3.Connection("bus_db")
cur=con.cursor()
cur.execute('create table if not exists bus(bus_id varchar(5) not null primary key,bus_type varchar(10),capacity int,fair int,op_id varchar(5) not null,route_id varchar(5) not null,foreign key(op_id) references operator(opr_id),foreign key(route_id) references route(r_id))')
cur.execute('create table if not exists operator(opr_id varchar(5) primary key,name varchar(20),address varchar(50),phone char(10),email varchar(30))')
cur.execute('create table if not exists running(b_id varchar(5) ,run_date date,seat_avail int,foreign key(b_id) references bus(bus_id))')
cur.execute('create table if not exists route(r_id varchar(5) not null primary key,s_name varchar(20),s_id varchar(5),e_name varchar(20),e_id varchar(5) )')
cur.execute('create table if not exists booking_history(name varchar(20),gender char(1),no_of_seat int,phone char(10),age int,booking_ref varchar(10) not null primary key,booking_date date,travel_date date,bid varchar(5),foreign key(bid) references bus(bus_id))')

res=cur.fetchall()
