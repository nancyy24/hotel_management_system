from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import random
# pip install mysql-connector-python
import mysql.connector
from tkinter import messagebox


class Customer_Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Details")
        self.root.geometry("1360x525+0+185")

        self.pwd="Nancy2403@"
    # creating variables
        self.var_ref=StringVar()
        x= random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()



    # adding the title
        lbl_title = Label(self.root,text="CUSTOMER DETAILS WINDOW",font=("Helvetica",24,"bold"),bg="light slate gray",fg="black",bd=4,relief=SOLID)
        lbl_title.place(x=0,y=0,width=1360,height=40)

        # creating frame
        main_frame=Frame(self.root,bd=5,relief=RAISED,bg="black")
        main_frame.place(x=0,y=40,width=250,height=485)


        # adding side image
        cust_side_img1=Image.open("Images\customer_details.png")
        cust_side_img1=cust_side_img1.resize((200,230),Image.ANTIALIAS)
        self.custsideimg1=ImageTk.PhotoImage(cust_side_img1)

        lblcustsideimg1 = Label(main_frame,image=self.custsideimg1,bd=4,relief=RAISED)
        lblcustsideimg1.place(x=15,y=15,width=200,height=230)

        # adding side image
        cust_side_img2=Image.open("Images\customer_details-1.jpg")
        cust_side_img2=cust_side_img2.resize((200,200),Image.ANTIALIAS)
        self.custsideimg2=ImageTk.PhotoImage(cust_side_img2)

        lblcustsideimg2 = Label(main_frame,image=self.custsideimg2,bd=4,relief=RAISED)
        lblcustsideimg2.place(x=15,y=260,width=200,height=200)

        # adding label frame
        frame1 = LabelFrame(self.root,bd=4,relief=RAISED,text="CUSTOMER DETAILS",font=("Helvetica",10,"bold"),bg="light slate gray",fg="black")
        frame1.place(x=250,y=40,width=1110,height=225)

        # LABELS AND ENTRIES
        # CustRef
        lbl_cust_ref=Label(frame1,text="Customer Ref",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.place(x=10,y=0,width=150)

        entry_ref=ttk.Entry(frame1,font=("arial",14),textvariable=self.var_ref,state="readonly")
        entry_ref.place(x=180,y=0,width=150)


        # vertical frame
        vertical = Frame(frame1, bg='black', height=50,width=1)
        vertical.place(x=350, y=10,height=150)

         # CUSTOMER NAME
        cname=Label(frame1,text="Customer Name",font=("arial",10,"bold"),padx=2,pady=4)
        cname.place(x=370,y=0,width=150)

        txtcname=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_cust_name)
        txtcname.place(x=540,y=0,width=150)

         # vertical frame
        vertical = Frame(frame1, bg='black', height=50,width=1)
        vertical.place(x=710, y=10,height=150)

        # MOTHER NAME
        lblmname=Label(frame1,text="Mother Name:",font=("arial",10,"bold"),padx=2,pady=4)
        lblmname.place(x=730,y=0,width=150)

        textmname=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_mother)
        textmname.place(x=890,y=0,width=150)

        # GENDER COMBOBOX
        label_gender=Label(frame1,text="Gender:",font=("arial",10,"bold"),padx=2,pady=4)
        label_gender.place(x=10,y=40,width=150)

        combo_gender=ttk.Combobox(frame1,font=("arial",14),width=20,state="readonly",textvariable=self.var_gender)
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.place(x=180,y=40,width=150)

        # POSTCODE
        lblPostCode=Label(frame1,text="PostCode",font=("arial",10,"bold"),padx=2,pady=4)
        lblPostCode.place(x=370,y=40,width=150)

        txtPostCode=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_post)
        txtPostCode.place(x=540,y=40,width=150)

        # MOBILE NUMBER
        lblMobile=Label(frame1,text="Mobile:",font=("arial",10,"bold"),padx=2,pady=4)
        lblMobile.place(x=730,y=40,width=150)

        textMobile=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_mobile)
        textMobile.place(x=890,y=40,width=150)

        # EMAIL
        lblEmail=Label(frame1,text="Email:",font=("arial",10,"bold"),padx=2,pady=4)
        lblEmail.place(x=10,y=80,width=150)

        txtMobile=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_email)
        txtMobile.place(x=180,y=80,width=150)

          # NATIONALITY
        lblNationality=Label(frame1,text="Nationality:",font=("arial",10,"bold"),padx=2,pady=4)
        lblNationality.place(x=370,y=80,width=150)

        combo_Nationality=ttk.Combobox(frame1,font=("arial",14),width=20,state="readonly",textvariable=self.var_nationality)
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.place(x=540,y=80,width=150)

        # IDPROOF TYPE COMBOBOX
        lblIdProof=Label(frame1,text="Id Proof Type:",font=("arial",10,"bold"),padx=2,pady=4)
        lblIdProof.place(x=730,y=80,width=150)

        combo_id=ttk.Combobox(frame1,font=("arial",14),width=20,state="readonly",textvariable=self.var_id_proof)
        combo_id["value"]=("Aadhaar Card","Driving License","Passport")
        combo_id.current(0)
        combo_id.place(x=890,y=80,width=150)

        # ID NUMBER
        lblIdNumber=Label(frame1,text="Id Number",font=("arial",10,"bold"),padx=2,pady=4)
        lblIdNumber.place(x=10,y=120,width=150)

        txtIdNumber=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_id_number)
        txtIdNumber.place(x=180,y=120,width=150)

         # ADDRESS
        lblAddress=Label(frame1,text="Address:",font=("arial",10,"bold"),padx=2,pady=4)
        lblAddress.place(x=370,y=120,width=150)

        txtAddress=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.var_address)
        txtAddress.place(x=540,y=120,width=150)

        # BUTTONS
        btn_frame=Frame(frame1,bd=2,relief=RIDGE)
        btn_frame.place(x=20,y=160,width=1050,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnAdd.place(x=150,y=3,width=150)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnUpdate.place(x=330,y=3,width=150)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnDelete.place(x=500,y=3,width=150)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnReset.place(x=680,y=3,width=150)

          # TABEL FRAME
        Table_Frame=LabelFrame(self.root,bd=4,relief=RAISED,text="VIEW DETAILS AND SEARCH SYSTEM",font=("arial",12,"bold"),padx=2,bg="grey")
        Table_Frame.place(x=250,y=268,width=1110,height=250)
        
        lblSearchBy=Label(Table_Frame,font=("arial",10,"bold"),text="Search By:",bg="red",fg="white",width=15)
        lblSearchBy.place(x=10,y=5,width=150)

        self.var_search=StringVar()
        combo_id=ttk.Combobox(Table_Frame,textvariable=self.var_search,font=("arial",10,"bold"),width=20,state="readonly")
        combo_id["value"]=("Mobile","Ref")
        combo_id.current(0)
        combo_id.place(x=170,y=5,width=150)

        self.text_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.text_search,font=("arial",11,"bold"),width=25)
        txtSearch.place(x=330,y=5,width=150)

        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnSearch.place(x=490,y=5,width=150)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.place(x=645,y=5,width=150)
        # # horizontal bar
        # horizontal =Frame(Table_Frame, bg='black', height=1,width=1050)
        # horizontal.place(x=50, y=35)
        
        # SHOW DATA TABLE
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=35,width=1100,height=200)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Reference No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
      if self.var_mobile.get() == "" or self.var_id_number == "":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into customerdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
              self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),
              self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","customer has been added",parent=self.root)
        except Exception as e:
          messagebox.showerror("Warning","some thing went wrong",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password=self.pwd,database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customerdetails")
        rows = my_cursor.fetchall()
        if(len(rows) !=0):
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
              self.Cust_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,events):
      cursor_row = self.Cust_Details_Table.focus()
      content = self.Cust_Details_Table.item(cursor_row)
      row=content["values"]

      self.var_ref.set(row[0])
      self.var_cust_name.set(row[1])
      self.var_mother.set(row[2])
      self.var_gender.set(row[3])
      self.var_post.set(row[4])
      self.var_mobile.set(row[5])
      self.var_email.set(row[6])
      self.var_nationality.set(row[7])
      self.var_id_proof.set(row[8])
      self.var_id_number.set(row[9])
      self.var_address.set(row[10])

    def update(self):
      if self.var_id_proof=="" or self.var_cust_name=="":
        messagebox.showerror("Error","please enter valid details",parent=self.root)
      else:
         conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
         my_cursor=conn.cursor()
         my_cursor.execute("update customerdetails set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
              self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),
              self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get()))
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("Update","Customer Details has benn updated")

    def delete(self):
      delitem = messagebox.askyesno("Question","Do you want to delete this customer",parent=self.root)
      if delitem>0:
        conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("delete from customerdetails where Ref=%s",(self.var_ref.get(),))
       
      else:
        if not delitem:
          return

      conn.commit()
      self.fetch_data()
      conn.close()
    
    def reset(self):
      # self.var_ref.set("")
      self.var_cust_name.set("")
      self.var_mother.set("")
      self.var_gender.set("")
      self.var_post.set("")
      self.var_mobile.set("")
      self.var_email.set("")
      self.var_nationality.set("")
      self.var_id_proof.set("")
      self.var_id_number.set("")
      self.var_address.set("")
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))

    def search(self):
      conn = mysql.connector.connect(host="localhost",username="root",password="Nancy2403@",database="hotel-managment-system")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from customerdetails where "+str(self.var_search.get())+" LIKE'%"+str(self.text_search.get())+"%'")
      rows=my_cursor.fetchall()
      if len(rows)!= 0:
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for i in rows:
          self.Cust_Details_Table.insert("",END,values=i)
      conn.commit()
      conn.close()


if __name__ == "__main__":
    root = Tk()
    obj=Customer_Details(root)
    root.mainloop()


