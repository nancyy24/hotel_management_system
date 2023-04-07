from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import random
# pip install mysql-connector-python
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime


class About_Us:
    def __init__(self,root):
        self.root=root
        self.root.title("ABOUT US")
        self.root.geometry("1360x525+0+185")

        # adding the title
        lbl_title = Label(self.root,text="ABOUT US",font=("Helvetica",17,"bold"),bg="light slate gray",fg="black",bd=4,relief=SOLID)
        lbl_title.place(x=0,y=0,width=1360,height=40)

        # left frame
        left_frame=Frame(self.root,bd=5,relief=RAISED)
        left_frame.place(x=0,y=40,width=278,height=605)
        # side image 1
        side_img1=Image.open("Images\hotel-2.jpg")
        side_img1=side_img1.resize((270,230),Image.ANTIALIAS)
        self.photosideimg1=ImageTk.PhotoImage(side_img1)

        lblsideimg1 = Label(left_frame,image=self.photosideimg1,bd=4,relief=RAISED)
        lblsideimg1.place(x=0,y=0,width=270,height=230)

        # side image 2
        side_img2=Image.open("Images\hotel-3.jpg")
        side_img2=side_img2.resize((270,240),Image.ANTIALIAS)
        self.photosideimg2=ImageTk.PhotoImage(side_img2)

        lblsideimg2 = Label(left_frame,image=self.photosideimg2,bd=5,relief=RAISED)
        lblsideimg2.place(x=0,y=230,width=270,height=240)

        # right frame
        right_frame=Frame(self.root,bd=5,relief=RAISED)
        right_frame.place(x=1050,y=40,width=309,height=605)
        # side image 1
        side_img3=Image.open("Images\hotel-2.jpg")
        side_img3=side_img3.resize((300,230),Image.ANTIALIAS)
        self.photosideimg3=ImageTk.PhotoImage(side_img3)

        lblsideimg3 = Label(right_frame,image=self.photosideimg3,bd=4,relief=RAISED)
        lblsideimg3.place(x=0,y=0,width=300,height=230)

        # side image 2
        side_img4=Image.open("Images\hotel-3.jpg")
        side_img4=side_img4.resize((300,240),Image.ANTIALIAS)
        self.photosideimg4=ImageTk.PhotoImage(side_img4)

        lblsideimg4 = Label(right_frame,image=self.photosideimg4,bd=5,relief=RAISED)
        lblsideimg4.place(x=0,y=230,width=300,height=240)

        # Middle frame
        middle_frame=Frame(self.root,bd=5,relief=RAISED)
        middle_frame.place(x=280,y=40,width=809,height=605)

        # # CUSTOMER NAME
        # cname=Label(middle_frame,text="",font=("arial",10,"bold"),padx=2,pady=4)
        # cname.place(x=0,y=0)

        T = Text(middle_frame, height = 605, width = 809,font=("times roman",14))
        T.pack(padx=10,pady=10)
        Fact="Alongside comfortable guest rooms and suites in the Hotel Ace, the Gallery Tower’s stunningly chic accommodations allow you to lose yourself in downtown and  desert views, ultramodern amenities, and personalized service. Join us within our premier collection of 100% non-smoking guest rooms and suites for an experience that won't disappoint.Our rooms are designed to transport you into an environment made for leisure.\n Take your mind off the day-to-day of home life and find a  private paradise.From concerts and magic shows to laughs with Delirious Comedy Club, The Ace Hotel offers visitors an outstanding calendar of  events year-round. Check our calendar for the latest and greatest in upcoming entertainment.\n The fusion of offbeat attractions, neon cityscape, and urban energy in our Hotel is the spirit that inspires Hotel. With so many new things to see and experience, it can be hard to choose what to do first (FOMO, right?). So, we’ve put together a little guide to help you plan the most unforgettable trip, just steps away from the world-famous hotel Experience.\nWhether you’re planning an intimate rehearsal dinner for friends and family, a corporate meeting and retreat for your team, or an unforgettable block party for up to 2,000 guests, The Ace Hotel features phenomenal event spaces to offer you and your group a greater gathering. "
        T.insert(END, Fact)
        







if __name__ == "__main__":
    root = Tk()
    obj=About_Us(root)
    root.mainloop()
