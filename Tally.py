
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
##from tkcalendar import Calendar, DateEntry
from tkinter import ttk

def Gatewayoftally():
    
        global Canvas1
        Canvas1 = tk.Canvas( background="white", relief="ridge",bd=0)
        Canvas1.place(relx=0, rely=0.07, relheight=0.960, relwidth=.900)
        Label5 = Label(Canvas1,text='Gateway of Tally',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

        Label5 = Label(Canvas1,text='CURRENT PERIOD',borderwidth="0", width=5, background="white",
                                            foreground="#4B77BE",font="-family {Segoe UI} -size 10 ")
        Label5.place(x=20, y=50, relheight=0.05, relwidth=0.100)
        Label5 = Label(Canvas1,text='CURRENT DATE',borderwidth="0", width=5, background="white",
                                            foreground="#4B77BE",font="-family {Segoe UI} -size 10 ")
        Label5.place(x=500, y=50, relheight=0.05, relwidth=0.100)
        Label5 = Label(Canvas1,text='1-Apr-22 to 31-Mar-23',borderwidth="0", width=5, background="white",
                                            foreground="black",font="-family {Segoe UI} -size 10 ")
        Label5.place(x=0, y=80, relheight=0.05, relwidth=0.150)
        btn2=Button(Canvas1,text='Friday, 1-Apr-2022',borderwidth="0",background="white",
                                     foreground="black",font=" -size 10 ")
        btn2.place(x=460, y=85, relheight=0.04, relwidth=0.150)

        global Frame2
        Frame2 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame2.place(x=0, y=300, relheight=0.620, width=652)
        # Using treeview widget
        treev = ttk.Treeview(Frame2, selectmode ='browse')
        # Calling pack method w.r.to treeview
        treev.place(relx=0, rely=0, height=400, relwidth=0.999)
         
        # Inserting the items and their features to the
        # columns built
        treev.insert("", 'end', text ="L1",
                     values =("Nidhi", "F", "25"))
        treev.insert("", 'end', text ="L2",
                     values =("Nisha", "F", "23"))
        treev.insert("", 'end', text ="L3",
                     values =("Preeti", "F", "27"))
        treev.insert("", 'end', text ="L4",
                     values =("Rahul", "M", "20"))
        treev.insert("", 'end', text ="L5",
                     values =("Sonu", "F", "18"))
        treev.insert("", 'end', text ="L6",
                     values =("Rohit", "M", "19"))
        treev.insert("", 'end', text ="L7",
                     values =("Geeta", "F", "25"))
        treev.insert("", 'end', text ="L8",
                     values =("Ankit", "M", "22"))
        treev.insert("", 'end', text ="L10",
                     values =("Mukul", "F", "25"))
        treev.insert("", 'end', text ="L11",
                     values =("Mohit", "M", "16"))
        treev.insert("", 'end', text ="L12",
                     values =("Vivek", "M", "22"))
        treev.insert("", 'end', text ="L13",
                     values =("Suman", "F", "30"))

        # Separator object
        separator = ttk.Separator(Canvas1, orient='vertical')
        separator.place(x=650, y=20, relwidth=0, relheight=1)
        
        global Frame1
        Frame1 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame1.place(x=800, y=200, relheight=0.620, relwidth=.220)
        Label5 = Label(Frame1,text='Gateway of Tally',borderwidth="0", width=5, background="blue",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0, rely=0, relheight=0.05, relwidth=0.999)
        Label5 = Label(Frame1,text='MASTERS',borderwidth="0", width=5, background="#e6ffff",
                                            foreground="#89C4F4",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(x=0, y=50, relheight=0.05, relwidth=0.999)
        btn1=Button(Frame1,text='Create',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn1.place(x=0, y=80, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame1,text='Alter',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn2.place(x=0, y=98, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn3=Button(Frame1,text='CHart of Accounts',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn3.place(x=0, y=118, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        Label5 = Label(Frame1,text='TRANSACTIONS',borderwidth="0", width=5, background="#e6ffff",
                                            foreground="#89C4F4",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(x=0, y=150, relheight=0.05, relwidth=0.999)
        btn4=Button(Frame1,text='Vouchers',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn4.place(x=0, y=178, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame1,text='Day BooK',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn5.place(x=0, y=198, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        Label5 = Label(Frame1,text='UTILITIES',borderwidth="0", width=5, background="#e6ffff",
                                            foreground="#89C4F4",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(x=0, y=230, relheight=0.05, relwidth=0.999)
        btn6=Button(Frame1,text='BanKing',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn6.place(x=0, y=258, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        Label5 = Label(Frame1,text='REPORTS',borderwidth="0", width=5, background="#e6ffff",
                                            foreground="#89C4F4",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(x=0, y=288, relheight=0.05, relwidth=0.999)
        btn7=Button(Frame1,text='Balanc Sheet',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn7.place(x=0, y=318, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        btn8=Button(Frame1,text='Profit & Loss A/C',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn8.place(x=0, y=337, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn8=Button(Frame1,text='Stock Summary',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn8.place(x=0, y=355, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame1,text='Ratio Analysis',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn9.place(x=0, y=374, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        btn10=Button(Frame1,text='Display More Reports',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn10.place(x=0, y=405, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn10['background'] = 'yellow'
        def on_leave(e):
            btn10['background'] = '#e6ffff'
        btn10.bind("<Enter>", on_enter)
        btn10.bind("<Leave>", on_leave)
        btn11=Button(Frame1,text='Quit',borderwidth="0",background="#e6ffff",
                                     foreground="black",font=" -size 10 ")
        btn11.place(x=0, y=455, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn11['background'] = 'yellow'
        def on_leave(e):
            btn11['background'] = '#e6ffff'
        btn11.bind("<Enter>", on_enter)
        btn11.bind("<Leave>", on_leave)
      
       
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black",bd=0, relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.95, relwidth=0.130)
        # Create a Button
        btn = Button(Canvas3, text = 'F2:Date', bd = '0',background="white",
                        font="-family {Segoe UI} -size 12  ",foreground="black",anchor="w")
        btn.place(x=5, y=5, height=30, width=153)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=160, y=5, height=30, width=20)
        btn = Button(Canvas3, text = 'F2:Company', bd = '0',background="white",
                        font="-family {Segoe UI} -size 12  ",foreground="black",command=ChangeCompany,anchor="w")
        btn.place(x=5, y=40, height=30, width=153)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=160, y=40, height=30, width=20)
        

##def ChangeDate():
##    
##        global Canvas4
##        Canvas4 = tk.Canvas( background="#B0B0B0", relief="ridge")
##        Canvas4.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
##        Label5 = Label(Canvas4,text='Change Current Date',borderwidth="0", width=5, background="#3385ff",
##                                            foreground="#00254a",
##                                            font="-family {Segoe UI} -size 10 -weight bold ")
##        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)
##
##
##        global Canvas5
##        Canvas5 = tk.Canvas(Canvas4, background="white",borderwidth="1", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
##        Canvas5.place(x=270, rely=0.300, relheight=0.300, relwidth=0.600)
##        Label11 = Label(Canvas5,text='Current Date',borderwidth="0", width=8, background="white",
##                                            foreground="black",
##                                            font="-family {Segoe UI} -size 12  -weight bold ")
##        Label11.place(x=300, rely=0.03, relheight=0.15, relwidth=0.250)
##        Entry2 = DateEntry(Canvas5, width= 16, background= "magenta3", foreground= "white",bd=2)
##        Entry2.place(x=280, rely=0.23, relheight=0.15, relwidth=0.600)
##        Label17 = Label(Canvas5,text='You will receive an e-mail with a link to reset password',borderwidth="0", width=8, background="white",
##                                            foreground="black",
##                                            font="-family {Helvetica} -size 12 -slant italic ")
##        Label17.place(x=320, rely=0.40, relheight=0.15, relwidth=0.500)
##        # Create a Button
##        btn = Button(Canvas5, text = 'Login', bd = '2',background="green",
##                        font="-family {Segoe UI} -size 12  ",foreground="white")
##        btn.place(x=350, rely=0.75, relheight=0.18, relwidth=0.08)
##
##        
##        global Canvas3
##        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
##        Canvas3.place(relx=0.850, rely=0.07, relheight=0.82, relwidth=0.150)


def ChangeCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Change Company',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.450)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0.42, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="center")
        btn.place(x=1310, rely=0, relheight=0.03, relwidth=0.03)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.375, rely=0.0300, relheight=0.100, relwidth=0.220)
        Label6 = Label(Frame2,text='Change Company',borderwidth="0", width=12, background="white",
                                             foreground="#00254a",
                                             font="-family {Segoe UI} -size 12 -weight bold ")
        Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.460)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.65, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame(Frame1, background="#e6ffff",borderwidth="1",relief="ridge")
        Frame3.place(relx=0.350, rely=0.130, relheight=0.900, relwidth=0.270)
        
        Label8 = Label(Frame3,text='List of Companies',borderwidth="0", width=8, background="#4B77BE",
                                             foreground="white",
                                             font="-family {Segoe UI} -size 12  ",anchor="w")
        Label8.place(x=0,y=0, relheight=0.04, relwidth=0.999)
        btn4=Button(Frame3,text='Create Company',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=Regular)
        btn4.place(relx=0, rely=0.10, relheight=0.03, width=363)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn1=Button(Frame3,text='Alter Company',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=SelectRemoteCompany)
        btn1.place(relx=0, rely=0.13, relheight=0.03, width=363)

        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Select Company',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e")
        btn2.place(relx=0, rely=0.16, relheight=0.03, width=363)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn3=Button(Frame3,text='Shut Comapny',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e")
        btn3.place(relx=0, rely=0.19, relheight=0.04, width=363)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        canvas = Canvas(Frame3,background="#e6ffff",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(5, 25, 358, 25,fill='black',width=0.01)
        canvas.place(relx=0, rely=0.23, relheight=0.04, relwidth=0.999)
        Label14 = Label(Frame3,text='Abc',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=10, y=185, height=30, width=190)
        Label14 = Label(Frame3,text='(10000)',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family Helvetica -size 10  ",anchor="e")
        Label14.place(x=196, y=185, height=30, width=160)
        
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        
##def call():
##    res = mb.askquestion('Exit Application', 
##                         'Do you really want to exit')
##      
##    if res == 'yes' :
##        Screen.destroy()
##          
##    else :
##        mb.showinfo('Return', 'Returning to main application')

def Regular():
    
        global Canvas1
        Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge",bd=0)
        Canvas1.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
        Label5 = Label(Canvas1,text='Company Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


        global Canvas2
        Canvas2 = tk.Canvas(Canvas1, background="white",borderwidth="0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas2.place(relx=0, rely=0.030, relheight=0.900, relwidth=0.880)
        Label11 = Label(Canvas2,text='Company Data Path',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label11.place(relx=0.02, rely=0.03, relheight=0.06, relwidth=0.160)
        Label12 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label12.place(relx=0.190, rely=0.03, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.05, relheight=0.04, relwidth=0.300)
        canvas = Canvas(Canvas2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.08, relheight=0.06, relwidth=0.980)
        Label13 = Label(Canvas2,text='Company Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label13.place(relx=0.01, rely=0.15, relheight=0.06, relwidth=0.150)
        Label14 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.190, rely=0.15, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.16, relheight=0.04, relwidth=0.300)
        Label15 = Label(Canvas2,text='Mailing Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label15.place(x=5, rely=0.23, relheight=0.06, relwidth=0.150)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.23, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.24, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Address',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=10, rely=0.28, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.28, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.29, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='State',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=5, rely=0.42, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.41, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.42, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Country',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=15, rely=0.46, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.45, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.46, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Pincode',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=15, rely=0.50, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.49, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.50, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Telephone',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=22, rely=0.54, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.53, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.54, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Mobile',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=12, rely=0.58, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.57, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.58, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Fax',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=12, rely=0.62, relheight=0.04, relwidth=0.080)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.61, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.62, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='E-mail',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=22, rely=0.66, relheight=0.04, relwidth=0.080)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.65, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.66, relheight=0.04, relwidth=0.300)
        Label17 = Label(Canvas2,text='Website',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=29, rely=0.70, relheight=0.04, relwidth=0.080)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.69, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.70, relheight=0.04, relwidth=0.300)
        canvas = Canvas(Canvas2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.74, relheight=0.06, relwidth=0.980)
        Label17 = Label(Canvas2,text='Base Currency symbol',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=40, rely=0.80, relheight=0.04, relwidth=0.150)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.79, relheight=0.06, relwidth=0.05)
        Label16 = Label(Canvas2,text='$',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=220, rely=0.80, relheight=0.04, relwidth=0.05)
        Label17 = Label(Canvas2,text='Formal name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=10, rely=0.84, relheight=0.04, relwidth=0.150)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.83, relheight=0.06, relwidth=0.05)
        Label16 = Label(Canvas2,text='INR',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=220, rely=0.84, relheight=0.04, relwidth=0.06)
        Label13 = Label(Canvas2,text='Financial year beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label13.place(x=600, rely=0.15, relheight=0.06, relwidth=0.210)
        Label14 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.720, rely=0.15, relheight=0.06, relwidth=0.02)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=850, rely=0.16, relheight=0.04, relwidth=0.200)
        Label13 = Label(Canvas2,text='Books beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label13.place(x=600, rely=0.20, relheight=0.06, relwidth=0.170)
        Label14 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.705, rely=0.20, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=850, rely=0.21, relheight=0.04, relwidth=0.200)
        # Create a Button
        btn = Button(Canvas2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=500, rely=0.90, relheight=0.06, relwidth=0.08)
        

       
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.850, rely=0.07, relheight=0.82, relwidth=0.150)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=5, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=5, height=30, width=20)
        Label14 = Label(Canvas3,text='F3:Company',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=40, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=100, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=135, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=170, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=205, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=240, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=275, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=275, height=30, width=20)
        Label14 = Label(Canvas3,text='F10:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=310, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=310, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'R: Group Company', bd = '0',background="white",
                        font="-family {Segoe UI} -size 12  ",foreground="black", command=GroupCompany)
        btn.place(x=5, y=380, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=380, height=30, width=20)






def GroupCompany():
    
        global Canvas1
        Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
        Canvas1.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
        Label5 = Label(Canvas1,text='Group Company Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


        global Canvas2
        Canvas2 = tk.Canvas(Canvas1, background="white",borderwidth="1", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas2.place(relx=0, rely=0.030, relheight=0.900, relwidth=0.600)
        Label11 = Label(Canvas2,text='Company Data Path',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label11.place(relx=0.02, rely=0.03, relheight=0.06, relwidth=0.200)
        Label12 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label12.place(relx=0.310, rely=0.03, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.05, relheight=0.04, relwidth=0.500)
        canvas = Canvas(Canvas2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.08, relheight=0.06, relwidth=0.980)
        Label13 = Label(Canvas2,text='Company Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label13.place(relx=0.03, rely=0.15, relheight=0.06, relwidth=0.150)
        Label14 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.310, rely=0.15, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.16, relheight=0.04, relwidth=0.500)
        Label15 = Label(Canvas2,text='Mailing Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label15.place(x=15, rely=0.23, relheight=0.06, relwidth=0.150)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.23, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.24, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Address',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=15, rely=0.28, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.28, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.29, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='State',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=8, rely=0.42, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.41, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.42, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Country',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=15, rely=0.46, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.45, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.46, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Pincode',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=15, rely=0.50, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.49, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.50, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Telephone',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=22, rely=0.54, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.53, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.54, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Mobile',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=12, rely=0.58, relheight=0.04, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.57, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.58, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Fax',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=8, rely=0.62, relheight=0.04, relwidth=0.080)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.61, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.62, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='E-mail',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=18, rely=0.66, relheight=0.04, relwidth=0.080)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.65, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.66, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Website',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=25, rely=0.70, relheight=0.04, relwidth=0.080)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.69, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.70, relheight=0.04, relwidth=0.500)
        Label17 = Label(Canvas2,text='Members companies',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=20, rely=0.80, relheight=0.04, relwidth=0.200)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.79, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.80, relheight=0.04, relwidth=0.500)
        # Create a Button
        btn = Button(Canvas2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=Regular)
        btn.place(x=300, rely=0.90, relheight=0.06, relwidth=0.08)
        

       
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.850, rely=0.07, relheight=0.82, relwidth=0.150)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=5, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=5, height=30, width=20)
        Label14 = Label(Canvas3,text='F3:Company',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=40, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=100, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=135, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=170, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=205, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=240, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=275, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=275, height=30, width=20)
        Label14 = Label(Canvas3,text='F10:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=5, y=310, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=310, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'R: Regular', bd = '0',background="white",
                        font="-family {Segoe UI} -size 12  ",foreground="black",command=GroupCompany)
        btn.place(x=5, y=380, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=380, height=30, width=20)



def SelectRemoteCompany():
    
        global Canvas1
        Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
        Canvas1.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
        Label5 = Label(Canvas1,text='Tally.NET User Login',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


        global Canvas2
        Canvas2 = tk.Canvas(Canvas1, background="white",borderwidth="1", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas2.place(x=270, rely=0.300, relheight=0.300, relwidth=0.600)
        Label11 = Label(Canvas2,text='Login as Tally.NET User',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  -weight bold ")
        Label11.place(x=300, rely=0.03, relheight=0.15, relwidth=0.250)
        Label17 = Label(Canvas2,text='Tally.Net ID',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=25, rely=0.23, relheight=0.15, relwidth=0.100)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=250, rely=0.22, relheight=0.15, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=10,borderwidth="3")
        Entry2.place(x=280, rely=0.23, relheight=0.15, relwidth=0.600)
        Label17 = Label(Canvas2,text='Tally.NET password',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=15, rely=0.48, relheight=0.15, relwidth=0.200)
        Label16 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=250, rely=0.46, relheight=0.15, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.48, relheight=0.15, relwidth=0.600)
        # Create a Button
        btn = Button(Canvas2, text = 'Login', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=350, rely=0.75, relheight=0.18, relwidth=0.08)
        

       
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.850, rely=0.07, relheight=0.82, relwidth=0.150)
        
        # Create a Button
        btn = Button(Canvas3, text = 'R: Reset Password', bd = '0',background="white",
                        font="-family {Segoe UI} -size 12  ",foreground="black",command=ResetPassword)
        btn.place(x=5, y=380, height=30, width=163)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=170, y=380, height=30, width=20)



def ResetPassword():
    
        global Canvas4
        Canvas4 = tk.Canvas( background="#B0B0B0", relief="ridge")
        Canvas4.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
        Label5 = Label(Canvas4,text='Reset Password',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


        global Canvas5
        Canvas5 = tk.Canvas(Canvas4, background="white",borderwidth="1", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas5.place(x=270, rely=0.300, relheight=0.300, relwidth=0.600)
        Label11 = Label(Canvas5,text='Reset Password',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  -weight bold ")
        Label11.place(x=300, rely=0.03, relheight=0.15, relwidth=0.250)
        Label17 = Label(Canvas5,text='Tally.Net ID',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label17.place(x=25, rely=0.23, relheight=0.15, relwidth=0.100)
        Label16 = Label(Canvas5,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=250, rely=0.22, relheight=0.15, relwidth=0.05)
        Entry2 = Entry(Canvas5,width=10,borderwidth="3")
        Entry2.place(x=280, rely=0.23, relheight=0.15, relwidth=0.600)
        Label17 = Label(Canvas5,text='You will receive an e-mail with a link to reset password',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Helvetica} -size 12 -slant italic ")
        Label17.place(x=320, rely=0.40, relheight=0.15, relwidth=0.500)
        # Create a Button
        btn = Button(Canvas5, text = 'Login', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=350, rely=0.75, relheight=0.18, relwidth=0.08)

        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.850, rely=0.07, relheight=0.82, relwidth=0.150)
        

       
       



global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#848884")
screen.configure(cursor="arrow")
          
##sbmibtn=Button(screen,text='K:Company',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=Gatewayoftally).place(x=20,y=10)
##sbmibtn=Button(screen,text='Y:Data',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=180,y=10)
##sbmibtn=Button(screen,text='Z:Exchange',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=340,y=10)
##sbmibtn=Button(screen,text='G:Go To',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=600,y=10)
##sbmibtn=Button(screen,text='O:Import',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=850,y=10)
##sbmibtn=Button(screen,text='E:Export',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=990,y=10)
##sbmibtn=Button(screen,text='M:E-mail',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)
##sbmibtn=Button(screen,text='P:Print',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1270,y=10)
##sbmibtn=Button(screen,text='F1:Help',borderwidth="0",background="#023047",
##                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1400,y=10)

# NavBar Start
name = Label(screen, text="TallyPrime", fg='pink',bg='#3a646b',font=("Arial", 13),anchor='w').place(x = 1,y = 0,width=1666,height=60)
name = Label(screen, text="MANAGE" ,fg='#00c8ff',bg='#3a646b',font=('Arial 9 underline'),anchor='w').place(x = 110,y = 9,width=206,height=10)

b1 = Button(screen,text = "K:Company",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10'),command=Gatewayoftally).place (x=120,y=33)
b2 = Button(screen,text = "Y:Data",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=275,y=33)
b3 = Button(screen,text = "Z:Exchange",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=395,y=33)
b4 = Button(screen,text = "  G:Go To  ",activeforeground = "black", activebackground = "white",fg='black',bg='white',borderwidth=0,underline=2,font=('Arial 10 bold'),).place (x=565,y=33)
b5 = Button(screen,text = "O:Import",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=825,y=33)
b6 = Button(screen,text = "E:Export",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=950,y=33)
b7 = Button(screen,text = "M:E-mail",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1080,y=33)
b8 = Button(screen,text = "P:Print",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1200,y=33)
b9 = Button(screen,text = "F1:Help",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1350,y=33)

# NavBar End

global Canvas1
Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.820, relwidth=0.900)
Label5 = Label(Canvas1,text='Select Company',borderwidth="0", width=5, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(x=0, y=0, relheight=0.03, relwidth=0.999)


global Canvas4
Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas4.place(relx=0.330, rely=0.0300, relheight=0.100, relwidth=0.350)
Label6 = Label(Canvas4,text='Select Company',borderwidth="0", width=12, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 12 -weight bold ")
Label6.place(relx=0.35, rely=0.20, relheight=0.30, relwidth=0.300)
Entry1 = Entry(Canvas4,width=60,borderwidth="3")
Entry1.place(relx=0.01, rely=0.65, relheight=0.30, relwidth=0.980)

global Canvas2
Canvas2 = tk.Canvas(Canvas1, background="#e6ffff",borderwidth="1", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas2.place(relx=0.200, rely=0.131, relheight=0.900, relwidth=0.600)
Label7 = Label(Canvas2,text='List of Companies',borderwidth="0", width=8, background="#3252a8",
                                     foreground="white",
                                     font="-family {Segoe UI} -size 12")
Label7.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)
Label8 = Label(Canvas2,text='Data Path/Name',borderwidth="0", width=8, background="#eff6f6",
                                     foreground="black",
                                     font="-family {Segoe UI} -size 12  ")
Label8.place(relx=0, rely=0.03, relheight=0.04, relwidth=0.220)
Label9 = Label(Canvas2,text='Number',borderwidth="0", width=8, background="#eff6f6",
                                     foreground="black",
                                     font="-family {Segoe UI} -size 12  ")
Label9.place(relx=0.20, rely=0.03, relheight=0.04, relwidth=0.700)
Label10 = Label(Canvas2,text='Period',borderwidth="0", width=8, background="#eff6f6",
                                     foreground="black",
                                     font="-family {Segoe UI} -size 12  ")
Label10.place(relx=0.89, rely=0.03, relheight=0.04, relwidth=0.120)
btn=Button(Canvas2,text='Create Company',borderwidth="0",background="#e6ffff",
                                     foreground="black",width=78,font="-family {Segoe UI} -size 12 ",command=Regular)
btn.place(relx=0, rely=0.10, relheight=0.04, width=780)
def on_enter(e):
    btn['background'] = 'yellow'
def on_leave(e):
    btn['background'] = '#e6ffff'
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)
btn1=Button(Canvas2,text='Select Remote Company',borderwidth="0",background="#e6ffff",
                                     foreground="black",width=78,font="-family {Segoe UI} -size 12 ",command=SelectRemoteCompany)
btn1.place(relx=0, rely=0.15, relheight=0.04, width=780)

def on_enter(e):
    btn1['background'] = 'yellow'
def on_leave(e):
    btn1['background'] = '#e6ffff'
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)
btn2=Button(Canvas2,text='Specify Path',borderwidth="0",background="#e6ffff",
                                     foreground="black",width=78,font="-family {Segoe UI} -size 12 ")
btn2.place(relx=0, rely=0.20, relheight=0.04, width=780)

def on_enter(e):
    btn2['background'] = 'yellow'
def on_leave(e):
    btn2['background'] = '#e6ffff'
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)
btn3=Button(Canvas2,text='Selec from Drive',borderwidth="0",background="#e6ffff",
                                     foreground="black",width=78,font="-family {Segoe UI} -size 12 ")
btn3.place(relx=0, rely=0.25, relheight=0.04, width=780)

def on_enter(e):
    btn3['background'] = 'yellow'
def on_leave(e):
    btn3['background'] = '#e6ffff'
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)


global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff",borderwidth="0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.880, rely=0.07, relheight=0.95, relwidth=0.130)
screen.mainloop()
