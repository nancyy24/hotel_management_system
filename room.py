from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import random
# pip install mysql-connector-python
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Room_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title("ROOM BOOKING")
        self.root.geometry("1360x525+0+185")


        # adding variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_no_of_days=StringVar()
        self.var_paid_tax=StringVar()
        self.var_actual_bill=StringVar()
        self.var_total_bill=StringVar()
        # adding the title
        lbl_title = Label(self.root,text="ROOM BOOKING WINDOW",font=("Helvetica",24,"bold"),bg="light slate gray",fg="black",bd=4,relief=SOLID)
        lbl_title.place(x=0,y=0,width=1360,height=40)

         # creating frame
        main_frame=Frame(self.root,bd=5,relief=RAISED,bg="black")
        main_frame.place(x=0,y=40,width=250,height=485)


        # adding side image
        cust_side_img1=Image.open("Images\hotelroom-1.jpg")
        cust_side_img1=cust_side_img1.resize((200,230),Image.ANTIALIAS)
        self.custsideimg1=ImageTk.PhotoImage(cust_side_img1)

        lblcustsideimg1 = Label(main_frame,image=self.custsideimg1,bd=4,relief=RAISED)
        lblcustsideimg1.place(x=15,y=15,width=200,height=230)

        # adding side image
        cust_side_img2=Image.open("Images\hotelroom-2.jpg")
        cust_side_img2=cust_side_img2.resize((200,200),Image.ANTIALIAS)
        self.custsideimg2=ImageTk.PhotoImage(cust_side_img2)

        lblcustsideimg2 = Label(main_frame,image=self.custsideimg2,bd=4,relief=RAISED)
        lblcustsideimg2.place(x=15,y=260,width=200,height=200)

        # adding label frame
        frame1 = LabelFrame(self.root,bd=4,relief=RAISED,text="ROOM DETAILS",font=("Helvetica",10,"bold"),bg="light slate gray",fg="black")
        frame1.place(x=250,y=40,width=1110,height=225)

        # LABELS AND ENTRIES
        # Contact 
        lbl_cust_contact=Label(frame1,text="Contact No",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_cust_contact.place(x=10,y=0,width=100)

        entry_contact=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_contact)
        entry_contact.place(x=120,y=0,width=120)

        btnFetch=Button(frame1,text="Fetch Data",command=self.fetch_customer_data,font=("arial",8,"bold"),bg="black",fg="gold",width=15)
        btnFetch.place(x=245,y=3,width=100)
        
        # vertical frame
        vertical = Frame(frame1, bg='black', height=50,width=1)
        vertical.place(x=350, y=10,height=150)

         # Check in date
        lbl_check_in=Label(frame1,text="Check In Date",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_check_in.place(x=370,y=0,width=150)

        entry_check_in=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_checkin)
        entry_check_in.place(x=540,y=0,width=150)


         # vertical frame
        vertical = Frame(frame1, bg='black', height=50,width=1)
        vertical.place(x=710, y=10,height=150)

        # Check out date
        lbl_check_out=Label(frame1,text="Check Out Date",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_check_out.place(x=730,y=0,width=150)

        entry_check_out=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_checkout)
        entry_check_out.place(x=890,y=0,width=150)


        
        # Room type COMBOBOX
        label_room_type=Label(frame1,text="Room Type",font=("arial",10,"bold"),padx=2,pady=4)
        label_room_type.place(x=10,y=40,width=150)

        combo_room_type=ttk.Combobox(frame1,font=("arial",14),width=20,state="readonly",textvariable=self.var_roomtype)
        combo_room_type["value"]=("Single","Double","Luxuxry")
        combo_room_type.current(0)
        combo_room_type.place(x=180,y=40,width=150)

        # Available room COMBOBOX
        # label_room_no=Label(frame1,text="Available room",font=("arial",10,"bold"),padx=2,pady=4)
        # label_room_no.place(x=370,y=40,width=150)

        # combo_room_no=ttk.Combobox(frame1,font=("arial",14),width=20,state="readonly",textvariable=self.var_roomavailable)
        # combo_room_no["value"]=("Male","Female","Others")
        # combo_room_no.current(0)
        # combo_room_no.place(x=540,y=40,width=150)

          # Paid Tax
        lbl_availroom=Label(frame1,text="Available Room",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_availroom.place(x=370,y=40,width=150)

        entry_avail_room=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_roomavailable)
        entry_avail_room.place(x=540,y=40,width=150)


        # # Meal COMBOBOX
        # label_room_no=Label(frame1,text="Meal",font=("arial",10,"bold"),padx=2,pady=4)
        # label_room_no.place(x=730,y=40,width=150)

        # combo_room_no=ttk.Combobox(frame1,font=("arial",14),width=20,state="readonly",textvariable=self.var_meal)
        # combo_room_no["value"]=("Male","Female","Others")
        # combo_room_no.current(0)
        # combo_room_no.place(x=890,y=40,width=150)

          # Meal
        lbl_meal=Label(frame1,text="Meal",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_meal.place(x=730,y=40,width=150)

        entry_lbl_meal=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_meal)
        entry_lbl_meal.place(x=890,y=40,width=150)

         # No of days
        lbl_total_days=Label(frame1,text="total Days",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_total_days.place(x=10,y=80,width=150)

        entry_total_days=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_no_of_days)
        entry_total_days.place(x=180,y=80,width=150)

        
         # Paid Tax
        lbl_Paid_Tax=Label(frame1,text="Paid Tax",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_Paid_Tax.place(x=370,y=80,width=150)

        entry_Paid_tax=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_paid_tax)
        entry_Paid_tax.place(x=540,y=80,width=150)

        
         # Actual Cost
        lbl_actual_cost=Label(frame1,text="Actual Cost",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_actual_cost.place(x=730,y=80,width=150)

        entry_actual_cost=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_actual_bill)
        entry_actual_cost.place(x=890,y=80,width=150)

         # Total Cost
        lbl_total_cost=Label(frame1,text="Actual Cost",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_total_cost.place(x=10,y=120,width=150)

        entry_total_cost=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_total_bill)
        entry_total_cost.place(x=180,y=120,width=150)

          # BUTTONS
        btn_frame=Frame(frame1,bd=2,relief=RIDGE)
        btn_frame.place(x=20,y=160,width=1050,height=40)

        
        btnBill=Button(btn_frame,text="Bill",font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnBill.place(x=90,y=3,width=150)

        btnAdd=Button(btn_frame,text="Save",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnAdd.place(x=260,y=3,width=150)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnUpdate.place(x=430,y=3,width=150)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnDelete.place(x=600,y=3,width=150)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnReset.place(x=770,y=3,width=150)

           # TABEL FRAME
        Table_Frame=LabelFrame(self.root,bd=4,relief=RAISED,text="VIEW DETAILS AND SEARCH SYSTEM",font=("arial",12,"bold"),padx=2,bg="grey")
        Table_Frame.place(x=250,y=268,width=1110,height=250)
        
        lblSearchBy=Label(Table_Frame,font=("arial",10,"bold"),text="Search By:",bg="red",fg="white",width=15)
        lblSearchBy.place(x=10,y=5,width=150)

        self.var_search=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.var_search,font=("arial",10,"bold"),width=20,state="readonly")
        combo_search["value"]=("Contact","Roomavailable")
        combo_search.current(0)
        combo_search.place(x=170,y=5,width=150)

        self.text_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.text_search,font=("arial",11,"bold"),width=25)
        txtSearch.place(x=330,y=5,width=150)

        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnSearch.place(x=490,y=5,width=150)
        
        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",10,"bold"),command=self.fetch_data,bg="black",fg="gold",width=10)
        btnShowAll.place(x=645,y=5,width=150)


        # SHOW DATA TABLE
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=35,width=1100,height=182)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Room_Details_Table=ttk.Treeview(details_table,column=("contact","checkin",'checkout',"roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Details_Table.xview)
        scroll_y.config(command=self.Room_Details_Table.yview)

        self.Room_Details_Table.heading("contact",text="Contact No.")
        self.Room_Details_Table.heading("checkin",text="Check-In")
        self.Room_Details_Table.heading("checkout",text="Check-Out")
        self.Room_Details_Table.heading("roomtype",text="Room-Type")
        self.Room_Details_Table.heading("roomavailable",text="Room Available")
        self.Room_Details_Table.heading("meal",text="Meal")
        self.Room_Details_Table.heading("noofdays",text="No_of_days")


        self.Room_Details_Table["show"]="headings"
        
        self.Room_Details_Table.column("contact",width=100)
        self.Room_Details_Table.column("checkin",width=100)
        self.Room_Details_Table.column("checkout",width=100)
        self.Room_Details_Table.column("roomtype",width=100)
        self.Room_Details_Table.column("roomavailable",width=100)
        self.Room_Details_Table.column("meal",width=100)
        self.Room_Details_Table.column("noofdays",width=100)
        
        self.Room_Details_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Room_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)



    def add_data(self):
      if self.var_contact.get() == "" or self.var_checkin == "":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into customerroom values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
            self.var_checkin.get(),
        self.var_checkout.get(),
        self.var_roomtype.get(),
        self.var_roomavailable.get(),
        self.var_meal.get(),
        self.var_no_of_days.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room Booked!!",parent=self.root)
        except Exception as e:
          messagebox.showerror("Warning","some thing went wrong",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customerroom")
        rows = my_cursor.fetchall()
        if(len(rows) !=0):
            self.Room_Details_Table.delete(*self.Room_Details_Table.get_children())
            for i in rows:
              self.Room_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()


    def fetch_customer_data(self):
            if self.var_contact.get() == "":
                messagebox.showerror("Error","Please Enter Your Contact Number",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
                my_cursor=conn.cursor()
                query=("select Name from customerdetails where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                # my_cursor.execute("select Name from customerdetails where Mobile=%s",self.var_contact.get())
                row=my_cursor.fetchone()
                

                if row == None:
                    messagebox.showerror("Error","This number is not Found",parent=self.root)
                else:
                    conn.commit()
                    conn.close()

                    # creating frame
                    text_frame=Frame(self.root,bd=5,relief=RAISED,bg="white")
                    text_frame.place(x=22,y=66,width=195,height=220)

                    lbl_Name=Label(text_frame,text="Name : ",font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_Name.place(x=10,y=10)

                    lbl_name1=Label(text_frame,text=row,font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_name1.place(x=80,y=10)

                    conn=mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
                    my_cursor=conn.cursor()
                    query=("select Email from customerdetails where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    # my_cursor.execute("select Name from customerdetails where Mobile=%s",self.var_contact.get())
                    row=my_cursor.fetchone()
                   

                    lbl_email=Label(text_frame,text="Email Id: ",font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_email.place(x=10,y=40)

                    lbl_email1=Label(text_frame,text=row,font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_email1.place(x=80,y=40)
                    conn.commit()
                    conn.close()

                    conn=mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
                    my_cursor=conn.cursor()
                    query=("select Idproof from customerdetails where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    # my_cursor.execute("select Name from customerdetails where Mobile=%s",self.var_contact.get())
                    row=my_cursor.fetchone()
                   

                    lbl_id_proof=Label(text_frame,text="Id Proof : ",font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_id_proof.place(x=10,y=70)

                    lbl_id_proof1=Label(text_frame,text=row[0],font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_id_proof1.place(x=80,y=70)
                    conn.commit()
                    conn.close()

                    # Refrence Number
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
                    my_cursor=conn.cursor()
                    query=("select Ref from customerdetails where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    # my_cursor.execute("select Name from customerdetails where Mobile=%s",self.var_contact.get())
                    row=my_cursor.fetchone()
                   

                    lbl_ref=Label(text_frame,text="Ref No. : ",font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_ref.place(x=10,y=100)

                    lbl_ref=Label(text_frame,text=row[0],font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_ref.place(x=80,y=100)
                    conn.commit()
                    conn.close()

                    # Address Number
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
                    my_cursor=conn.cursor()
                    query=("select Address from customerdetails where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    # my_cursor.execute("select Name from customerdetails where Mobile=%s",self.var_contact.get())
                    row=my_cursor.fetchone()
                   

                    lbl_address=Label(text_frame,text="Address : ",font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_address.place(x=10,y=130)

                    lbl_address1=Label(text_frame,text=row,font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_address1.place(x=80,y=130)
                    conn.commit()
                    conn.close()


                     # Id Number
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
                    my_cursor=conn.cursor()
                    query=("select Idnumber from customerdetails where Mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    # my_cursor.execute("select Name from customerdetails where Mobile=%s",self.var_contact.get())
                    row=my_cursor.fetchone()
                   

                    lbl_idnumber=Label(text_frame,text="Id number: ",font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_idnumber.place(x=10,y=160)

                    lbl_idnumber1=Label(text_frame,text=row,font=("arial",8,"bold"),padx=2,pady=4)
                    lbl_idnumber1.place(x=80,y=160)
                    conn.commit()
                    conn.close()

    def get_cursor(self,events):
      cursor_row = self.Room_Details_Table.focus()
      content = self.Room_Details_Table.item(cursor_row)
      row=content["values"]

      self.var_contact.set(row[0])
      self.var_checkin.set(row[1])
      self.var_checkout.set(row[2])
      self.var_roomtype.set(row[3])
      self.var_roomavailable.set(row[4])
      self.var_meal.set(row[5])
      self.var_no_of_days.set(row[6])

    def update(self):
      if self.var_contact=="" or self.var_checkin=="":
        messagebox.showerror("Error","please enter valid details",parent=self.root)
      else:
        conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("update customerroom set Check_in=%s,Check_out=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,No_of_days=%s where Contact=%s",(
            self.var_checkin.get(),
        self.var_checkout.get(),
        self.var_roomtype.get(),
        self.var_roomavailable.get(),
        self.var_meal.get(),
        self.var_no_of_days.get(),self.var_contact.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Room Details has been updated",parent=self.root)

    def delete(self):
      delitem = messagebox.askyesno("Question","Do you want to delete this customer",parent=self.root)
      if delitem>0:
        conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("delete from customerroom where Contact=%s",(self.var_contact.get(),))
       
      else:
        if not delitem:
          return

      conn.commit()
      self.fetch_data()
      conn.close()

    def reset(self):
      self.var_contact.set("")
      self.var_checkin.set("")
      self.var_checkout.set("")
      self.var_roomtype.set("")
      self.var_roomavailable.set("")
      self.var_meal.set("")
      self.var_no_of_days.set("")
      self.var_no_of_days.set("")
      self.var_paid_tax.set("")
      self.var_actual_bill.set("")
      self.var_total_bill.set("")

    def search(self):
      conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from customerroom where "+str(self.var_search.get())+" LIKE'%"+str(self.text_search.get())+"%'")
      rows=my_cursor.fetchall()
      if len(rows)!= 0:
        self.Room_Details_Table.delete(*self.Room_Details_Table.get_children())
        for i in rows:
          self.Room_Details_Table.insert("",END,values=i)
      conn.commit()
      conn.close()

      











                    


                    

        
       
        









        
        
if __name__ == "__main__":
    root = Tk()
    obj=Room_Booking(root)
    root.mainloop()
