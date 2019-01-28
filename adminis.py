import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
import os
import sqlite3
import xlwt 
from xlwt import Workbook 

root1=Tk()
root1.geometry('1400x730')
root1.title('ADMINISTRATOR')

n1=StringVar()
n2=StringVar()
h1=StringVar()
h2=StringVar()
D1=StringVar()
D2=StringVar()
D3=StringVar()
D4=StringVar()
D5=StringVar()
D6=StringVar()
D7=StringVar()
D8=StringVar()
hd1=StringVar()

DD1=StringVar()
DD2=StringVar()
DD3=StringVar()
DD4=StringVar()
DD5=StringVar()
DD6=StringVar()
DD7=StringVar()
DD8=StringVar()


def enroll(f11):
    global data
    tn1=n1.get()
    tn2=n2.get()
    conn=sqlite3.connect('adimidata.db')
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS adimi(data TEXT)')
    t=cursor.execute('select * from adimi')
    a=t.fetchone()
    data=a[0]
    print (data)
    conn.commit()
    if (tn1=='a'):
        if (tn2=='a'):
            m = "{Login SucessFull"
            messagebox.showinfo("Login Info", m)
            f11.destroy()
            main()
        else:
            m = " Login UnSucessFull!!!Password is wrong"
            messagebox.showerror("Login Info!", m)
                    
    else:
        m = "your are enter wrong username"
        messagebox.showwarning("Login Info!", m)


def main():
    
    label=Label(root1,text="WELCOME IN ADMINISTRATOR",font=("bold",20))
    label.place(x=350,y=10)

    def Find(f22):
        f22.destroy()
        f11.destroy()
        f33=Frame(root1,width=500,height=200,bg="silver",relief=SUNKEN)
        f33.place(x=200,y=200)

        label=Label(f33,text="Find The Question",font=("bold",20))
        label.place(x=120,y=10)

        label=Label(f33,text="Enter The Question Number:-",font=("bold",15))
        label.place(x=10,y=80)
        e1=tk.Entry(f33,font=("bold",15),textvariable=h1)
        e1.place(x=280,y=80)
        e1.delete(0,END)


        def check(f33):
            try:
                t1=h1.get()
                conn=sqlite3.connect(data)
                cursor=conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS QUS(Qus_no INTEGER,Qusetion TEXT,Option_A TEXT,Option_B TEXT,Option_C TEXT,Option_D TEXT,Answer TEXT)')
                con=cursor.execute('SELECT Qus_no, Qusetion,Option_A,Option_B,Option_C,Option_D,Answer FROM QUS WHERE Qus_no=?',(t1,))
                t=con.fetchone()
                a1="Qusetion number is {}".format(t[0])
                a2=t[1]
                a3=t[2]
                a4=t[3]
                a5=t[4]
                a6=t[5]
                a7="Answer is {}".format(t[6])


                f44=Frame(root1,width=800,height=500,bg="silver",relief=SUNKEN)
                f44.place(x=50,y=100)

                label11=Label(f44,text="Details of Question",font=("bold",20))
                label11.place(x=50,y=40)

                label1=Label(f44,text=a1,bg="silver",font=("bold",15))
                label1.place(x=100,y=100)

                label2=Label(f44,text=a2,bg="silver",font=("bold",15))
                label2.place(x=100,y=150)

                label3=Label(f44,text=a3,bg="silver",font=("bold",15))
                label3.place(x=100,y=200)

                label4=Label(f44,text=a4,bg="silver",font=("bold",15))
                label4.place(x=100,y=250)

                label5=Label(f44,text=a5,bg="silver",font=("bold",15))
                label5.place(x=100,y=300)

                label6=Label(f44,text=a6,bg="silver",font=("bold",15))
                label6.place(x=100,y=350)

                label7=Label(f44,text=a7,bg="silver",font=("bold",15))
                label7.place(x=100,y=400)



                logbtn2=Button(f44,text="back",width=8,command=lambda:Find(f44),font=("bold",15)).place(x=200,y=450)
            except:
                messagebox.showerror("Error","plz!!! Check Entered Question Number")
                
                
        
        logbtn1=Button(f33,text="Check",width=8,command=lambda:check(f33),font=("bold",15)).place(x=100,y=150)
        logbtn2=Button(f33,text="back",width=8,command=main,font=("bold",15)).place(x=250,y=150)

    
    def Insert(f22):
        try:
        
            f22.destroy()
            f11.destroy()
            
            
            f44=Frame(root1,width=700,height=550,bg="silver",relief=SUNKEN)
            f44.place(x=150,y=100)

            label=Label(f44,text="Enter Details of Question ",font=("bold",20))
            label.place(x=200,y=40)

            label1=Label(f44,text="Enter Question Number:-",font=("bold",15))
            label1.place(x=100,y=100)
            e1=Entry(f44,font=("bold",15),textvariable=D1).place(x=350,y=100)

            label2=Label(f44,text="Enter Question:-",font=("bold",15))
            label2.place(x=100,y=150)
            e2=Entry(f44,font=("bold",15),textvariable=D2).place(x=350,y=150)

            label3=Label(f44,text="Enter option A:-",font=("bold",15))
            label3.place(x=100,y=200)
            e3=Entry(f44,font=("bold",15),textvariable=D3).place(x=350,y=200)

            label4=Label(f44,text="Enter option B:-",font=("bold",15))
            label4.place(x=100,y=250)
            e4=Entry(f44,font=("bold",15),textvariable=D4).place(x=350,y=250)

            label5=Label(f44,text="Enter option C:-",font=("bold",15))
            label5.place(x=100,y=300)
            e5=Entry(f44,font=("bold",15),textvariable=D5).place(x=350,y=300)

            label6=Label(f44,text="Enter option D:-",font=("bold",15))
            label6.place(x=100,y=350)
            e6=Entry(f44,font=("bold",15),textvariable=D6).place(x=350,y=350)

            label7=Label(f44,text="Enter option Of Answer:-",font=("bold",15))
            label7.place(x=100,y=400)
            e7=Entry(f44,font=("bold",15),textvariable=D7).place(x=350,y=400)

            def back(f44):
                f44.destroy()
                main()

            logbtn2=Button(f44,text="back",width=8,command=lambda:back(f44),font=("bold",15)).place(x=350,y=500)

        except:
            messagebox.showerror("Error","plz!!! Check Entered Question Number")

        def Insert1(f33):
            try:
                d1=D1.get()
                d2=D2.get()
                d3=D3.get()
                d4=D4.get()
                d5=D5.get()
                d6=D6.get()
                d7=D7.get()

                conn=sqlite3.connect(data)
                cursor=conn.cursor()
                cursor=cursor.execute('INSERT INTO Qus(Qus_no, Qusetion,Option_A,Option_B,Option_C,Option_D,Answer) VALUES(?,?,?,?,?,?,?)',(d1,d2,d3,d4,d5,d6,d7))
                conn.commit()
                messagebox.showinfo("Data Insert","Your Question is inserted into record")
                t=messagebox.askyesno("Quit","Do u want to Quit the form")
                if(t==True):
                    root1.destroy()
                else:
                    f33.destroy()
            except:
                messagebox.showerror("Error","plz!!! Check Entered Question Number")
                

        logbtn1=Button(f44,text="okk",width=8,command=lambda:Insert1(f44),font=("bold",15)).place(x=200,y=500)

    
    def Update(f22):
        f22.destroy()
        f11.destroy()

        
        f55=Frame(root1,width=700,height=550,bg="silver",relief=SUNKEN)
        f55.place(x=150,y=100)

        label=Label(f55,text="Updata Details of Question ",font=("bold",20))
        label.place(x=200,y=40)

        label1=Label(f55,text="Enter Question Number:-",font=("bold",15))
        label1.place(x=100,y=100)
        e1=Entry(f55,font=("bold",15),textvariable=DD1).place(x=350,y=100)

        label2=Label(f55,text="Enter Question:-",font=("bold",15))
        label2.place(x=100,y=150)
        e2=Entry(f55,font=("bold",15),textvariable=DD2).place(x=350,y=150)

        label3=Label(f55,text="Enter option A:-",font=("bold",15))
        label3.place(x=100,y=200)
        e3=Entry(f55,font=("bold",15),textvariable=DD3).place(x=350,y=200)

        label4=Label(f55,text="Enter option B:-",font=("bold",15))
        label4.place(x=100,y=250)
        e4=Entry(f55,font=("bold",15),textvariable=DD4).place(x=350,y=250)

        label5=Label(f55,text="Enter option C:-",font=("bold",15))
        label5.place(x=100,y=300)
        e5=Entry(f55,font=("bold",15),textvariable=DD5).place(x=350,y=300)

        label6=Label(f55,text="Enter option D:-",font=("bold",15))
        label6.place(x=100,y=350)
        e6=Entry(f55,font=("bold",15),textvariable=DD6).place(x=350,y=350)

        label7=Label(f55,text="Enter option Of Answer:-",font=("bold",15))
        label7.place(x=100,y=400)
        e7=Entry(f55,font=("bold",15),textvariable=DD7).place(x=350,y=400)

        def back(f55):
            f55.destroy()
            main()

        logbtn2=Button(f55,text="back",width=8,command=lambda:back(f55),font=("bold",15)).place(x=250,y=450)


        def Update1(f33):
            try:
                d1=DD1.get()
                d2=DD2.get()
                d3=DD3.get()
                d4=DD4.get()
                d5=DD5.get()
                d6=DD6.get()
                d7=DD7.get()
                d8=DD8.get()

                conn=sqlite3.connect(data)
                cursor=conn.cursor()
                cursor=cursor.execute('UPDATE Qus SET Qusetion=?,Option_A=?,Option_B=?,Option_C=?,Option_D=?,Answer=? WHERE Qus_no=?',(d2,d3,d4,d5,d6,d7,d1))
                conn.commit()
                messagebox.showinfo("Data Updata","Your Question is Updata in the record")
                t=messagebox.askyesno("Quit","Do u want to Quit the form")
                if(t==True):
                    root1.destroy()
                else:
                    f33.destroy()
            except:
                messagebox.showerror("Error","plz!!! Question Number Does Not Exist")
        logbtn1=Button(f55,text="okk",width=8,command=lambda:Update1(f55),font=("bold",15)).place(x=300,y=500)


    def delete(f22):
        f22.destroy()
        f11.destroy()
        f33=Frame(root1,width=500,height=200,bg="silver",relief=SUNKEN)
        f33.place(x=200,y=200)

        label=Label(f33,text="Delete The Question",font=("bold",20))
        label.place(x=120,y=10)

        label=Label(f33,text="Enter Question Number:-",font=("bold",15))
        label.place(x=10,y=80)
        e1=tk.Entry(f33,font=("bold",15),textvariable=hd1).place(x=280,y=80)

        def delete1(f33):
            try:
                dd1=hd1.get()
                conn=sqlite3.connect(data)
                cursor=conn.cursor()
                cursor=cursor.execute('DELETE FROM Qus WHERE Qus_no=? ',(dd1,))
                conn.commit()
                messagebox.showinfo("Data Delete","Your Question is Delete in the record")
                t=messagebox.askyesno("Quit","Do u want to Quit the form")
                if(t==True):
                    root1.destroy()
                else:
                    f33.destroy()
            except:
                messagebox.showerror("Error","plz!!! Check Entered Question Number")


        logbtn2=Button(f33,text="back",width=8,command=main,font=("bold",15)).place(x=250,y=150)
            

        logbtn1=Button(f33,text="delete",width=8,command=lambda:delete1(f33),font=("bold",15)).place(x=100,y=150)


    def show(f22):
        global lb
        f11.destroy()
        f22.destroy()
        f23=Frame(root1,width=1000,height=550,bg="silver",relief=SUNKEN)
        f23.place(x=70,y=100)
        label=Label(f23,text="MARKS OF STUDENT",font=("bold",20))
        label.place(x=250,y=30)
        lb=Listbox(f23, width=90, height=20)
        lb.place(x=50,y=100)
        conn=sqlite3.connect(data)
        cursor=conn.cursor()
        con=cursor.execute('SELECT enroll,marks FROM ANS')
        t=con.fetchall()
        for row in t:
            print (row)
            lb.insert(END,row)
            #lb.insert(END,"")

        def Del():
            global lb
            current=lb.get(lb.curselection())
            selection=lb.curselection()
            dd1=current[0]
            print (dd1)
            print (selection)
            lb.delete(selection)
            conn=sqlite3.connect(data)
            cursor=conn.cursor()
            cursor=cursor.execute('DELETE FROM ANS WHERE enroll=? ',(dd1,))
            cursor=cursor.execute('DELETE FROM DATA WHERE enroll=? ',(dd1,))
            conn.commit()

        def Excel():   
            wb= Workbook()
            sh = wb.add_sheet('sh')
            conn=sqlite3.connect(data)
            c=conn.cursor()
            c.execute("select * from ANS")
            mysel=c.execute("select * from ANS")
            for i, row in enumerate(mysel):
                for j, value in enumerate(row):
                    sh.write(i, j, value) 
            wb.save('xlwt data.xls')

        def search():
            label21=Label(f23,text="Enrollment:-",font=("bold",15))
            label21.place(x=600,y=120)

            e1=Entry(f23,bd=5,font=("bold",15))
            e1.place(x=750,y=120)
            

            def finds():
                try:
                    aa=e1.get()
                    conn=sqlite3.connect(data)
                    cursor=conn.cursor()
                    con=cursor.execute('SELECT enroll,marks FROM ANS where enroll=?',(aa,))
                    t=con.fetchall()
                    lb.delete(0,END)
                    for row in t:
                        print (row)
                        lb.insert(END,row)
                except:
                    messagebox.showerror("Error","plz!!! Check Entered Enrolment Number")
                        
                

            logbtn1=Button(f23,text="Find",width=8,command=finds,font=("bold",15)).place(x=685,y=200)

        def back(f23):
            f23.destroy()
            main()
        def show_all(f23):
            show(f23)
            
            

        logbtn1=Button(f23,text="Excel",width=8,command=Excel,font=("bold",15)).place(x=350,y=450)
        logbtn2=Button(f23,text="Back",width=8,command=lambda: back(f23),font=("bold",15)).place(x=200,y=500)
        logbtn1=Button(f23,text="Search",width=8,command=search,font=("bold",15)).place(x=350,y=500)
        logbtn1=Button(f23,text="Delete",width=8,command=Del,font=("bold",15)).place(x=200,y=450)
        logbtn1=Button(f23,text="Show All",width=8,command=lambda: show_all(f23),font=("bold",15)).place(x=500,y=475)
        
        

    global c
    
    f22=Frame(root1,width=900,height=500,bg="silver",relief=SUNKEN)
    f22.place(x=70,y=150)

    c=PhotoImage(file="F:\\python project\\images\\aa3.PNG")

    label=tk.Label(f22,image=c,borderwidth=5,bg="silver",font='Arial 25 bold')
    label.place(x=0,y=0)

    f11=Frame(root1,width=200,height=360,bg="silver",relief=SUNKEN)
    f11.place(x=1100,y=220)

    logbtn1=Button(f11,text="Find",width=8,command=lambda:Find(f22),font=("bold",15)).place(x=60,y=30)
    logbtn2=Button(f11,text="Insert",width=8,command=lambda:Insert(f22),font=("bold",15)).place(x=60,y=100)
    logbtn3=Button(f11,text="Update",width=8,command=lambda:Update(f22),font=("bold",15)).place(x=60,y=170)
    logbtn4=Button(f11,text="Delete",width=8,command=lambda:delete(f22),font=("bold",15)).place(x=60,y=240)
    logbtn4=Button(f11,text="Show",width=8,command=lambda:show(f22),font=("bold",15)).place(x=60,y=310)
    

f11=Frame(root1,width=600,height=400,bg="silver",relief=SUNKEN)
f11.place(x=400,y=200)

label=Label(f11,text="WELCOME TO ADMINISTRATOR",borderwidth=5, relief="groove",font=("bold",20))
label.place(x=100,y=30)

label2=Label(f11,text="Enter your Username:- ",font=("bold",15))
label2.place(x=70,y=120)

e1=Entry(f11, textvariable=n1,bd=5,font=("bold",15))
e1.place(x=290,y=120)

label2=Label(f11,text="Enter your Password:- ",font=("bold",15))
label2.place(x=70,y=180)

e2=tk.Entry(f11, textvariable=n2,bd=5,show="*",font=("bold",15))
e2.place(x=290,y=180)

logbtn2=tk.Button(f11,text="Submit",width=8,command=lambda:enroll(f11),font=("bold",15)).place(x=250,y=250)
#logbtn3=tk.Button(f11,text="Forget Password",command=lambda:forget(f11),font=("bold",12)).place(x=250,y=320)
root1.mainloop()
