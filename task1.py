
from __future__ import print_function
import sqlite3
import sys
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from pydal import DAL, Field
from reportlab.lib import colors
from collections import namedtuple
from PDFWriter import PDFWriter
# connection to sqlite database
conn = sqlite3.connect('info.s3db')
c = conn.cursor()
# Table name :- info
# feilds :- 1. number(int)AI pk
#           2. name(vc) 
#           3. age(int)
#           4. mobile_number(int)
#           5. email_id(vc)
#           6. address (vc)
#           7. gender(vc) def(Prefer not to say)
#           8. Nationality(vc) 
#           9. Qualification
def delt():
    c.execute("drop table info") 
    conn.commit()

    c.execute("""create table info(
	             number INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	             name VARCHAR(30) NOT NULL,
	             age INTEGER NOT NULL,
	             mobile_number INT NOT NULL,
	             email_id varchar(60) NOT NULL,
	             address VARCHAR(50),
	             gender varchar(14) default "Prefer not to say",
	             nationality varchar(20),
	             qualification varchar(20) 
	             )""")


    c.execute("Delete from info where number = 2")
    conn.commit()
    print()
    print("All records deleted successfully!")
    front_end()



def enter():
	print()
	print("!! Index once assigned can never be changed until all records are delete and entered again !!")
	nm = input("Enter Name :- ")
	ag = int(input("Enter Age :- "))
	mn = int(input("Enter Mobile Number :- "))
	em = input("Enter Email-Id :- ")
	ad = input("Enter Address :- ")
	gd = input("Enter Gender :- ")
	na = input("Enter Nationality :- ")
	qf = input("Enter Qualification :- ")
	if len(qf) <= 17:
		temp  =  len(qf)
		nln = 17 - temp
		asp = " " * nln
		qf = qf + asp 
	lst1 = list()
	lst1.extend([nm,ag,mn,em,ad,gd,na,qf])
	c.execute("INSERT INTO info (name, age, mobile_number, email_id, address, gender, nationality, qualification) VALUES (?,?,?,?,?,?,?,?)",lst1)
	conn.commit()
	print()
	print("Data entered successfully!")
	print()
	front_end()
def view_all():
	print()
	print("The records are as follows :")
	c.execute("SELECT * from info")
	all_info = c.fetchall()
	print("Index     Name              Age        Number            Email-Id                         Address         Gender      Nationality   Qualification     ")
	for i in all_info:		
		print("-------+---------------+---------+-----------------+-------------------------------+---------------+-----------+-------------+------------------+")
		for j in i:
			print(j,"       ",end=" ")
		print()
	print()
	front_end()
def view_spc():
	print()
	ind = input("Enter Index of person :- ")
	lst2 = list()
	lst2.append(ind)
	c.execute("select * from info where number = ?",lst2)
	res = c.fetchall()
	print("Index     Name              Age        Number            Email-Id                         Address         Gender      Nationality   Qualification     ")
	for i in res:		
		print("-------+---------------+---------+-----------------+-------------------------------+---------------+-----------+-------------+------------------+")
		for j in i:
			print(j,"       ",end=" ")
		print()
	print()
	front_end()
def delete_all():
	delt()
def delete_spc():
	print()
	del_ind = input("Enter index of record you want to delete :- ")
	lst3  = list()
	lst3.append(del_ind)
	c.execute("delete from info where number = ?",lst3)
	conn.commit()
	print("Record deleted successfully!")
	front_end()
def update():
	print()
	ind_upd = input("Enter index of record you want to update :-")

	nm = input("Enter Name :- ")
	cmd  ="update info set name = ? where number = ?"
	data = (nm, ind_upd)
	c.execute(cmd,data)

	ag = int(input("Enter Age :- "))
	cmd  ="update info set age = ? where number = ?"
	data = (ag, ind_upd)
	c.execute(cmd,data)

	mn = int(input("Enter mobile number :- "))
	cmd  ="update info set mobile_number = ? where number = ?"
	data = (mn, ind_upd)
	c.execute(cmd,data)

	em= input("Enter Email-Id :- ")
	cmd  ="update info set email_id = ? where number = ?"
	data = (em, ind_upd)
	c.execute(cmd,data)

	ad = input("Enter Address :- ")
	cmd  ="update info set address = ? where number = ?"
	data = (ad, ind_upd)
	c.execute(cmd,data)

	gd = input("Enter Gender :- ")
	cmd  ="update info set gender = ? where number = ?"
	data = (gd, ind_upd)
	c.execute(cmd,data)

	na = input("Enter Nationality :- ")
	cmd  ="update info set nationality = ? where number = ?"
	data = (na, ind_upd)
	c.execute(cmd,data)

	qf = input("Enter Qualification :- ")
	cmd  ="update info set qualification = ? where number = ?"
	data = (qf, ind_upd)
	c.execute(cmd,data)
	conn.commit()
	print("Data updated successfully!")
	front_end()

def create():
    print("Enter Index of person or type 'all' for all records ")
    inp = input()
    if inp == "all":
        gen_tup = namedtuple('Index','Name','Age','Number','Email-Id','Address','Gender','Nationality','Qualification')
        c.execute("select number, name, age, mobile_number, email_id, address, gender, nationality, qualification from info")
        pw = PDFWriter("info.pdf")
        pw.setFont("Courier", 12)
        pw.setHeader("Known information of people")
        pw.setFooter("Generated by :- Kushagra Sharma")
        hdr_flds = [ str(hdr_fld).rjust(10) + " " for hdr_fld in infor._fields ]
        hdr_fld_str = ''.join(hdr_flds)
        print_and_write(pw, '=' * len(hdr_fld_str))
        print_and_write(pw, hdr_fld_str)
        for stock in map(infor._make, c.fetchall()):
            row = [ str(col).rjust(10) + " " for col in (info.number, \
            info.name, info.age, info.mobile_number, info.email_id, info.address, info.gender, info.nationality, info.qualification) ]
            # Above line can instead be written more simply as:
            # row = [ str(col).rjust(10) + " " for col in stock ]
            row_str = ''.join(row)
            print_and_write(pw, row_str)
            print_and_write(pw, '=' * len(hdr_fld_str))
            print_and_write(pw, '-' * len(hdr_fld_str))






def front_end():
    print()
    print("""1. Enter new record
2. View all records
3. View specific record
4. Delete all records
5. Delete specific records
6. Update specific record
7. Enter 'create' to get PDF document
0. Exit""")
    choice = input()
    if choice == "1" or choice == "enter new record" or choice == "Enter new record":
	    enter()
    if choice == "2" or choice == "view all record" or choice == "View all record":
	    view_all()
    if choice == "3" or choice == "view specific record" or choice == "View specific record":
	    view_spc()
    if choice == "4" or choice == "delete all records" or choice == "Delete all records":
	    delete_all()
    if choice == "5" or choice == "delete specific records" or choice == "Delete specific records":
	    delete_spc()
    if choice == "6" or choice == "update specific record" or choice == "Update specific record":
	    update()
    if choice == "create":
        create()
    if choice == "0" or choice == "exit" or choice == "Exit":
	    sys.exit()
    else:
        print("Invalid Entry")
        front_end()


front_end()
conn.commit()
conn.close()