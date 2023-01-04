from tkinter import *
from PIL import Image,ImageTk 
from customerDetails import Customer_Details
from room import Room_Booking 

# homepage
class HotelManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1360x750")

        # logo
        img1=Image.open("Images\logo.jpg")
        img1=img1.resize((200,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=200,height=100)

        # title
        lbl_title = Label(self.root,text="Hotel Manangement Application",font=("Helvetica",40,"bold"),bg="light slate gray",fg="black",bd=4,relief=SOLID)
        lbl_title.place(x=200,y=0,width=1160,height=100)

        # creating frame
        main_frame=Frame(self.root,bd=5,relief=RAISED)
        main_frame.place(x=0,y=100,width=1355,height=605)

        # creating button frame
        btn_frame=Frame(main_frame,bd=5,relief=RAISED,bg="black")
        btn_frame.place(x=0,y=0,width=1350,height=50)

        # creating buttons
        customer_btn= Button(btn_frame,text="CUSTOMER DETAILS",command=self.customer_details_system,width=22,font=("Helvetica",14,"bold"),bg="light grey",fg="black",bd=2,cursor="hand1")
        customer_btn.place(x=0,y=0,height=40)

        customer_btn= Button(btn_frame,text="ROOM BOOKING",command=self.room_booking,width=22,font=("Helvetica",14,"bold"),bg="light grey",fg="black",bd=2,cursor="hand1")
        customer_btn.place(x=280,y=0,height=40)

        customer_btn= Button(btn_frame,text="ROOM DETAILS",width=22,font=("Helvetica",14,"bold"),bg="light grey",fg="black",bd=2,cursor="hand1")
        customer_btn.place(x=560,y=0,height=40)

        customer_btn= Button(btn_frame,text="ABOUT US",width=22,font=("Helvetica",14,"bold"),bg="light grey",fg="black",bd=2,cursor="hand1")
        customer_btn.place(x=840,y=0,height=40)

        customer_btn= Button(btn_frame,text="LOG OUT",width=17,font=("Helvetica",14,"bold"),bg="light grey",fg="black",bd=2,cursor="hand1")
        customer_btn.place(x=1120,y=0,height=40)

        # adding images to main frame
        # side image 1
        side_img1=Image.open("Images\hotel-2.jpg")
        side_img1=side_img1.resize((300,450),Image.ANTIALIAS)
        self.photosideimg1=ImageTk.PhotoImage(side_img1)

        lblsideimg1 = Label(main_frame,image=self.photosideimg1,bd=4,relief=RAISED)
        lblsideimg1.place(x=0,y=50,width=300,height=270)

        # side image 2
        side_img2=Image.open("Images\hotel-3.jpg")
        side_img2=side_img2.resize((300,450),Image.ANTIALIAS)
        self.photosideimg2=ImageTk.PhotoImage(side_img2)

        lblsideimg2 = Label(main_frame,image=self.photosideimg2,bd=5,relief=RAISED)
        lblsideimg2.place(x=0,y=325,width=300,height=270)

        # middle image
        middle_img2=Image.open("Images\hotel-1.jpg")
        middle_img2=middle_img2.resize((750,600),Image.ANTIALIAS)
        self.middleimg2=ImageTk.PhotoImage(middle_img2)

        lblmiddleimg2 = Label(main_frame,image=self.middleimg2,bd=5,relief=RAISED)
        lblmiddleimg2.place(x=300,y=50,width=750,height=600)

        # right side images
        side_img3=Image.open("Images\hotel-4.jpg")
        side_img3=side_img3.resize((300,450),Image.ANTIALIAS)
        self.photosideimg3=ImageTk.PhotoImage(side_img3)

        lblsideimg3 = Label(main_frame,image=self.photosideimg3,bd=4,relief=RAISED)
        lblsideimg3.place(x=1050,y=50,width=300,height=270)

        side_img4=Image.open("Images\hotel-5.jpg")
        side_img4=side_img4.resize((300,450),Image.ANTIALIAS)
        self.photosideimg4=ImageTk.PhotoImage(side_img4)

        lblsideimg4 = Label(main_frame,image=self.photosideimg4,bd=4,relief=RAISED)
        lblsideimg4.place(x=1050,y=322,width=300,height=270)


    def customer_details_system(self):
        self.customer_window = Toplevel(self.root)
        self.app = Customer_Details(self.customer_window)

    
    def room_booking(self):
        self.room_booking_window=Toplevel(self.root)
        self.application = Room_Booking(self.room_booking_window)


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
