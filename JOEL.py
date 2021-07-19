from tkinter import *
import math,random
from tkinter import messagebox
import os
import smtplib
from PIL import Image,ImageTk
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen

class Bill_App:
    def __init__(self, master):
        self.master=master
        self.master.geometry("1920x1080+-10+0")
        self.master.title("SPORTs WEAR MANAGEMENT & BILLING SYSTEM")

        title=Label(self.master,text="JOEL SPORTs WEAR",bd=12,relief=GROOVE,bg="indian red1",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #    variable ---------------------------------------
        
        #   cricket variable
        self.bat=IntVar()
        self.cricketball=IntVar()
        self.gloves=IntVar()
        self.kitbag=IntVar()
        self.legpad=IntVar()
        self.cricketjersey=IntVar()
        
        # hockey varible
        self.hockeystick=IntVar()
        self.puck=IntVar()
        self.shoulderpads=IntVar()
        self.jockstrap=IntVar()
        self.shoes=IntVar()
        self.keepergloves=IntVar()
        
        # football drink
        self.soccerball=IntVar()
        self.uniform=IntVar()
        self.shinguard=IntVar()
        self.goalie=IntVar()
        self.gearbags=IntVar()
        self.prakits=IntVar()
        
        # volleyball varible 
        
        self.ball=IntVar()
        self.kneepad=IntVar()
        self.net=IntVar()
        self.shoe=IntVar()
        self.elbowpad=IntVar()
        self.anklebrace=IntVar()
        
        #product price varible
        
        self.cricket_price=StringVar()
        self.hockey_price=StringVar()
        self.football_price=StringVar()
        self.volleyball_price=StringVar()
        
        # tax varible
        
        self.cricket_tax=StringVar()
        self.hockey_tax=StringVar()
        self.football_tax=StringVar()
        self.volleyball_tax=StringVar()
        
        #bills details
        
        self.c_name=StringVar()
        self.c_cn=StringVar()
        self.c_mail=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        # admin
        self.admin_id=StringVar()
        self.admin_pass=StringVar()
        
        
        
        # ------------>>> BILL DETAILS <<<<<-----------------
        F0=LabelFrame(self.master,bd=10,relief=GROOVE,text="BILL DETAILS",font=("times new roman",15,"bold"),fg="BROWN",bg="YELLOW")
        F0.place(x=0,y=70,width=950)
        
        cname_label=Label(F0,text="CUSTOMER NAME",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=0,padx=10,pady=5)
        cname_txt=Entry(F0,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_label=Label(F0,text="CASHIER NAME",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=2,padx=10,pady=5)
        cphn_txt=Entry(F0,width=20,textvariable=self.c_cn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
         ################################ send email button
        F1=LabelFrame(self.master,bd=10,relief=GROOVE,text="Send the Bill via EMAIL",font=("times new roman",15,"bold"),fg="BROWN",bg="YELLOW")
        F1.place(x=920,y=70,width=587)
        
        cmail_label=Label(F1,text="Email-id",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=4,padx=10,pady=5)
        cmail_txt=Entry(F1,width=20,textvariable=self.c_mail,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        #bn_txt=Entry(F9,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        send_btn=Button(F1,text="SEND",command=self.check_mail,bg="red",bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=7) 

        
        #----------------->>>>> Cricket frame <<<----------------
        F2=LabelFrame(self.master,bd=10,relief=GROOVE,text="CRICKET",font=("times new roman",15,"bold"),fg="red4",bg="deep sky blue")
        F2.place(x=5,y=152,width=220,height=373)
        
        
        bt_txt=Entry(F2,width=2,textvariable=self.bat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        bt_label=Label(F2,text="Bat",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        
        cb_label=Label(F2,text="Cricket Ball",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cb_txt=Entry(F2,width=2,textvariable=self.cricketball,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        
        glv_label=Label(F2,text="Gloves",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        glv_txt=Entry(F2,width=2,textvariable=self.gloves,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        
        kb_Spry_label=Label(F2,text="Kit Bag",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        kb_spry_txt=Entry(F2,width=2,textvariable=self.kitbag,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
    
        pd_gel_label=Label(F2,text="Leg Pad",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        pd_gel_txt=Entry(F2,width=2,textvariable=self.legpad,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        
        jer_lt_label=Label(F2,text="Cricket Jersey",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        jer_lt_txt=Entry(F2,width=2,textvariable=self.cricketjersey,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        
        
         #----------------->>>>> Hockey frame <<<----------------
        F3=LabelFrame(self.master,bd=10,relief=GROOVE,text="HOCKEY",font=("times new roman",15,"bold"),fg="red4",bg="deep sky blue")
        F3.place(x=220,y=152,width=220,height=373)
        
        g1_label=Label(F3,text="Hockey Stick",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=2,textvariable=self.hockeystick,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        g2_label=Label(F3,text="Puck",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=2,textvariable=self.puck,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        g3_label=Label(F3,text="Shoulder Pads",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=2,textvariable=self.shoulderpads,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
            
        g4_label=Label(F3,text="Jock Strap",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=2,textvariable=self.jockstrap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        g5_label=Label(F3,text="Shoes",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=2,textvariable=self.shoes,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        g6_label=Label(F3,text="Keeper Gloves",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=2,textvariable=self.keepergloves,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
         
         #----------------->>>>> football frame <<<----------------
        F4=LabelFrame(self.master,bd=10,relief=GROOVE,text="FOOTBALL",font=("times new roman",15,"bold"),fg="red4",bg="deep sky blue")
        F4.place(x=440,y=152,width=220,height=373)
        
        c1_label=Label(F4,text="Soccer Ball",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=2,textvariable=self.soccerball,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F4,text="Uniform",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=2,textvariable=self.uniform,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F4,text="Shin Guard",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=2,textvariable=self.shinguard,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F4,text="Goalie Gloves",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=2,textvariable=self.goalie,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F4,text="Gear Bags",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=2,textvariable=self.gearbags,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F4,text="Practice Kits",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=2,textvariable=self.prakits,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        #----------------->>>>> Volleyball frame <<<----------------
        F4=LabelFrame(self.master,bd=10,relief=GROOVE,text="VOLLEYBALL",font=("times new roman",15,"bold"),fg="red4",bg="deep sky blue")
        F4.place(x=660,y=152,width=230,height=373)
        
        c1_label=Label(F4,text="Ball",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=2,textvariable=self.ball,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F4,text="Knee Pad",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=2,textvariable=self.kneepad,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F4,text="Shoe",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=2,textvariable=self.shoe,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F4,text="Net",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=2,textvariable=self.net,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F4,text="Elbow Pad",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=2,textvariable=self.elbowpad,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F4,text="Ankle Brace",font=("times new roman",12,"bold"),fg="black",bg="spring green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=2,textvariable=self.anklebrace,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        
        
        
        # bill Area ....................................
        
        F6=LabelFrame(self.master,bd=10,relief=RAISED,bg="maroon1")
        F6.place(x=890,y=152,width=480,height=360)
        bill_title=Label(F6,text="BILL AREA",font="arial 15 bold",bd=7,relief=RAISED,bg="seagreen1").pack(fill=X)
        
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #  bottom button frame----------------------------------
        
        F7=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="red4",bg="deep sky blue")
        F7.place(x=0,y=510,relwidth=1,height=160)
        
        m1=Label(F7,text="Total Cricket Price",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky=W)
        ml_txt=Entry(F7,width=18,textvariable=self.cricket_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F7,text="Total Hockey Price",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky=W)
        m2_txt=Entry(F7,width=18,textvariable=self.hockey_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F7,text="Total Football Price",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky=W)
        m3_txt=Entry(F7,width=18,textvariable=self.football_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m4=Label(F7,text="Total Volleyball Price",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=3,column=0,padx=10,pady=1,sticky=W)
        m4_txt=Entry(F7,width=18,textvariable=self.volleyball_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)

        # for tax
        
        tax1=Label(F7,text="Cricket Tax (6%)",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky=W)
        taxl_txt=Entry(F7,width=18,textvariable=self.cricket_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        tax2=Label(F7,text="Hockey Tax (5%)",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky=W)
        tax2_txt=Entry(F7,width=18,textvariable=self.hockey_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        tax3=Label(F7,text="Football Tax (7%)",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky=W)
        tax3_txt=Entry(F7,width=18,textvariable=self.football_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        tax4=Label(F7,text="Volleyball Tax (5%)",bg="seagreen3",fg="black",font=("times new roman",12,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky=W)
        tax4_txt=Entry(F7,width=18,textvariable=self.volleyball_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=1)


        btn_frame=Frame(F7,bd=7,relief=GROOVE)
        btn_frame.place(x=790,y=10,width=560,height=115)
        
        total_btn=Button(btn_frame,command=self.total,text="Total",bg="indian red",bd=5,fg="black",pady=15,width=10,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)

        genbill_btn=Button(btn_frame,text="Generate Bill",command=self.bill_area,bg="indian red",bd=5,fg="black",pady=15,width=10,font="arial 12 bold").grid(row=0,column=1,padx=10,pady=15)

        clear_btn=Button(btn_frame,text="Clear",command=self.clear_data,bg="indian red",bd=5,fg="black",pady=15,width=10,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=15)

        exit_btn=Button(btn_frame,text="Exit",command=self.exit_app,bg="indian red",bd=5,fg="black",pady=15,width=10,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=15)
        
        self.welcome_bill()
        
        #----------------->>>>> bill search frame <<<----------------
        F8=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Search ",font=("times new roman",15,"bold"),fg="gold",bg="firebrick1")
        F8.place(x=0,y=672,width=350,height=80)
        
        bn_txt=Entry(F8,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        search_btn=Button(F8,text="Search",command=self.find_bill,bg="tan1",bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=2)

           #---------------Admin area-----------------------
        F9=LabelFrame(self.master,bd=10,relief=GROOVE,text="ADMIN ZONE ",font=("times new roman",15,"bold"),fg="gold",bg="firebrick1")
        F9.place(x=351,y=672,width=1186,height=80)
            
        
        
        Label(F9,text="Login :  | ",font=("times new roman",15,"bold"),fg="black",bg="orchid").grid(row=0,column=0)
        Label(F9,text="ID ",font=("times new roman",15,"bold"),fg="black",bg="orchid").grid(row=0,column=1)
        
        admin_id1=Entry(F9,width=25,textvariable=self.admin_id,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=2,sticky=E)
        
        Label(F9,text="  Password",font=("times new roman",15,"bold"),fg="black",bg="orchid").grid(row=0,column=3)
        
        admin_pass1=Entry(F9,width=18,textvariable=self.admin_pass,font="arial 10 bold",bd=7,relief=SUNKEN,show='X').grid(row=0,column=4,sticky=E)
        
        a_login=Button(F9,text="Login",command=self.login_page,bg="orchid",bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=5,padx=35)
        
        
     # price given to the items
    
    def total(self):
        self.c_sp=self.bat.get()*1000
        self.c_fc=self.cricketball.get()*60
        self.c_fw=self.gloves.get()*500
        self.c_hsp=self.kitbag.get()*5000
        self.c_hg=self.legpad.get()*400
        self.c_bl=self.cricketjersey.get()*150
        self.total_cricket_price=float(
                self.c_sp+
                self.c_bl+
                self.c_fc+
                self.c_fw+
                self.c_hg+
                self.c_hsp
                )
        
        self.c_tax=round((self.total_cricket_price*0.6),2)
        self.cricket_price.set("Rs. "+str(self.total_cricket_price))
        self.cricket_tax.set("Rs. "+str(self.c_tax))
        
        
        
        self.g_mg=self.hockeystick.get()*1500
        self.g_rc=self.puck.get()*70
        self.g_wh=self.shoulderpads.get()*150
        self.g_sg=self.jockstrap.get()*200
        self.g_fol=self.shoes.get()*1000
        self.g_dl=self.keepergloves.get()*550
        
        self.total_hockey_price=float(
                self.g_dl+
                self.g_fol+
                self.g_mg+
                self.g_rc+
                self.g_sg+
                self.g_wh
                )
        self.g_tax=round((self.total_hockey_price*0.05),2)
        self.hockey_price.set("Rs. "+str(self.total_hockey_price))
        self.hockey_tax.set("Rs. "+str(self.g_tax))
        
        
        self.cd_mz=self.soccerball.get()*700
        self.cd_cc=self.uniform.get()*400
        self.cd_sl=self.shinguard.get()*150
        self.ccd_thu=self.goalie.get()*200
        self.cd_ft=self.gearbags.get()*5000
        self.cd_ps=self.prakits.get()*300
        
        self.total_football_price=float(
                self.cd_cc+
                self.cd_ft+
                self.cd_mz+
                self.cd_ps+
                self.cd_sl+
                self.ccd_thu
                )
        self.cd_tax=round((self.total_football_price*0.7),2)
        self.football_price.set("Rs. "+str(self.total_football_price))
        self.football_tax.set("Rs. "+str(self.cd_tax))
         
        self.bc_pr=self.ball.get()*1000
        self.bc_o=self.shoe.get()*700
        self.bc_mc=self.anklebrace.get()*250
        self.bc_bt=self.kneepad.get()*250
        self.bc_gd=self.net.get()*3000
        self.bc_sf=self.elbowpad.get()*240
        
        self.total_volleyball_price=float(
                self.bc_bt+
                self.bc_gd+
                self.bc_mc+
                self.bc_o+
                self.bc_pr+
                self.bc_sf
                )
        self.bc_tax=round((self.total_volleyball_price*0.05),2)
        self.volleyball_price.set("Rs. "+str(self.total_volleyball_price))
        self.volleyball_tax.set("Rs. "+str(self.bc_tax))
        
        self.total_bill=float(
                self.total_cricket_price+
                self.total_hockey_price+
                self.total_football_price+
                self.total_volleyball_price+
                self.c_tax+
                self.g_tax+
                self.cd_tax+
                self.bc_tax
                )
        
    def stock_update_after_purchased(self,name,n):
        f1=open("stock.csv","w+",encoding='utf-8-sig')
        for i in f1:
            data=i.split(",")
            if data[0]==name:
                if n<=int(data[1]):
                    x=int(data[1])
                    x=x-n
                    return n
        
        
        
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t|| JOEL SPORTs WEAR ||")
        self.txtarea.insert(END,"\n_________________________________________\n")
        self.txtarea.insert(END,f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name :   {self.c_name.get()}")
        self.txtarea.insert(END,f"\nCashier Name.:    {self.c_cn.get()}")
        self.txtarea.insert(END,"\n===================================================")
        self.txtarea.insert(END,"\nProducts\t\t       QTY  \t       Price")
        self.txtarea.insert(END,"\n===================================================")
        
        
    def bill_area(self):
       
       if self.c_name.get()=="" or self.c_cn.get()=="":
           messagebox.showerror("Error","Fill Bill details")
       elif self.cricket_price=="Rs. 0.0" and self.hockey_price=="Rs. 0.0" and self.football_price=="Rs. 0.0" and self.volleyball_price=="Rs. 0.0":
           messagebox.showerror("Error","No product purchased")
       else: 
           self.welcome_bill()
           # cricket
           if self.bat.get()!=0:
               self.txtarea.insert(END,f"\nBat          \t\t\t{self.bat.get()}\t    {self.c_sp}")
           if self.cricketball.get()!=0:
               self.txtarea.insert(END,f"\nCricketBall  \t\t\t{self.cricketball.get()}\t    {self.c_fw}")
           if self.gloves.get()!=0:
               self.txtarea.insert(END,f"\nGloves       \t\t\t{self.gloves.get()}\t    {self.c_fc}")
           if self.kitbag.get()!=0:
               self.txtarea.insert(END,f"\nKitBag       \t\t\t{self.kitbag.get()}\t    {self.c_hsp}")
           if self.legpad.get()!=0:
               self.txtarea.insert(END,f"\nLegPad       \t\t\t{self.legpad.get()}\t    {self.c_hg}")
           if self.cricketjersey.get()!=0:
               self.txtarea.insert(END,f"\nCricJersey   \t\t\t{self.cricketjersey.get()}\t    {self.c_bl}")
            
            # hockey print
           if self.hockeystick.get()!=0:
               self.txtarea.insert(END,f"\nHockyStick   \t\t\t{self.soccerball.get()}\t    {self.g_mg}")
           if self.puck.get()!=0:
               self.txtarea.insert(END,f"\nPuck         \t\t\t{self.puck.get()}\t    {self.g_rc}")
           if self.shoulderpads.get()!=0:
               self.txtarea.insert(END,f"\nShouldPads   \t\t\t{self.shoulderpads.get()}\t    {self.g_wh}")
           if self.jockstrap.get()!=0:
               self.txtarea.insert(END,f"\nJockStrap    \t\t\t{self.jockstrap.get()}\t    {self.g_fol}")
           if self.shoes.get()!=0:
               self.txtarea.insert(END,f"\nShoes        \t\t\t{self.shoes.get()}\t    {self.g_sg}")
           if self.keepergloves.get()!=0:
               self.txtarea.insert(END,f"\nKeepGloves   \t\t\t{self.keepergloves.get()}\t    {self.g_dl}")
    
            
            # volleyball print
           if self.ball.get()!=0:
               self.txtarea.insert(END,f"\nBall         \t\t\t{self.ball.get()}\t    {self.bc_pr}")
           if self.shoe.get()!=0:
               self.txtarea.insert(END,f"\nShoe         \t\t\t{self.shoe.get()}\t    {self.bc_o}")
           if self.kneepad.get()!=0:
               self.txtarea.insert(END,f"\nKneePad      \t\t\t{self.kneepad.get()}\t    {self.bc_bt}")
           if self.net.get()!=0:
               self.txtarea.insert(END,f"\nNet          \t\t\t{self.net.get()}\t    {self.bc_gd}")
           if self.elbowpad.get()!=0:
               self.txtarea.insert(END,f"\nElbowPad     \t\t\t{self.elbowpad.get()}\t    {self.bc_sf}")
           if self.anklebrace.get()!=0:
               self.txtarea.insert(END,f"\nAnkleBrace   \t\t\t{self.anklebrace.get()}\t    {self.bc_mc}")
            
            
            # football print
           if self.soccerball.get()!=0:
               self.txtarea.insert(END,f"\nSoccerBall   \t\t\t{self.soccerball.get()}\t    {self.cd_mz}")
           if self.uniform.get()!=0:
               self.txtarea.insert(END,f"\nUniform      \t\t\t{self.uniform.get()}\t    {self.cd_cc}")
           if self.shinguard.get()!=0:
               self.txtarea.insert(END,f"\nShinGuard    \t\t\t{self.shinguard.get()}\t    {self.cd_sl}")
           if self.goalie.get()!=0:
               self.txtarea.insert(END,f"\nGoalieGloves \t\t\t{self.goalie.get()}\t    {self.ccd_thu}")
           if self.gearbags.get()!=0:
               self.txtarea.insert(END,f"\nGearBags     \t\t\t{self.gearbags.get()}\t    {self.cd_ps}")
           if self.prakits.get()!=0:
               self.txtarea.insert(END,f"\nPracticeKits \t\t\t{self.prakits.get()}\t    {self.cd_ft}")
            
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           if self.cricket_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nCricket Tax \t\t\t       {self.cricket_tax.get()}")
           if self.hockey_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nHockey  Tax \t\t\t       {self.hockey_tax.get()}")
           if self.volleyball_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nVolleyball Tax\t\t\t       {self.volleyball_tax.get()}")
           if self.football_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nFootball  Tax \t\t\t      {self.football_tax.get()}")
           
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           self.txtarea.insert(END,f"\nTotalBill :\t\t\t      Rs. {str(self.total_bill)}") 
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           
           self.save_bill()
       
    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save the bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
            fp1.write(self.bill_data)
            fp1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved successfuly")
        else:
            return 
    
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,f1.read())
                f1.close()
                present="yes"
                
                
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

        
    def clear_data(self):
        #   cricket variable
        op=messagebox.askyesno("Clear","Do you want to Clear")
        if op>0:
            self.bat.set(0)
            self.cricketball.set(0)
            self.gloves.set(0)
            self.kitbag.set(0)
            self.legpad.set(0)
            self.cricketjersey.set(0)
            
            # hockey varible
            self.hockeystick.set(0)
            self.puck.set(0)
            self.shoulderpads.set(0)
            self.jockstrap.set(0)
            self.shoes.set(0)
            self.keepergloves.set(0)
            
            # football variable
            self.soccerball.set(0)
            self.uniform.set(0)
            self.shinguard.set(0)
            self.goalie.set(0)
            self.gearbags.set(0)
            self.prakits.set(0)
            
            # volleyball varible 
            
            self.ball.set(0)
            self.kneepad.set(0)
            self.net.set(0)
            self.shoe.set(0)
            self.elbowpad.set(0)
            self.anklebrace.set(0)
            
            # product price varible
            
            self.cricket_price.set("")
            self.hockey_price.set("")
            self.football_price.set("")
            self.volleyball_price.set("")
            
            # tax varible
            
            self.cricket_tax.set("")
            self.hockey_tax.set("")
            self.football_tax.set("")
            self.volleyball_tax.set("")
            
            #customer details
            
            self.c_name.set("")
            self.c_cn.set("")
            self.c_mail.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.welcome_bill()
    
        else:
            return
                
        
    def exit_app(self):
        op1=messagebox.askyesno("Exit","Do you want to Exit")
        if op1>0:
            root.destroy()
        else:
            return
    
    def check_mail(self):
        txt_msg= self.send_email_bill()
        messagebox.showinfo("Sent",f"Bill No. :{self.bill_no.get()} Sent successfuly")
        
        
    def send_email_bill(self):
         get_3 = self.c_mail.get()
         store_get_3 = get_3
        
         op=messagebox.askyesno("Send bill","Do you want to Send the bill ?")
         if op>0:
             self.bill_data=self.txtarea.get('1.0',END)
             fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
             msg=self.bill_data
         else:
             return  
         get_4 = msg
         store_get_4 = get_4
    
        
         try:
             server = smtplib.SMTP('smtp.gmail.com', 587)
             server.ehlo()
             server.starttls()
             server.login("joedummy14@gmail.com","rqgabrlzchmahflj") # you should enter your email and password
             server.sendmail("joedummy@gmail.com",store_get_3,store_get_4)
             statement_1 = "MAIL HAS BEEN SENT"
             return statement_1
         except:
             statement_2 = "SOMETHING WENT WRONG"
             return statement_2
    def login_page(self):
        ad_id=self.admin_id.get()
        ad_pass=self.admin_pass.get()
        if(ad_id=="JOEL"):
            if(ad_pass=="JOEL"):
                global login_window
                login_window=Tk()
                
                obj1=login_page_window(login_window)
                
                
                
                login_window.mainloop()
            else:
                messagebox.showerror("Error","invalid password")
        else:
            messagebox.showerror("Error","invalid User id")
                
class login_page_window:
    def __init__(self, master1):
        self.master1=master1
        self.master1.geometry("1920x1080+-10+0")
        self.master1.title("ADMIN ZONE")

        title=Label(self.master1,text="JOEL SPORTs WEAR",bd=12,relief=GROOVE,bg="indianred1",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        F0=LabelFrame(self.master1,bd=10,relief=GROOVE,bg="yellow")
        F0.place(x=0,y=73,height=60,width=1370)
        ad_title=Label(F0,text="ADMIN ZONE",font="arial 15 bold",bd=10,relief=FLAT,bg="YELLOW").pack(fill=X)

        F1=LabelFrame(self.master1,bd=10,relief=RAISED,text="MENU",font=("times new roman",15,"bold"),fg="TURQUOISE1",bg="SlateBlue1")
        F1.place(x=0,y=133,width=230,height=600)
        
        
        stock=Button(F1,text="Stock",command=self.check_stock,bg="orchid",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=1,column=0,padx=10,pady=15)
        
        update_stock=Button(F1,text="Update Stock",command=self.Update_stock,bg="orchid",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=2,column=0,padx=10,pady=15)
        
        lis_of_bill=Button(F1,text="Bill List",command=self.bill_list,bg="orchid",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=3,column=0,padx=10,pady=15)
        
        clear=Button(F1,text="Clear",command=self.clear_admin_notebook,bg="orchid",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=4,column=0,padx=10,pady=15)
        
        
        
        F3=LabelFrame(self.master1,bd=10,text="Bottom",relief=GROOVE,bg="GREEN")
        F3.place(x=0,y=733,width=1537,height=60)
        
    
    
        #........................# Datapad Area # ....................................
        
        F4=LabelFrame(self.master1,bd=10,relief=RAISED ,bg="MAROON1")
        F4.place(x=295,y=133,width=800,height=600)
        bill_title=Label(F4,text="DATA PAD",font="arial 15 bold",bd=10,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.welcome_bill_admin()

        

    def welcome_bill_admin(self):
            
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\t\t\t\t\t|| JOEL SPORTs WEAR ||")
            self.txtarea.insert(END,"\n_________________________________________________________________________________________\n")
    def check_stock(self):
        
        self.txtarea.delete('1.0',END)
        
        self.welcome_bill_admin()
        
        f1=open("stock.csv","r",encoding='utf-8-sig')
        
        #self.txtarea.insert(END,f1.read())
        self.txtarea.insert(END,"|| Product || \t\t\t\t\t\t||Quantity||")
        self.txtarea.insert(END,"\n_________________________________________________________________________________________\n")
        for i in f1:
            data=i.split(",")
            print((data[0],data[1]))
            
            self.txtarea.insert(END,"\n"+data[0]+"\t\t\t\t\t\t"+data[1])
        
        f1.close()
    def clear_admin_notebook(self):
        self.txtarea.delete('1.0',END)
        self.welcome_bill_admin()
    
    def bill_list(self):
        
        j=1 
        self.txtarea.insert(END,"S.No.\t Bill \n\n")
        for i in os.listdir("bills/"):
           self.txtarea.insert(END,str(j)+".\t"+str(i)+"\n\n")
           j+=1
    def Update_stock(self):           
         p=Popen('stock.csv',shell=True)       
        
        
        
global root       
root=Tk()

#obj=login_page_window(root)       
obj = Bill_App(root)
root.mainloop()
