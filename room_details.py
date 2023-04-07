from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import random
# pip install mysql-connector-python
import mysql.connector
from tkinter import messagebox
from time import strptime
from datetime import datetime

class Room_Details:
    def __init__(self,root):
        self.root=root
        self.root.title("ROOM Details Window")
        self.root.geometry("1360x525+0+185")

        self.pwd="Nancy2403@"

        # adding the title
        lbl_title = Label(self.root,text="All ROOM DETAILS WINDOW",font=("Helvetica",17,"bold"),bg="light slate gray",fg="black",bd=4,relief=SOLID)
        lbl_title.place(x=0,y=0,width=1360,height=40)

         # creating frame
        main_frame=Frame(self.root,bd=5,relief=RAISED,bg="black")
        main_frame.place(x=0,y=40,width=250,height=485)


        # adding side image
        cust_side_img1=Image.open("Images\hotelroom-3.jpg")
        cust_side_img1=cust_side_img1.resize((200,230),Image.ANTIALIAS)
        self.custsideimg1=ImageTk.PhotoImage(cust_side_img1)

        lblcustsideimg1 = Label(main_frame,image=self.custsideimg1,bd=4,relief=RAISED)
        lblcustsideimg1.place(x=15,y=15,width=200,height=230)

        # adding side image
        cust_side_img2=Image.open("Images\hotelroom-4.jpg")
        cust_side_img2=cust_side_img2.resize((200,200),Image.ANTIALIAS)
        self.custsideimg2=ImageTk.PhotoImage(cust_side_img2)

        lblcustsideimg2 = Label(main_frame,image=self.custsideimg2,bd=4,relief=RAISED)
        lblcustsideimg2.place(x=15,y=260,width=200,height=200)


        # adding label frame
        frame1 = LabelFrame(self.root,bd=4,relief=RAISED,text="ROOM DETAILS",font=("Helvetica",10,"bold"),bg="light slate gray",fg="black")
        frame1.place(x=250,y=40,width=1110,height=120)

        # LABELS AND ENTRIES

        # Floor
        self.floor = StringVar()
        lbl_floor=Label(frame1,text="Floor No.",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_floor.place(x=10,y=0,width=150)

        entry_floor=ttk.Entry(frame1,font=("arial",14),textvariable=self.floor)
        entry_floor.place(x=180,y=0,width=150)


        # vertical frame
        vertical = Frame(frame1, bg='black', height=50,width=1)
        vertical.place(x=350, y=6,height=20)

         # Room No
        self.room_no = StringVar()
        lbl_room_no=Label(frame1,text="Room No.",font=("arial",10,"bold"),padx=2,pady=4)
        lbl_room_no.place(x=370,y=0,width=150)

        entry_room_no=ttk.Entry(frame1,font=("arial",14),width=20,textvariable=self.room_no)
        entry_room_no.place(x=540,y=0,width=150)

         # vertical frame
        vertical = Frame(frame1, bg='black', height=50,width=1)
        vertical.place(x=710, y=6,height=20)

        # # Room type
        # lbl_room_type=Label(frame1,text="Room Type",font=("arial",10,"bold"),padx=2,pady=4)
        # lbl_room_type.place(x=730,y=0,width=150)

        # entry_room_type=ttk.Entry(frame1,font=("arial",14),width=20)
        # entry_room_type.place(x=890,y=0,width=150)

        # Room type COMBOBOX
        self.room_type=StringVar()
        label_room_type=Label(frame1,text="Room Type",font=("arial",10,"bold"),padx=2,pady=4)
        label_room_type.place(x=730,y=0,width=150)

        combo_room_type=ttk.Combobox(frame1,textvariable=self.room_type,font=("arial",14),width=20,state="readonly")
        combo_room_type["value"]=("Single","Double","Luxuxry")
        combo_room_type.current(0)
        combo_room_type.place(x=890,y=0,width=150)

        # BUTTONS
        btn_frame=Frame(frame1,bd=2,relief=RIDGE)
        btn_frame.place(x=150,y=40,width=700,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnAdd.place(x=20,y=3,width=150)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnUpdate.place(x=190,y=3,width=150)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",10,"bold"),bg="black",fg="gold",width=15)
        btnDelete.place(x=360,y=3,width=150)
        
        btnReset=Button(btn_frame,text="Reset",font=("arial",10,"bold"),command=self.reset,bg="black",fg="gold",width=15)
        btnReset.place(x=530,y=3,width=150)

          # TABEL FRAME
        Table_Frame=LabelFrame(self.root,bd=4,relief=RAISED,text="ROOM DETAILS WINDOW",font=("arial",12,"bold"),padx=2,bg="grey")
        Table_Frame.place(x=250,y=160,width=1110,height=360)
        
        # SHOW DATA TABLE
        room_type_details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        room_type_details_table.place(x=50,y=20,width=1000,height=300)

        scroll_x=ttk.Scrollbar(room_type_details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(room_type_details_table,orient=VERTICAL)

        self.room_type_details_table=ttk.Treeview(room_type_details_table,column=("floor","room_no",'room_type'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_type_details_table.xview)
        scroll_y.config(command=self.room_type_details_table.yview)

        self.room_type_details_table.heading("floor",text="Floor")
        self.room_type_details_table.heading("room_no",text="Room No")
        self.room_type_details_table.heading("room_type",text="Room Type")

        self.room_type_details_table["show"]="headings"
        
        self.room_type_details_table.column("floor",width=100)
        self.room_type_details_table.column("room_no",width=100)
        self.room_type_details_table.column("room_type",width=100)
        
        self.room_type_details_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_type_details_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
      if self.floor.get() == "" or self.room_type.get() == "" or self.room_no.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password=self.pwd,database="hotel-managment-system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into roomdetails values(%s,%s,%s)",(self.floor.get(),
            self.room_no.get(),self.room_type.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room has been added",parent=self.root)
        except Exception as e:
          messagebox.showerror("Warning","some thing went wrong",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password=self.pwd,database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from roomdetails")
        rows = my_cursor.fetchall()
        if(len(rows) !=0):
            self.room_type_details_table.delete(*self.room_type_details_table.get_children())
            for i in rows:
              self.room_type_details_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,events):
      cursor_row = self.room_type_details_table.focus()
      content = self.room_type_details_table.item(cursor_row)
      row=content["values"]
      self.floor.set(row[0])
      self.room_no.set(row[1])
      self.room_type.set(row[2])

    def update(self):
      if self.floor.get() == "" or self.room_type.get() == "" or self.room_no.get()=="":
        messagebox.showerror("Error","please enter valid details",parent=self.root)
      else:
         conn = mysql.connector.connect(host="localhost",username="root",password=self.pwd,database="hotel-managment-system")
         my_cursor=conn.cursor()
         my_cursor.execute("update roomdetails set Floor=%s,Room_type=%s where Room_No=%s",(
              self.floor.get(),self.room_type.get(),self.room_no.get()))
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("Update","Customer Details has been updated",parent=self.root)

    def delete(self):
      delitem = messagebox.askyesno("Question","Do you want to delete this Room",parent=self.root)
      if delitem>0:
        conn = mysql.connector.connect(host="localhost",username="root",password=self.pwd,database="hotel-managment-system")
        my_cursor=conn.cursor()
        my_cursor.execute("delete from roomdetails where Room_No=%s",(self.room_no.get(),))
       
      else:
        if not delitem:
          return

      conn.commit()
      self.fetch_data()
      conn.close()
    
    def reset(self):
      self.floor.set("")
      self.room_no.set("")
      self.room_type.set("")



        








        
if __name__ == "__main__":
    root = Tk()
    obj=Room_Details(root)
    root.mainloop()
