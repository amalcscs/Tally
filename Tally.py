from tkinter.messagebox import showinfo
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
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
        # Separator object
        separator = ttk.Separator(Canvas1, orient='horizontal')
        separator.place(x=0, y=140, relwidth=0.530, relheight=0)
        Label5 = Label(Canvas1,text='NAME OF COMPANY',borderwidth="0", width=5, background="white",
                                            foreground="#4B77BE",font="-family {Segoe UI} -size 10 ")
        Label5.place(x=0, y=142, relheight=0.03, relwidth=0.150)
        Label5 = Label(Canvas1,text='DATE OF LAST ENTRY',borderwidth="0", width=5, background="white",
                                            foreground="#4B77BE",font="-family {Segoe UI} -size 10 ")
        Label5.place(x=460, y=142, relheight=0.03, relwidth=0.150)
        # Separator object
        separator = ttk.Separator(Canvas1, orient='horizontal')
        separator.place(x=0, y=162, relwidth=0.530, relheight=0)

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
                                     foreground="black",font=" -size 10 ",command=MasterCreation)
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
                        font="-family {Segoe UI} -size 12  ",foreground="black",command=ChangeDate,anchor="w")
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
        

def ChangeDate():
   
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Change Current Date',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.450)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0.42, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="black",anchor="center")
        btn.place(x=1160, rely=0, relheight=0.03, relwidth=0.03)
        global Frame2
        Frame2 = tk.Frame(Frame1, background="white", relief="ridge",bd=0)
        Frame2.place(x=480, y=300, relheight=0.200, relwidth=0.200)
        Label5 = Label(Frame2,text='Current Date',borderwidth="0", width=5, background="white",
                                            foreground="#00254a",font="-family {Segoe UI} -size 12 -weight bold ",anchor="w")
        Label5.place(x=65, y=10, relheight=0.15, relwidth=0.450)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(x=70, y=50, relheight=0.15, relwidth=0.350)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="white",anchor="center")
        btn.place(x=70, y=90, relheight=0.20, relwidth=0.350)

        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def ChangeCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Change Company',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.375, rely=0.0300, relheight=0.100, relwidth=0.220)
        Label6 = Label(Frame2,text='Change Company',borderwidth="0", width=12, background="white",
                                             foreground="#00254a",
                                             font="-family {Segoe UI} -size 12 -weight bold ")
        Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.510)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.65, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame(Frame1, background="#e6ffff",borderwidth="1",relief="ridge")
        Frame3.place(relx=0.330, rely=0.130, relheight=0.900, relwidth=0.310)
        
        Label8 = Label(Frame3,text='List of Companies',borderwidth="0", width=8, background="#4B77BE",
                                             foreground="white",
                                             font="-family {Segoe UI} -size 12  ",anchor="w")
        Label8.place(relx=0,rely=0, relheight=0.04, relwidth=0.999)
        btn4=Button(Frame3,text='Create Company   ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=Regular)
        btn4.place(relx=0, rely=0.10, relheight=0.03, width=370)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn1=Button(Frame3,text='Alter Company   ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=AlterCompany)
        btn1.place(relx=0, rely=0.13, relheight=0.03, width=370)

        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Select Company   ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=SelectCompany)
        btn2.place(relx=0, rely=0.16, relheight=0.03, width=370)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn3=Button(Frame3,text='Shut Company   ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=ShutCompany)
        btn3.place(relx=0, rely=0.19, relheight=0.04, width=370)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0, rely=0.23, relwidth=0.995, height=0)
        Label14 = Label(Frame3,text='Abc',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=10, y=140, height=27, width=190)
        Label14 = Label(Frame3,text='(10000)',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family Helvetica -size 10  ",anchor="e")
        Label14.place(x=230, y=140, height=30, width=110)
        
        
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
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Company Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0,relief="ridge")
        Frame2.place(relx=0, rely=0.030, relheight=0.800, relwidth=0.880)
        Label11 = Label(Frame2,text='Company Data Path',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label11.place(x=10, rely=0.03, relheight=0.06, relwidth=0.130)
        Label12 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label12.place(relx=0.190, rely=0.03, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.05, relheight=0.04, relwidth=0.300)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.08, relheight=0.06, relwidth=0.980)
        Label13 = Label(Frame2,text='Company Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=15, rely=0.15, relheight=0.06, relwidth=0.100)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.190, rely=0.15, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.16, relheight=0.04, relwidth=0.300)
        Label15 = Label(Frame2,text='Mailing Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label15.place(x=10, rely=0.23, relheight=0.06, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.23, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.24, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Address',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=5, rely=0.28, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.28, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.29, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='State',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=5, rely=0.42, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.41, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.42, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Country',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=13, rely=0.46, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.45, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.46, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Pincode',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=15, rely=0.50, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.49, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.50, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Telephone',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=20, rely=0.54, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.53, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.54, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Mobile',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=13, rely=0.58, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.57, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.58, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Fax',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=3, rely=0.62, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.61, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.62, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='E-mail',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=12, rely=0.66, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.65, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.66, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Website',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=7, rely=0.70, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.69, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.70, relheight=0.04, relwidth=0.300)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.74, relheight=0.06, relwidth=0.980)
        Label17 = Label(Frame2,text='Base Currency symbol',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.80, relheight=0.04, relwidth=0.150)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.79, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.80, relheight=0.04, relwidth=0.06)
        Label17 = Label(Frame2,text='Formal name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.84, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.83, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.84, relheight=0.04, relwidth=0.06)

        Label13 = Label(Frame2,text='Financial year beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=590, rely=0.15, relheight=0.06, relwidth=0.210)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.760, rely=0.15, relheight=0.06, relwidth=0.02)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(x=820, rely=0.16, relheight=0.04, relwidth=0.100)
        Label13 = Label(Frame2,text='Books beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=590, rely=0.20, relheight=0.06, relwidth=0.170)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.745, rely=0.20, relheight=0.06, relwidth=0.05)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(x=820, rely=0.21, relheight=0.04, relwidth=0.100)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn.place(x=500, rely=0.90, relheight=0.06, relwidth=0.08)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=5, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=5, height=30, width=20)
        Label14 = Label(Canvas3,text='F3:Company',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=40, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=100, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=135, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=170, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=205, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=240, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=275, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=275, height=30, width=20)
        Label14 = Label(Canvas3,text='F10:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=310, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=310, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'R: Group Company', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=GroupCompany)
        btn.place(x=5, y=380, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=380, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'F12: Configure', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=Configure)
        btn.place(x=5, y=580, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=580, height=30, width=20)


def Configure():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Configuration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0,relief="ridge")
        Frame2.place(relx=0.280, rely=0.330, relheight=0.350, relwidth=0.450)
        Label5 = Label(Frame2,text='Configuration',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.05, rely=0.10, relheight=0.10, relwidth=0.200)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.05, rely=0.23, relwidth=0.900, height=0)
        Label5 = Label(Frame2,text='Provide Contact Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.30, relheight=0.07, relwidth=0.300)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.30, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.29, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Set Edit Log applicability',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.39, relheight=0.07, relwidth=0.300)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.39, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.38, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Use TallyVault Password to encrypt Company Data',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.48, relheight=0.07, relwidth=0.600)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.48, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.47, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Use User Access Control',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.57, relheight=0.07, relwidth=0.600)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.57, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.56, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Provide Additional Base Currency details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.66, relheight=0.07, relwidth=0.600)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.66, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.65, relheight=0.08, relwidth=0.200)
        
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn.place(x=220, rely=0.80, relheight=0.10, relwidth=0.15)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        


def CompanyFeaturesAlteration():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Company Features Alteration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.450)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0.42, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="center")
        btn.place(x=1160, rely=0, relheight=0.03, relwidth=0.03)

        global Frame2
        Frame2 = tk.Canvas(Frame1, background="white",bd=0, insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Frame2.place(relx=0.100, rely=0.200, relheight=0.600, relwidth=0.800)
        Label11 = Label(Frame2,text='Company created successfully.',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold  ")
        Label11.place(relx=0.380, rely=0.03, relheight=0.06, relwidth=0.250)
        Label11 = Label(Frame2,text='(Enable the features as per your business needs.)',borderwidth="0", width=8, background="white",
                                            foreground="black")
        Label11.configure(font=("Segoe", 10, "italic"))
        Label11.place(relx=0.355, rely=0.10, relheight=0.04, relwidth=0.300)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=1)
        canvas.place(relx=0, rely=0.14, relheight=0.10, relwidth=0.980)
        Label17 = Label(Frame2,text='Company',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold  ")
        Label17.place(x=10, rely=0.22, relheight=0.05, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.090, rely=0.22, relheight=0.04, relwidth=0.05)
        Label16 = Label(Frame2,text='Abc',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  -weight bold")
        Label16.place(relx=0.130, rely=0.22, relheight=0.04, relwidth=0.05)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=1)
        canvas.place(relx=0, rely=0.27, relheight=0.10, relwidth=0.980)
        Label17 = Label(Frame2,text='Show more features',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=20, rely=0.36, relheight=0.04, relwidth=0.150)
        Label17.configure(font=("Segoe", 10, "italic"))
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.170, rely=0.35, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=200, rely=0.35, relheight=0.05, relwidth=0.100)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=1)
        canvas.place(relx=0, rely=0.41,relheight=0.10, relwidth=0.980)
        Label17 = Label(Frame2,text='Accounting',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold")
        Label17.place(x=20, rely=0.49, relheight=0.05, relwidth=0.100)
        Label17 = Label(Frame2,text='Maintain Accounts',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=23, rely=0.55, relheight=0.04, relwidth=0.130)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.350, rely=0.55, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=370, rely=0.55, relheight=0.05, relwidth=0.100)
        Label17 = Label(Frame2,text='Enable Bill-wise entry',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=40, rely=0.62, relheight=0.05, relwidth=0.130)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.350, rely=0.62, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=370, rely=0.62, relheight=0.05, relwidth=0.100)
        Label17 = Label(Frame2,text='Inventory',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold")
        Label17.place(x=15, rely=0.72, relheight=0.06, relwidth=0.100)
        Label17 = Label(Frame2,text='Maintain Inventory',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=25, rely=0.80, relheight=0.04, relwidth=0.130)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.350, rely=0.80, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=370, rely=0.80, relheight=0.05, relwidth=0.100)
        Label17 = Label(Frame2,text='Integrate Accounts with Inventory',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=45, rely=0.88, relheight=0.05, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.350, rely=0.88, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=370, rely=0.88, relheight=0.05, relwidth=0.100)
        # Separator object
        separator = ttk.Separator(Frame2, orient='vertical')
        separator.place(relx=0.500, y=190, relwidth=0, height=200)
        Label17 = Label(Frame2,text='Taxation',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold")
        Label17.place(x=500, rely=0.49, relheight=0.04, relwidth=0.06)
        Label17 = Label(Frame2,text='Enable Goods and Services Tax (GST)',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=500, rely=0.55, relheight=0.04, relwidth=0.24)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.790, rely=0.55, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=800, rely=0.55, relheight=0.05, relwidth=0.100)
        Label17 = Label(Frame2,text='Enable Tax Deducted at Source (TDS)',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=500, rely=0.62, relheight=0.04, relwidth=0.24)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.790, rely=0.62, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=800, rely=0.62, relheight=0.05, relwidth=0.100)
        
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=5, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=5, height=30, width=20)
        Label14 = Label(Canvas3,text='F3:Company',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=40, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=100, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=135, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=170, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=205, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=240, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=275, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=275, height=30, width=20)
        Label14 = Label(Canvas3,text='F10:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=310, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=310, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'I: More Details', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=MoreDetails)
        btn.place(x=5, y=380, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=380, height=30, width=20)

def MoreDetails():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Company Features Alteration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Canvas(Frame1, background="white",bd=0, insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Frame2.place(relx=0.320, rely=0.03, relheight=0.100, relwidth=0.350)
        Label11 = Label(Frame2,text='More Details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold  ")
        Label11.place(relx=0.27, rely=0.06, relheight=0.25, relwidth=0.50)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(relx=0.03, rely=0.45, relheight=0.28, relwidth=0.940)

        global Frame3
        Frame3 = tk.Canvas(Frame1, background="#e6ffff",bd=0, insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Frame3.place(relx=0.270, rely=0.11, relheight=0.200, relwidth=0.450)
        Label11 = Label(Frame3,text='  List of Company Details',borderwidth="0", width=8, background="#2a52be",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 11",anchor="w")
        Label11.place(relx=0, rely=0, relheight=0.12, relwidth=1.000)
        # Create a Button
        btn = Button(Frame3, text = 'Show More  ', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10",foreground="black",anchor="e",command=ShowMore)
        btn.place(relx=0, rely=0.23, relheight=0.12, relwidth=1.000)
        def on_enter(e):
            btn['background'] = 'yellow'
        def on_leave(e):
            btn['background'] = '#e6ffff'
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.36, relheight=0, relwidth=0.980)
        Label11 = Label(Frame3,text='  Statutory Details',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label11.place(relx=0, rely=0.40, relheight=0.12, relwidth=1.000)
        # Create a Button
        btn1 = Button(Frame3, text = '      GST Details', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10",foreground="black",anchor="w",command=GSTdetails)
        btn1.place(relx=0, rely=0.55, relheight=0.12, relwidth=1.000)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        Label11 = Label(Frame3,text='  General Details',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label11.place(relx=0, rely=0.70, relheight=0.10, relwidth=1.000)
        # Create a Button
        btn2 = Button(Frame3, text = '      PAN/CIN Details', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w",command=PANdetails)
        btn2.place(relx=0, rely=0.85, relheight=0.10, relwidth=1.000)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        

def ShowMore():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Company Features Alteration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Canvas(Frame1, background="white",bd=0, insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Frame2.place(relx=0.320, rely=0.03, relheight=0.100, relwidth=0.350)
        Label11 = Label(Frame2,text='More Details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold  ")
        Label11.place(relx=0.27, rely=0.06, relheight=0.25, relwidth=0.50)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(relx=0.03, rely=0.45, relheight=0.28, relwidth=0.940)

        global Frame3
        Frame3 = tk.Canvas(Frame1, background="#e6ffff",bd=0, insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Frame3.place(relx=0.270, rely=0.11, relheight=0.300, relwidth=0.450)
        Label11 = Label(Frame3,text='  List of Company Details',borderwidth="0", width=8, background="#2a52be",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 11",anchor="w")
        Label11.place(relx=0, rely=0, relheight=0.12, relwidth=1.000)
        # Create a Button
        btn = Button(Frame3, text = 'Show Less  ', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10",foreground="black",anchor="e",command=MoreDetails)
        btn.place(relx=0, rely=0.23, relheight=0.10, relwidth=1.000)
        def on_enter(e):
            btn['background'] = 'yellow'
        def on_leave(e):
            btn['background'] = '#e6ffff'
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        # Create a Button
        btn4 = Button(Frame3, text = 'Show Inactive  ', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10",foreground="black",anchor="e")
        btn4.place(relx=0, rely=0.31, relheight=0.10, relwidth=1.000)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.40, relheight=0, relwidth=0.980)
        Label11 = Label(Frame3,text='  Statutory Details',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label11.place(relx=0, rely=0.42, relheight=0.12, relwidth=1.000)
        # Create a Button
        btn1 = Button(Frame3, text = '      GST Details', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10",foreground="black",anchor="w",command=GSTdetails)
        btn1.place(relx=0, rely=0.53, relheight=0.10, relwidth=1.000)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        Label11 = Label(Frame3,text='  General Details',borderwidth="0", width=8, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label11.place(relx=0, rely=0.65, relheight=0.10, relwidth=1.000)
        # Create a Button
        btn5 = Button(Frame3, text = '      PAN/CIN Details', bd = '2',background="#e6ffff",borderwidth="0",
                       font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w",command=PANdetails)
        btn5.place(relx=0, rely=0.75, relheight=0.10, relwidth=1.000)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def GSTdetails():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Company GSTDetails moreDetails',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0, relief="ridge")
        Frame2.place(relx=0.10, rely=0.10, relheight=0.750, relwidth=0.800)
        Label11 = Label(Frame2,text='GST Details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11 -weight bold  ")
        Label11.place(relx=0.25, rely=0, relheight=0.12, relwidth=0.50)
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.45, y=38, relheight=0, relwidth=0.10)
        Label11 = Label(Frame2,text='GST Registration Details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11 -weight bold  ")
        Label11.place(relx=0, rely=0.10, relheight=0.10, relwidth=0.250)
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.03, y=85, relheight=0, relwidth=0.19)
        Label11 = Label(Frame2,text='State',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.19, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.18, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Kerala", "Delhi"])
        combo.place(relx=0.345, rely=0.19, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Registration type',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.24, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.23, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Composition", "Regular"])
        combo.place(relx=0.345, rely=0.24, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Assessee of Other Territory',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.29, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.28, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.345, rely=0.29, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='GST Application form',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.34, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.33, relheight=0.06, relwidth=0.03)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(relx=0.345, rely=0.34, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='GSTIN/UIN',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.39, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.38, relheight=0.06, relwidth=0.03)
        entry1 = Entry(Frame2,width=60,borderwidth="1")
        entry1.place(relx=0.345, rely=0.39, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Periodicity of GSTR1',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.44, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.43, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Monthly", "Quarterly"])
        combo.place(relx=0.345, rely=0.44, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Additional Features',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11 -weight bold",anchor="w")
        Label11.place(relx=0.03, rely=0.50, relheight=0.04, relwidth=0.200)
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.03, rely=0.54, relheight=0, relwidth=0.19)
        Label11 = Label(Frame2,text='Set/alter GST rate details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.56, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.55, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.345, rely=0.56, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Enable tax liability on advance receipts',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.61, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.60, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.345, rely=0.61, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Enable tax liability on reverse charge',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.66, relheight=0.04, relwidth=0.300)
        Label11 = Label(Frame2,text='(Enable tax liability on reverse charge)',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Helvetica} -size 11 -slant italic ",anchor="w")
        Label11.place(relx=0.03, rely=0.70, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.65, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.345, rely=0.66, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Enable GST Classifications',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.76, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.75, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.345, rely=0.76, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Provide LUT/BOND details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.03, rely=0.81, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.320, rely=0.80, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.345, rely=0.81, relheight=0.04, relwidth=0.100)

        Label11 = Label(Frame2,text='Invoice Features',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11 -weight bold  ")
        Label11.place(relx=0.520, rely=0.10, relheight=0.10, relwidth=0.250)
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.580, y=85, relheight=0, relwidth=0.13)
        Label11 = Label(Frame2,text='e-Way Bill applicable',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.580, rely=0.19, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.850, rely=0.18, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.870, rely=0.19, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='e-Invoicing applicable',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.580, rely=0.24, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.850, rely=0.23, relheight=0.06, relwidth=0.03)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.870, rely=0.24, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Applicable from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.600, rely=0.29, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.850, rely=0.28, relheight=0.06, relwidth=0.03)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(relx=0.870, rely=0.29, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Bill from place',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.600, rely=0.34, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.850, rely=0.33, relheight=0.06, relwidth=0.03)
        entry1 = Entry(Frame2,width=60,borderwidth="1")
        entry1.place(relx=0.870, rely=0.34, relheight=0.04, relwidth=0.100)
        Label11 = Label(Frame2,text='Default period for the e-Invoice report',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.600, rely=0.39, relheight=0.04, relwidth=0.300)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.850, rely=0.38, relheight=0.06, relwidth=0.03)
        entry1 = Entry(Frame2,width=20,borderwidth="1")
        entry1.place(relx=0.870, rely=0.39, relheight=0.04, relwidth=0.04)
        Label11 = Label(Frame2,text='Days',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label11.place(relx=0.900, rely=0.39, relheight=0.04, relwidth=0.100)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=Regular)
        btn.place(x=430, rely=0.91, relheight=0.06, relwidth=0.08)

        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        Label14 = Label(Canvas3,text='  W:Details',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12", anchor="w")
        Label14.place(x=5, y=300, height=30, width=110)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=120, y=300, height=30, width=20)



def PANdetails():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Company Features Alteration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0, relief="ridge")
        Frame2.place(relx=0.270, rely=0.350, relheight=0.250, relwidth=0.450)
        Label5 = Label(Frame2,text='PAN/CIN Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 11 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0.10, relheight=0.10, relwidth=0.600)
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.40, rely=0.20, relheight=0, relwidth=0.20)
        Label5 = Label(Frame2,text='PAN/Income tax no.',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label5.place(relx=0.04, rely=0.30, relheight=0.10, relwidth=0.250)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.500, rely=0.30, relheight=0.10, relwidth=0.03)
        entry1 = Entry(Frame2,width=20,borderwidth="1")
        entry1.place(relx=0.550, rely=0.30, relheight=0.10, relwidth=0.40)
        Label5 = Label(Frame2,text='Corporate Identity No. (CIN)',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 11",anchor="w")
        Label5.place(relx=0.04, rely=0.45, relheight=0.10, relwidth=0.400)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.500, rely=0.45, relheight=0.10, relwidth=0.03)
        entry1 = Entry(Frame2,width=20,borderwidth="1")
        entry1.place(relx=0.550, rely=0.45, relheight=0.10, relwidth=0.40)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=Regular)
        btn.place(x=250, rely=0.70, relheight=0.15, relwidth=0.08)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        

def GroupCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Group Company Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",borderwidth="0",relief="ridge")
        Frame2.place(relx=0, rely=0.030, relheight=0.900, relwidth=0.600)
        Label11 = Label(Frame2,text='Company Data Path',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label11.place(relx=0.02, rely=0.03, relheight=0.06, relwidth=0.200)
        Label12 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label12.place(relx=0.310, rely=0.03, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.05, relheight=0.04, relwidth=0.500)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.08, relheight=0.06, relwidth=0.980)
        Label13 = Label(Frame2,text='Company Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(relx=0.03, rely=0.15, relheight=0.06, relwidth=0.150)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.310, rely=0.15, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.16, relheight=0.04, relwidth=0.500)
        Label15 = Label(Frame2,text='Mailing Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label15.place(x=15, rely=0.23, relheight=0.06, relwidth=0.150)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.23, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.24, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Address',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=15, rely=0.28, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.28, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.29, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='State',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=8, rely=0.42, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.41, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.42, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Country',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=15, rely=0.46, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.45, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.46, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Pincode',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=15, rely=0.50, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.49, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.50, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Telephone',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=22, rely=0.54, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.53, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.54, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Mobile',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=12, rely=0.58, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.57, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.58, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Fax',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=8, rely=0.62, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.61, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.62, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='E-mail',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=18, rely=0.66, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.65, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.66, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Website',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=25, rely=0.70, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.69, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.70, relheight=0.04, relwidth=0.500)
        Label17 = Label(Frame2,text='Members companies',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=20, rely=0.80, relheight=0.04, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.310, rely=0.79, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.80, relheight=0.04, relwidth=0.500)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=Regular)
        btn.place(x=300, rely=0.90, relheight=0.06, relwidth=0.08)
        

       
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ",anchor="w")
        Label14.place(x=5, y=5, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=5, height=30, width=20)
        Label14 = Label(Canvas3,text='F3:Company',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label14.place(x=5, y=40, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label14.place(x=5, y=100, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label14.place(x=5, y=135, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label14.place(x=5, y=170, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label14.place(x=5, y=205, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label14.place(x=5, y=240, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label14.place(x=5, y=275, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=275, height=30, width=20)
        Label14 = Label(Canvas3,text='F10:',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label14.place(x=5, y=310, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=310, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'R: Regular', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10 ",foreground="black",anchor="w",command=Regular)
        btn.place(x=5, y=380, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=380, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'F12: Configure', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10 ",foreground="black",anchor="w",command=GroupConfiguration)
        btn.place(x=5, y=550, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=550, height=30, width=20)



def GroupConfiguration():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Configuration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",borderwidth="0",relief="ridge")
        Frame2.place(relx=0.300, rely=0.400, relheight=0.200, relwidth=0.400)
        Label5 = Label(Frame2,text='Configuration',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 12 -weight bold ",anchor="w")
        Label5.place(relx=0.05, rely=0.15, relheight=0.15, relwidth=0.600)
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.05, rely=0.30, relheight=0, relwidth=0.900)
        Label5 = Label(Frame2,text='Provide Contact Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.40, relheight=0.15, relwidth=0.600)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.650, rely=0.40, relheight=0.10, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.700, rely=0.40, relheight=0.12, relwidth=0.200)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=Regular)
        btn.place(x=200, rely=0.75, relheight=0.15, relwidth=0.15)
       
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)

def AlterCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Company Alteration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0,relief="ridge")
        Frame2.place(relx=0, rely=0.030, relheight=0.800, relwidth=0.880)
        Label13 = Label(Frame2,text='Company Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=15, rely=0.05, relheight=0.06, relwidth=0.100)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.190, rely=0.05, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.07, relheight=0.04, relwidth=0.300)
        Label15 = Label(Frame2,text='Mailing Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label15.place(x=10, rely=0.10, relheight=0.06, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.10, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.12, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Address',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=5, rely=0.15, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.15, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.17, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='State',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=5, rely=0.42, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.41, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.42, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Country',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=13, rely=0.46, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.45, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.46, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Pincode',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=15, rely=0.50, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.49, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.50, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Telephone',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=20, rely=0.54, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.53, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.54, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Mobile',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=13, rely=0.58, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.57, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.58, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Fax',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=3, rely=0.62, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.61, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.62, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='E-mail',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=12, rely=0.66, relheight=0.04, relwidth=0.060)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.65, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.66, relheight=0.04, relwidth=0.300)
        Label17 = Label(Frame2,text='Website',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ")
        Label17.place(x=7, rely=0.70, relheight=0.04, relwidth=0.080)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.69, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.70, relheight=0.04, relwidth=0.300)
        canvas = Canvas(Frame2,background="white",bd=0, highlightthickness=0, relief='ridge')
        canvas.create_line(15, 25, 1800, 25,fill='#D3D3D3',width=2)
        canvas.place(relx=0, rely=0.74, relheight=0.06, relwidth=0.980)
        Label17 = Label(Frame2,text='Base Currency symbol',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.80, relheight=0.04, relwidth=0.150)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.79, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.80, relheight=0.04, relwidth=0.06)
        Label17 = Label(Frame2,text='Formal name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.84, relheight=0.04, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.190, rely=0.83, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=230, rely=0.84, relheight=0.04, relwidth=0.06)

        Label13 = Label(Frame2,text='Financial year beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=590, rely=0.05, relheight=0.06, relwidth=0.210)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.760, rely=0.05, relheight=0.06, relwidth=0.02)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(x=820, rely=0.06, relheight=0.04, relwidth=0.100)
        Label13 = Label(Frame2,text='Books beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=590, rely=0.10, relheight=0.06, relwidth=0.170)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.745, rely=0.10, relheight=0.06, relwidth=0.05)
        cal = DateEntry(Frame2, width= 16, background= "magenta3", foreground= "white",bd=2)
        cal.place(x=820, rely=0.11, relheight=0.04, relwidth=0.100)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn.place(x=500, rely=0.90, relheight=0.06, relwidth=0.08)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=5, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=5, height=30, width=20)
        Label14 = Label(Canvas3,text='F3:Company',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=40, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=100, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=135, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=170, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=205, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=240, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=275, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=275, height=30, width=20)
        Label14 = Label(Canvas3,text='F10:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=310, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=310, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'F12: Configure', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=Configure)
        btn.place(x=5, y=580, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=580, height=30, width=20)


def AlterConfigure():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Configuration',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0,relief="ridge")
        Frame2.place(relx=0.280, rely=0.330, relheight=0.350, relwidth=0.450)
        Label5 = Label(Frame2,text='Configuration',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.05, rely=0.10, relheight=0.10, relwidth=0.200)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.05, rely=0.23, relwidth=0.900, height=0)
        Label5 = Label(Frame2,text='Provide Contact Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.30, relheight=0.07, relwidth=0.300)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.30, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.29, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Set Edit Log applicability',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.39, relheight=0.07, relwidth=0.300)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.39, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.38, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Use TallyVault Password to encrypt Company Data',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.48, relheight=0.07, relwidth=0.600)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.48, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.47, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Use User Access Control',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.57, relheight=0.07, relwidth=0.600)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.57, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.56, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text='Provide Additional Base Currency details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Arial UI} -size 10",anchor="w")
        Label5.place(relx=0.05, rely=0.66, relheight=0.07, relwidth=0.600)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.700, rely=0.66, relheight=0.06, relwidth=0.02)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.65, relheight=0.08, relwidth=0.200)
        
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn.place(x=220, rely=0.80, relheight=0.10, relwidth=0.15)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def SelectCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='Select Company',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.300, rely=0.0300, relheight=0.100, relwidth=0.400)
        Label6 = Label(Frame2,text='Select Company',borderwidth="0", width=12, background="white",
                                             foreground="#00254a",
                                             font="-family {Segoe UI} -size 12 -weight bold ")
        Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.510)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.65, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame(Frame1, background="#e6ffff",borderwidth="0",relief="ridge")
        Frame3.place(relx=0.190, rely=0.130, relheight=0.900, relwidth=0.620)
        Label8 = Label(Frame3,text='  List of Companies',borderwidth="0", width=8, background="#4B77BE",
                                             foreground="white",
                                             font="-family {Segoe UI} -size 12  ",anchor="w")
        Label8.place(relx=0,rely=0, relheight=0.04, relwidth=1.000)
        Label8 = Label(Frame3,text='  Data Path/Name',borderwidth="0", width=8, background="#F5FFFA",
                                             foreground="black",
                                             font="-family {Segoe UI} -size 10  ",anchor="w")
        Label8.place(relx=0,rely=0.04, relheight=0.04, relwidth=0.400)
        Label8 = Label(Frame3,text='Number',borderwidth="0", width=8, background="#F5FFFA",
                                             foreground="black",
                                             font="-family {Segoe UI} -size 10  ",anchor="center")
        Label8.place(relx=0.400,rely=0.04, relheight=0.04, relwidth=0.200)
        Label8 = Label(Frame3,text='Period  ',borderwidth="0", width=8, background="#F5FFFA",
                                             foreground="black",
                                             font="-family {Segoe UI} -size 10  ",anchor="e")
        Label8.place(relx=0.600,rely=0.04, relheight=0.04, relwidth=0.400)
        btn4=Button(Frame3,text='Create Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=Regular)
        btn4.place(relx=0, rely=0.10, relheight=0.03, width=750)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn1=Button(Frame3,text='Select Remote Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=SelectRemoteCompany)
        btn1.place(relx=0, rely=0.13, relheight=0.03, width=750)

        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Specify Path  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=SpecifyPath)
        btn2.place(relx=0, rely=0.16, relheight=0.03, width=750)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn3=Button(Frame3,text='Select from Drive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e")
        btn3.place(relx=0, rely=0.19, relheight=0.04, width=750)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.23, relwidth=0.980, height=0)
        btn3=Button(Frame3,text='  c',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w")
        btn3.place(relx=0, rely=0.24, relheight=0.04, width=750)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        Label8 = Label(Frame3,text='  Abc',borderwidth="0", width=8, background="#e6ffff",
                                             foreground="black",
                                             font="-family {Segoe UI} -size 10  ",anchor="w")
        Label8.place(relx=0,rely=0.30, relheight=0.04, relwidth=0.400)
        Label8 = Label(Frame3,text='(10000)',borderwidth="0", width=8, background="#e6ffff",
                                             foreground="black",
                                             font="-family {Helvetica} -size 10 -slant italic ",anchor="center")
        Label8.place(relx=0.400,rely=0.30, relheight=0.04, relwidth=0.200)
        Label8 = Label(Frame3,text='1-Apr-22 to 31-Mar-23  ',borderwidth="0", width=8, background="#e6ffff",
                                             foreground="black",
                                             font="-family {Segoe UI} -size 10  ",anchor="e")
        Label8.place(relx=0.600,rely=0.30, relheight=0.04, relwidth=0.400)
        
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def SelectRemoteCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Tally.NET User Login',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",borderwidth="0", relief="ridge")
        Frame2.place(x=270, rely=0.300, relheight=0.300, relwidth=0.600)
        Label11 = Label(Frame2,text='Login as Tally.NET User',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  -weight bold ")
        Label11.place(x=280, rely=0.03, relheight=0.15, relwidth=0.250)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(x=280, rely=0.15, relheight=0, relwidth=0.250)
        Label17 = Label(Frame2,text='Tally.Net ID',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 ",anchor="w")
        Label17.place(x=25, rely=0.23, relheight=0.15, relwidth=0.150)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12")
        Label16.place(x=250, rely=0.22, relheight=0.15, relwidth=0.05)
        Entry2 = Entry(Frame2,width=10,borderwidth="3")
        Entry2.place(x=280, rely=0.23, relheight=0.15, relwidth=0.600)
        Label17 = Label(Frame2,text='Tally.NET password',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10",anchor="w")
        Label17.place(x=25, rely=0.48, relheight=0.15, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=250, rely=0.46, relheight=0.15, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=280, rely=0.48, relheight=0.15, relwidth=0.600)
        # Create a Button
        btn = Button(Frame2, text = 'Login', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=350, rely=0.75, relheight=0.18, relwidth=0.08)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        
        # Create a Button
        btn = Button(Canvas3, text = 'R: Reset Password', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10",foreground="black",anchor="w", command=ResetPassword)
        btn.place(x=5, y=380, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12")
        Label14.place(x=130, y=380, height=30, width=20)



def ResetPassword():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Reset Password',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",borderwidth="0",relief="ridge")
        Frame2.place(x=270, rely=0.300, relheight=0.300, relwidth=0.500)
        Label11 = Label(Frame2,text='Reset Password',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  -weight bold ")
        Label11.place(x=230, rely=0.15, relheight=0.08, relwidth=0.250)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(x=245, rely=0.25, relheight=0, relwidth=0.200)
        Label17 = Label(Frame2,text='Tally.Net ID',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=15, rely=0.37, relheight=0.15, relwidth=0.200)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(x=180, rely=0.37, relheight=0.15, relwidth=0.05)
        Entry2 = Entry(Frame2,width=10,borderwidth="3")
        Entry2.place(x=200, rely=0.37, relheight=0.15, relwidth=0.600)
        Label17 = Label(Frame2,text='You will receive an e-mail with a link to reset password',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Helvetica} -size 10 -slant italic ")
        Label17.place(x=200, rely=0.50, relheight=0.15, relwidth=0.600)
        # Create a Button
        btn = Button(Frame2, text = 'Login', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=270, rely=0.75, relheight=0.18, relwidth=0.15)

        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        

def SpecifyPath():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Specify Path',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",borderwidth="0",relief="ridge")
        Frame2.place(x=400, rely=0.400, relheight=0.200, relwidth=0.300)
        Label11 = Label(Frame2,text='Specify Company/Folder Path',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  -weight bold ")
        Label11.place(x=50, rely=0.10, relheight=0.20, relwidth=0.700)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(x=60, rely=0.28, relheight=0, relwidth=0.650)
        Entry2 = Entry(Frame2,width=10,borderwidth="3")
        Entry2.place(x=10, rely=0.45, relheight=0.20, relwidth=0.950)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=150, rely=0.75, relheight=0.20, relwidth=0.20)

        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)       
       

def ShutCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Shut Company',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.375, rely=0.0300, relheight=0.100, relwidth=0.220)
        Label6 = Label(Frame2,text='Shut Company',borderwidth="0", width=12, background="white",
                                             foreground="#00254a",
                                             font="-family {Segoe UI} -size 12 -weight bold ")
        Label6.place(relx=0.25, rely=0.15, relheight=0.30, relwidth=0.510)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.25, rely=0.45, relwidth=0.500, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.65, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame(Frame1, background="#e6ffff",borderwidth="0",relief="ridge")
        Frame3.place(relx=0.350, rely=0.130, relheight=0.900, relwidth=0.270)
        
        Label8 = Label(Frame3,text='  List of Companies',borderwidth="0", width=8, background="#4B77BE",
                                             foreground="white",
                                             font="-family {Segoe UI} -size 12  ",anchor="w")
        Label8.place(relx=0,rely=0, relheight=0.04, relwidth=0.999)
        btn3=Button(Frame3,text='  Abc                                                           (10000)',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn3.place(relx=0, rely=0.06, relheight=0.04, width=350)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)



def ShutCompanyChangeCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Change Company',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.370, rely=0.400, relheight=0.220, relwidth=0.290)
        Label6 = Label(Frame2,text='This will close all the open Reports, Vouchers, and \n Masters, without saving changes you might have made. \n Do you want to shut the Company?',
                       borderwidth="0", width=20, background="white",foreground="black",font="-family {Arial UI} -size 10",anchor="w")
        Label6.place(relx=0.03, rely=0.07, relheight=0.40, relwidth=0.950)
        btn = Button(Frame2, text = 'Yes', bd = '2',background="white",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="blue",anchor="w")
        btn.place(relx=0.37, rely=0.750, relheight=0.15, relwidth=0.10)
        Label6 = Label(Frame2,text='or',borderwidth="0", width=20, background="white",
                                             foreground="black",font="-family {Arial UI} -size 10",anchor="center")
        Label6.place(relx=0.47, rely=0.750, relheight=0.15, relwidth=0.10)
        btn = Button(Frame2, text = 'No', bd = '2',background="white",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="blue",anchor="w")
        btn.place(relx=0.57, rely=0.750, relheight=0.15, relwidth=0.10)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)



def MasterCreation():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  ',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.380, rely=0.03, relheight=0.150, relwidth=0.250)
        Label5 = Label(Frame2,text='Master Creation',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.30, rely=0.27, relwidth=0.400, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.45, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=420, y=150, relheight=0.700, relwidth=.270)
        Label5 = Label(Frame3,text='  List of Masters',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
        btn1=Button(Frame3,text='Change Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterChangeCompany)
        btn1.place(relx=0, rely=0.06, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Show More  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterShowmore)
        btn2.place(relx=0, rely=0.10, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.14, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  Accounting Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.15, relheight=0.04, relwidth=0.999)
        btn3=Button(Frame3,text='     Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group)
        btn3.place(relx=0, rely=0.21, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Ledger',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn4.place(relx=0, rely=0.25, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Currency',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn5.place(relx=0, rely=0.29, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     Voucher Type',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn6.place(relx=0, rely=0.33, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Inventory Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.38, relheight=0.04, relwidth=0.999)
        btn7=Button(Frame3,text='     Stock Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn7.place(relx=0, rely=0.42, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        btn8=Button(Frame3,text='     Stock Category',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn8.place(relx=0, rely=0.46, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame3,text='     Stock Item',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn9.place(relx=0, rely=0.50, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        btn10=Button(Frame3,text='     Unit',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn10.place(relx=0, rely=0.54, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn10['background'] = 'yellow'
        def on_leave(e):
            btn10['background'] = '#e6ffff'
        btn10.bind("<Enter>", on_enter)
        btn10.bind("<Leave>", on_leave)
        btn11=Button(Frame3,text='     Location',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn11.place(relx=0, rely=0.58, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn11['background'] = 'yellow'
        def on_leave(e):
            btn11['background'] = '#e6ffff'
        btn11.bind("<Enter>", on_enter)
        btn11.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Statutory Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.63, relheight=0.04, relwidth=0.999)
        btn12=Button(Frame3,text='     GST Details',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn12.place(relx=0, rely=0.67, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn12['background'] = 'yellow'
        def on_leave(e):
            btn12['background'] = '#e6ffff'
        btn12.bind("<Enter>", on_enter)
        btn12.bind("<Leave>", on_leave)
        btn13=Button(Frame3,text='     PAN/CIN Details',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn13.place(relx=0, rely=0.71, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn13['background'] = 'yellow'
        def on_leave(e):
            btn13['background'] = '#e6ffff'
        btn13.bind("<Enter>", on_enter)
        btn13.bind("<Leave>", on_leave)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def MasterChangeCompany():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Change Company',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.380, rely=0.03, relheight=0.150, relwidth=0.250)
        Label5 = Label(Frame2,text='Change Company',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.20, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.30, rely=0.33, relwidth=0.400, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.45, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=420, y=150, relheight=0.700, relwidth=.270)
        Label5 = Label(Frame3,text='  List of Masters',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
        btn1=Button(Frame3,text='Create Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=Regular)
        btn1.place(relx=0, rely=0.06, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Select Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=SelectCompany)
        btn2.place(relx=0, rely=0.10, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn3=Button(Frame3,text='Shut Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=ShutCompany)
        btn3.place(relx=0, rely=0.14, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.03, rely=0.18, relwidth=0.950, height=0)
        # Using treeview widget
        style = ttk.Style()
        style.configure(".", font=('Helvetica', 8), foreground="white",bd=0)
        style.configure("Treeview",background='green',font=('Arial', 9))
        treev = ttk.Treeview(Frame3, selectmode ='browse')
        
        # Calling pack method w.r.to treeview
        treev.grid(row=10,column=0,padx=0,pady=100)
        
        # Defining number of columns
        treev["columns"] = ("1", "2")
        
        # Defining heading
        # treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 150, anchor ='w')
        treev.column("2", width = 150, anchor ='e')
        
        # # Assigning the heading names to the
        # # respective columns
        # treev.heading("1", text ="Name")
        # treev.heading("2", text ="Sex")
        # treev.heading("3", text ="Age")
        
        # Inserting the items and their features to the
        # columns built
        treev.insert("", 'end', text ="L1",
                    values =("Nidhi", "F", "25"))
        treev.insert("", 'end', text ="L2",
                    values =("Nisha", "F", "23"))
        
          
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def MasterShowmore():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  ',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.380, rely=0.03, relheight=0.150, relwidth=0.250)
        Label5 = Label(Frame2,text='Master Creation',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.30, rely=0.27, relwidth=0.400, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.45, relheight=0.30, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=420, y=150, relheight=0.700, relwidth=.270)
        Label5 = Label(Frame3,text='  List of Masters',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
        btn1=Button(Frame3,text='Change Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterChangeCompany)
        btn1.place(relx=0, rely=0.06, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Show Less  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterCreation)
        btn2.place(relx=0, rely=0.10, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn14=Button(Frame3,text='Show Inactive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterShowInactive)
        btn14.place(relx=0, rely=0.14, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn14['background'] = 'yellow'
        def on_leave(e):
            btn14['background'] = '#e6ffff'
        btn14.bind("<Enter>", on_enter)
        btn14.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.18, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  Accounting Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.19, relheight=0.04, relwidth=0.999)
        btn3=Button(Frame3,text='     Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn3.place(relx=0, rely=0.23, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Ledger',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn4.place(relx=0, rely=0.27, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Currency',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn5.place(relx=0, rely=0.31, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     Voucher Type',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn6.place(relx=0, rely=0.35, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Inventory Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.39, relheight=0.04, relwidth=0.999)
        btn7=Button(Frame3,text='     Stock Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn7.place(relx=0, rely=0.43, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        btn8=Button(Frame3,text='     Stock Category',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn8.place(relx=0, rely=0.47, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame3,text='     Stock Item',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn9.place(relx=0, rely=0.51, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        btn10=Button(Frame3,text='     Unit',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn10.place(relx=0, rely=0.55, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn10['background'] = 'yellow'
        def on_leave(e):
            btn10['background'] = '#e6ffff'
        btn10.bind("<Enter>", on_enter)
        btn10.bind("<Leave>", on_leave)
        btn11=Button(Frame3,text='     Location',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn11.place(relx=0, rely=0.59, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn11['background'] = 'yellow'
        def on_leave(e):
            btn11['background'] = '#e6ffff'
        btn11.bind("<Enter>", on_enter)
        btn11.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Statutory Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.63, relheight=0.04, relwidth=0.999)
        btn12=Button(Frame3,text='     GST Details',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn12.place(relx=0, rely=0.67, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn12['background'] = 'yellow'
        def on_leave(e):
            btn12['background'] = '#e6ffff'
        btn12.bind("<Enter>", on_enter)
        btn12.bind("<Leave>", on_leave)
        btn13=Button(Frame3,text='     PAN/CIN Details',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn13.place(relx=0, rely=0.71, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn13['background'] = 'yellow'
        def on_leave(e):
            btn13['background'] = '#e6ffff'
        btn13.bind("<Enter>", on_enter)
        btn13.bind("<Leave>", on_leave)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def MasterShowInactive():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  ',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.380, rely=0.03, relheight=0.150, relwidth=0.250)
        Label5 = Label(Frame2,text='Master Creation',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.30, rely=0.27, relwidth=0.400, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.35, relheight=0.25, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=420, y=135, relheight=0.750, relwidth=.270)
        Label5 = Label(Frame3,text='  List of Masters',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
        btn1=Button(Frame3,text='Change Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterChangeCompany)
        btn1.place(relx=0, rely=0.06, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Show Less  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterCreation)
        btn2.place(relx=0, rely=0.10, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn111=Button(Frame3,text='Hide Inactive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterShowmore)
        btn111.place(relx=0, rely=0.14, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn111['background'] = 'yellow'
        def on_leave(e):
            btn111['background'] = '#e6ffff'
        btn111.bind("<Enter>", on_enter)
        btn111.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.18, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  Accounting Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.19, relheight=0.04, relwidth=0.999)
        btn3=Button(Frame3,text='     Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn3.place(relx=0, rely=0.23, height=17, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Ledger',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn4.place(relx=0, rely=0.26, height=17, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Cost Category',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn5.place(relx=0, rely=0.29, height=17, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     Cost Centre',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn6.place(relx=0, rely=0.32, height=17, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        btn7=Button(Frame3,text='     Cost Centre Class',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn7.place(relx=0, rely=0.35, height=17, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        btn8=Button(Frame3,text='     Currency',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn8.place(relx=0, rely=0.38, height=17, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame3,text='     Rates of Exchange',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn9.place(relx=0, rely=0.41, height=17, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        btn10=Button(Frame3,text='     Budget',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn10.place(relx=0, rely=0.44, height=17, relwidth=0.999)
        def on_enter(e):
            btn10['background'] = 'yellow'
        def on_leave(e):
            btn10['background'] = '#e6ffff'
        btn10.bind("<Enter>", on_enter)
        btn10.bind("<Leave>", on_leave)
        btn11=Button(Frame3,text='     Scenario',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn11.place(relx=0, rely=0.47, height=17, relwidth=0.999)
        def on_enter(e):
            btn11['background'] = 'yellow'
        def on_leave(e):
            btn11['background'] = '#e6ffff'
        btn11.bind("<Enter>", on_enter)
        btn11.bind("<Leave>", on_leave)
        btn12=Button(Frame3,text='     Voucher Type',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn12.place(relx=0, rely=0.50, height=17, relwidth=0.999)
        def on_enter(e):
            btn12['background'] = 'yellow'
        def on_leave(e):
            btn12['background'] = '#e6ffff'
        btn12.bind("<Enter>", on_enter)
        btn12.bind("<Leave>", on_leave)
        btn13=Button(Frame3,text='     Credit Limits',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn13.place(relx=0, rely=0.53, height=17, relwidth=0.999)
        def on_enter(e):
            btn13['background'] = 'yellow'
        def on_leave(e):
            btn13['background'] = '#e6ffff'
        btn13.bind("<Enter>", on_enter)
        btn13.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Inventory Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.57, relheight=0.04, relwidth=0.999)
        btn14=Button(Frame3,text='     Stock Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn14.place(relx=0, rely=0.61, height=17, relwidth=0.999)
        def on_enter(e):
            btn14['background'] = 'yellow'
        def on_leave(e):
            btn14['background'] = '#e6ffff'
        btn14.bind("<Enter>", on_enter)
        btn14.bind("<Leave>", on_leave)
        btn15=Button(Frame3,text='     Stock Category',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn15.place(relx=0, rely=0.64, height=17, relwidth=0.999)
        def on_enter(e):
            btn15['background'] = 'yellow'
        def on_leave(e):
            btn15['background'] = '#e6ffff'
        btn15.bind("<Enter>", on_enter)
        btn15.bind("<Leave>", on_leave)
        btn16=Button(Frame3,text='     Stock Item',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn16.place(relx=0, rely=0.67, height=17, relwidth=0.999)
        def on_enter(e):
            btn16['background'] = 'yellow'
        def on_leave(e):
            btn16['background'] = '#e6ffff'
        btn16.bind("<Enter>", on_enter)
        btn16.bind("<Leave>", on_leave)
        btn17=Button(Frame3,text='     Unit',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn17.place(relx=0, rely=0.70, height=17, relwidth=0.999)
        def on_enter(e):
            btn17['background'] = 'yellow'
        def on_leave(e):
            btn17['background'] = '#e6ffff'
        btn17.bind("<Enter>", on_enter)
        btn17.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Location',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.73,height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Price Levels',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.76, height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Price List (Stock Group)',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.79, height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn19=Button(Frame3,text='     Price List (Stock Category)',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn19.place(relx=0, rely=0.82, height=17, relwidth=0.999)
        def on_enter(e):
            btn19['background'] = 'yellow'
        def on_leave(e):
            btn19['background'] = '#e6ffff'
        btn19.bind("<Enter>", on_enter)
        btn19.bind("<Leave>", on_leave)
        btn20=Button(Frame3,text='Next',borderwidth="0",background="green",
                                             foreground="white",width=78,font="-family {Segoe UI} -size 10 ",anchor="center",command=MasterShowInactivePage1)
        btn20.place(relx=0.750, rely=0.908, height=30, relwidth=0.200)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def MasterShowInactivePage1():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  ',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.380, rely=0.03, relheight=0.150, relwidth=0.250)
        Label5 = Label(Frame2,text='Master Creation',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.30, rely=0.27, relwidth=0.400, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.35, relheight=0.25, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=420, y=135, relheight=0.750, relwidth=.270)
        Label5 = Label(Frame3,text='  List of Masters',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
        btn1=Button(Frame3,text='Change Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterChangeCompany)
        btn1.place(relx=0, rely=0.06, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Show Less  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterCreation)
        btn2.place(relx=0, rely=0.10, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn111=Button(Frame3,text='Hide Inactive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterShowmore)
        btn111.place(relx=0, rely=0.14, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn111['background'] = 'yellow'
        def on_leave(e):
            btn111['background'] = '#e6ffff'
        btn111.bind("<Enter>", on_enter)
        btn111.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.18, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  Payroll Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.19, relheight=0.04, relwidth=0.999)
        btn3=Button(Frame3,text='     Employee Category',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn3.place(relx=0, rely=0.23, height=17, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Employee Group',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn4.place(relx=0, rely=0.26, height=17, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Employee',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn5.place(relx=0, rely=0.29, height=17, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     Units (Work)',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn6.place(relx=0, rely=0.32, height=17, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        btn7=Button(Frame3,text='     Attendance/Production Type',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn7.place(relx=0, rely=0.35, height=17, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        btn8=Button(Frame3,text='     Pay Heads',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn8.place(relx=0, rely=0.38, height=17, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame3,text='     Payroll Voucher Type',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn9.place(relx=0, rely=0.41, height=17, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Statutory Masters',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.45, relheight=0.04, relwidth=0.999)
        btn14=Button(Frame3,text='     GST Classification',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn14.place(relx=0, rely=0.49, height=17, relwidth=0.999)
        def on_enter(e):
            btn14['background'] = 'yellow'
        def on_leave(e):
            btn14['background'] = '#e6ffff'
        btn14.bind("<Enter>", on_enter)
        btn14.bind("<Leave>", on_leave)
        btn15=Button(Frame3,text='     TDS Nature of Payments',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn15.place(relx=0, rely=0.52, height=17, relwidth=0.999)
        def on_enter(e):
            btn15['background'] = 'yellow'
        def on_leave(e):
            btn15['background'] = '#e6ffff'
        btn15.bind("<Enter>", on_enter)
        btn15.bind("<Leave>", on_leave)
        btn16=Button(Frame3,text='     TCS Nature of Goods',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn16.place(relx=0, rely=0.55, height=17, relwidth=0.999)
        def on_enter(e):
            btn16['background'] = 'yellow'
        def on_leave(e):
            btn16['background'] = '#e6ffff'
        btn16.bind("<Enter>", on_enter)
        btn16.bind("<Leave>", on_leave)
        btn17=Button(Frame3,text='     VAT Classification',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn17.place(relx=0, rely=0.58, height=17, relwidth=0.999)
        def on_enter(e):
            btn17['background'] = 'yellow'
        def on_leave(e):
            btn17['background'] = '#e6ffff'
        btn17.bind("<Enter>", on_enter)
        btn17.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Tax Units',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.61,height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Excise Duty Classification',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.64, height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Excise Classification',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.67, height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn19=Button(Frame3,text='     Excise Book',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn19.place(relx=0, rely=0.70, height=17, relwidth=0.999)
        def on_enter(e):
            btn19['background'] = 'yellow'
        def on_leave(e):
            btn19['background'] = '#e6ffff'
        btn19.bind("<Enter>", on_enter)
        btn19.bind("<Leave>", on_leave)
        btn21=Button(Frame3,text='     Service Category',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn21.place(relx=0, rely=0.73, height=17, relwidth=0.999)
        def on_enter(e):
            btn21['background'] = 'yellow'
        def on_leave(e):
            btn21['background'] = '#e6ffff'
        btn21.bind("<Enter>", on_enter)
        btn21.bind("<Leave>", on_leave)
        btn20=Button(Frame3,text='Next',borderwidth="0",background="green",
                                             foreground="white",width=78,font="-family {Segoe UI} -size 10 ",anchor="center",command=MasterShowInactivePage2)
        btn20.place(relx=0.750, rely=0.908, height=30, relwidth=0.200)
        btn22=Button(Frame3,text='Previous',borderwidth="0",background="green",
                                             foreground="white",width=78,font="-family {Segoe UI} -size 10 ",anchor="center",command=MasterShowInactivePage1)
        btn22.place(relx=0.05, rely=0.908, height=30, relwidth=0.200)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)



def MasterShowInactivePage2():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  ',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.380, rely=0.03, relheight=0.150, relwidth=0.250)
        Label5 = Label(Frame2,text='Master Creation',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.30, rely=0.27, relwidth=0.400, height=0)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.01, rely=0.35, relheight=0.25, relwidth=0.980)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=420, y=135, relheight=0.750, relwidth=.270)
        Label5 = Label(Frame3,text='  List of Masters',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
        btn1=Button(Frame3,text='Change Company  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterChangeCompany)
        btn1.place(relx=0, rely=0.06, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn1['background'] = 'yellow'
        def on_leave(e):
            btn1['background'] = '#e6ffff'
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)
        btn2=Button(Frame3,text='Show Less  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterCreation)
        btn2.place(relx=0, rely=0.10, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn111=Button(Frame3,text='Hide Inactive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=MasterShowmore)
        btn111.place(relx=0, rely=0.14, relheight=0.04, relwidth=0.999)
        def on_enter(e):
            btn111['background'] = 'yellow'
        def on_leave(e):
            btn111['background'] = '#e6ffff'
        btn111.bind("<Enter>", on_enter)
        btn111.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.18, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  Statutory Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.19, relheight=0.04, relwidth=0.999)
        btn3=Button(Frame3,text='     GST Details',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn3.place(relx=0, rely=0.23, height=17, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     TDS Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn4.place(relx=0, rely=0.26, height=17, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     TCS Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn5.place(relx=0, rely=0.29, height=17, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     VAT Registration Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn6.place(relx=0, rely=0.32, height=17, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        btn7=Button(Frame3,text='     Payroll Statutory Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn7.place(relx=0, rely=0.35, height=17, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        btn8=Button(Frame3,text='     Excise Registration Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn8.place(relx=0, rely=0.38, height=17, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame3,text='     Service Tax Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn9.place(relx=0, rely=0.41, height=17, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        btn14=Button(Frame3,text='     CENVAT Opening Balance',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn14.place(relx=0, rely=0.44, height=17, relwidth=0.999)
        def on_enter(e):
            btn14['background'] = 'yellow'
        def on_leave(e):
            btn14['background'] = '#e6ffff'
        btn14.bind("<Enter>", on_enter)
        btn14.bind("<Leave>", on_leave)
        btn15=Button(Frame3,text='     PLA Opening Balance',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn15.place(relx=0, rely=0.47, height=17, relwidth=0.999)
        def on_enter(e):
            btn15['background'] = 'yellow'
        def on_leave(e):
            btn15['background'] = '#e6ffff'
        btn15.bind("<Enter>", on_enter)
        btn15.bind("<Leave>", on_leave)
        btn16=Button(Frame3,text='     PAN/CIN Details',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn16.place(relx=0, rely=0.50, height=17, relwidth=0.999)
        def on_enter(e):
            btn16['background'] = 'yellow'
        def on_leave(e):
            btn16['background'] = '#e6ffff'
        btn16.bind("<Enter>", on_enter)
        btn16.bind("<Leave>", on_leave)
        btn17=Button(Frame3,text='     Dealer Excise Opening Stock',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn17.place(relx=0, rely=0.53, height=17, relwidth=0.999)
        def on_enter(e):
            btn17['background'] = 'yellow'
        def on_leave(e):
            btn17['background'] = '#e6ffff'
        btn17.bind("<Enter>", on_enter)
        btn17.bind("<Leave>", on_leave)
        btn18=Button(Frame3,text='     Excise Opening Balance',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn18.place(relx=0, rely=0.56,height=17, relwidth=0.999)
        def on_enter(e):
            btn18['background'] = 'yellow'
        def on_leave(e):
            btn18['background'] = '#e6ffff'
        btn18.bind("<Enter>", on_enter)
        btn18.bind("<Leave>", on_leave)
        btn22=Button(Frame3,text='Previous',borderwidth="0",background="green",
                                             foreground="white",width=78,font="-family {Segoe UI} -size 10 ",anchor="center",command=MasterShowInactivePage2)
        btn22.place(relx=0.05, rely=0.908, height=30, relwidth=0.200)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_Group():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="white",bd=0,relief="ridge")
        Frame2.place(relx=0, rely=0.030, relheight=0.450, relwidth=0.450)
        Label13 = Label(Frame2,text='Name',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label13.place(x=10, rely=0.03, relheight=0.06, relwidth=0.100)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.160, rely=0.03, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=120, rely=0.03, relheight=0.08, relwidth=0.450)
        Label15 = Label(Frame2,text='(alias)',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Helvetica} -size 11 -slant italic ")
        Label15.place(x=10, rely=0.10, relheight=0.06, relwidth=0.100)
        Label14 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.160, rely=0.10, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=120, rely=0.11, relheight=0.08, relwidth=0.450)
        Label17 = Label(Frame2,text='Under',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.25, relheight=0.06, relwidth=0.100)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.160, rely=0.25, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=120, rely=0.25, relheight=0.08, relwidth=0.450)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.01, rely=0.40, relwidth=0.980, height=0)
        Label17 = Label(Frame2,text='Group behaves like a sub-ledger',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.50, relheight=0.06, relwidth=0.400)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.580, rely=0.50, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=340, rely=0.50, relheight=0.08, relwidth=0.200)
        Label17 = Label(Frame2,text='Nett Debit/Credit Balances for Reporting',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.58, relheight=0.06, relwidth=0.450)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.580, rely=0.58, relheight=0.06, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=340, rely=0.59, relheight=0.08, relwidth=0.200)
        Label17 = Label(Frame2,text='Used for calculation (for example: taxes, discounts)',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.66, relheight=0.06, relwidth=0.600)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.580, rely=0.66, relheight=0.06, relwidth=0.05)
        Label15 = Label(Frame2,text='(for sales invoice entries)',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Helvetica} -size 10 -slant italic ")
        Label15.place(x=20, rely=0.71, relheight=0.06, relwidth=0.400)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(x=340, rely=0.68, relheight=0.08, relwidth=0.200)
        Label17 = Label(Frame2,text='Method to allocate when used in purchase invoice',borderwidth="0", width=8, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10  ")
        Label17.place(x=10, rely=0.79, relheight=0.06, relwidth=0.600)
        Label16 = Label(Frame2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label16.place(relx=0.580, rely=0.79, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Frame2,width=60,borderwidth="3")
        Entry2.place(x=340, rely=0.78, relheight=0.08, relwidth=0.350)
        # Create a Button
        btn = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn.place(x=200, rely=0.90, relheight=0.08, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)
        Label14 = Label(Canvas3,text='F2:Period',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=5, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=5, height=30, width=20)
        btn1 = Button(Canvas3, text = 'F3: Company', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=ChangeCompany)
        btn1.place(x=5, y=40, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=40, height=30, width=20)
        Label14 = Label(Canvas3,text='F4:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=100, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=100, height=30, width=20)
        Label14 = Label(Canvas3,text='F5:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=135, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=135, height=30, width=20)
        Label14 = Label(Canvas3,text='F6:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=170, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=170, height=30, width=20)
        Label14 = Label(Canvas3,text='F7:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=205, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=205, height=30, width=20)
        Label14 = Label(Canvas3,text='F8:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=240, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=240, height=30, width=20)
        Label14 = Label(Canvas3,text='F9:',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10  ",anchor="w")
        Label14.place(x=5, y=275, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=275, height=30, width=20)
        btn2 = Button(Canvas3, text = 'F10: Other Masters', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=MasterCreation)
        btn2.place(x=5, y=310, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=310, height=30, width=20)
        btn3 = Button(Canvas3, text = 'I: More Details', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=AccountingMasters_Group_MoreDetails)
        btn3.place(x=5, y=345, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=345, height=30, width=20)
        # Create a Button
        btn = Button(Canvas3, text = 'F12: Configure', bd = '0',background="white",
                        font="-family {Segoe UI} -size 10  ",foreground="black",anchor="w", command=Configure)
        btn.place(x=5, y=580, height=30, width=120)
        Label14 = Label(Canvas3,text='<',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(x=130, y=580, height=30, width=20)


def AccountingMasters_Group_MoreDetails():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.340, rely=0.03, relheight=0.150, relwidth=0.330)
        Label5 = Label(Frame2,text='More Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.38, rely=0.27, relwidth=0.250, height=0)
        Label5 = Label(Frame2,text='Under',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.37, relheight=0.15, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.37, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.37, relheight=0.20, relwidth=0.500)
        Label5 = Label(Frame2,text='Add',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.60, relheight=0.15, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.60, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.60, relheight=0.20, relwidth=0.500)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=350, y=160, relheight=0.250, relwidth=.380)
        Label5 = Label(Frame3,text='  List of Group Details',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.10, relwidth=1.000)
        btn2=Button(Frame3,text='Show More  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn2.place(relx=0, rely=0.20, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        # Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.30, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  General Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.35, relheight=0.08, relwidth=0.999)
        btn3=Button(Frame3,text='     Name and Alias                                                               Ddff',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group)
        btn3.place(relx=0, rely=0.45, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Group behaves like a Sub-ledger                                      Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn4.place(relx=0, rely=0.53, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Nett Credit/Debit Balances for Reporting                           Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=ShutCompanyChangeCompany)
        btn5.place(relx=0, rely=0.65, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        # Create a Button
        btn = Button(Frame3, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn.place(x=200, rely=0.80, relheight=0.15, relwidth=0.20)

        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)



def AccountingMasters_Group_ShowMore():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.340, rely=0.03, relheight=0.150, relwidth=0.330)
        Label5 = Label(Frame2,text='More Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.38, rely=0.27, relwidth=0.250, height=0)
        Label5 = Label(Frame2,text='Under',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.37, relheight=0.15, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.37, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.37, relheight=0.20, relwidth=0.500)
        Label5 = Label(Frame2,text='Add',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.60, relheight=0.15, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.60, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.60, relheight=0.20, relwidth=0.500)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=350, y=160, relheight=0.350, relwidth=.380)
        Label5 = Label(Frame3,text='  List of Group Details',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.10, relwidth=1.000)
        btn2=Button(Frame3,text='Show Less  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=AccountingMasters_Group_MoreDetails)
        btn2.place(relx=0, rely=0.15, relheight=0.08, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn33=Button(Frame3,text='Show Inactive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=AccountingMasters_Group_ShowInactive)
        btn33.place(relx=0, rely=0.22, relheight=0.08, relwidth=0.999)
        def on_enter(e):
            btn33['background'] = 'yellow'
        def on_leave(e):
            btn33['background'] = '#e6ffff'
        btn33.bind("<Enter>", on_enter)
        btn33.bind("<Leave>", on_leave)
        #Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.30, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  General Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.31, relheight=0.08, relwidth=0.999)
        btn3=Button(Frame3,text='     Name and Alias                                                               Ddff',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_NameAndAlias)
        btn3.place(relx=0, rely=0.39, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn31=Button(Frame3,text='     Language Alias                                                               ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_LanguageAlias)
        btn31.place(relx=0, rely=0.45, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn31['background'] = 'yellow'
        def on_leave(e):
            btn31['background'] = '#e6ffff'
        btn31.bind("<Enter>", on_enter)
        btn31.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Group behaves like a Sub-ledger                                      Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_GroupBehaviour)
        btn4.place(relx=0, rely=0.53, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Nett Credit/Debit Balances for Reporting                           Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_NettCreditdebitbalance)
        btn5.place(relx=0, rely=0.61, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     Use for calculation                                                           Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_Calculation)
        btn6.place(relx=0, rely=0.69, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        btn7=Button(Frame3,text='     Method of allocation in Purchase Invoice                           Not Applicable',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_MethodofAllocation)
        btn7.place(relx=0, rely=0.77, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        # Create a Button
        btn10 = Button(Frame3, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=200, rely=0.88, relheight=0.10, relwidth=0.20)

        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_Group_ShowInactive():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='     Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X      ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e")
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)

        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.340, rely=0.03, relheight=0.150, relwidth=0.330)
        Label5 = Label(Frame2,text='More Details',bd=0, width=5, background="white",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.38, rely=0.27, relwidth=0.250, height=0)
        Label5 = Label(Frame2,text='Under',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.37, relheight=0.15, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.37, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.37, relheight=0.20, relwidth=0.500)
        Label5 = Label(Frame2,text='Add',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.60, relheight=0.15, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.60, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.60, relheight=0.20, relwidth=0.500)

        global Frame3
        Frame3 = tk.Frame( background="#e6ffff", relief="ridge",bd=0)
        Frame3.place(x=350, y=160, relheight=0.450, relwidth=.380)
        Label5 = Label(Frame3,text='  List of Group Details',bd=0, width=5, background="#3385ff",
                                            foreground="white",
                                            font="-family {Segoe UI} -size 12 ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.08, relwidth=1.000)
        btn2=Button(Frame3,text='Show Less  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=AccountingMasters_Group_MoreDetails)
        btn2.place(relx=0, rely=0.13, relheight=0.08, relwidth=0.999)
        def on_enter(e):
            btn2['background'] = 'yellow'
        def on_leave(e):
            btn2['background'] = '#e6ffff'
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)
        btn33=Button(Frame3,text='Hide Inactive  ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn33.place(relx=0, rely=0.19, relheight=0.08, relwidth=0.999)
        def on_enter(e):
            btn33['background'] = 'yellow'
        def on_leave(e):
            btn33['background'] = '#e6ffff'
        btn33.bind("<Enter>", on_enter)
        btn33.bind("<Leave>", on_leave)
        #Separator object
        separator = ttk.Separator(Frame3, orient='horizontal')
        separator.place(relx=0.01, rely=0.26, relwidth=0.980, height=0)
        Label5 = Label(Frame3,text='  General Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.27, relheight=0.08, relwidth=0.999)
        btn3=Button(Frame3,text='     Name and Alias                                                               Ddff',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_NameAndAlias)
        btn3.place(relx=0, rely=0.33, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn3['background'] = 'yellow'
        def on_leave(e):
            btn3['background'] = '#e6ffff'
        btn3.bind("<Enter>", on_enter)
        btn3.bind("<Leave>", on_leave)
        btn31=Button(Frame3,text='     Language Alias                                                               ',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_LanguageAlias)
        btn31.place(relx=0, rely=0.39, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn31['background'] = 'yellow'
        def on_leave(e):
            btn31['background'] = '#e6ffff'
        btn31.bind("<Enter>", on_enter)
        btn31.bind("<Leave>", on_leave)
        btn4=Button(Frame3,text='     Group behaves like a Sub-ledger                                      Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_GroupBehaviour)
        btn4.place(relx=0, rely=0.45, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn4['background'] = 'yellow'
        def on_leave(e):
            btn4['background'] = '#e6ffff'
        btn4.bind("<Enter>", on_enter)
        btn4.bind("<Leave>", on_leave)
        btn5=Button(Frame3,text='     Nett Credit/Debit Balances for Reporting                           Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_NettCreditdebitbalance)
        btn5.place(relx=0, rely=0.51, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn5['background'] = 'yellow'
        def on_leave(e):
            btn5['background'] = '#e6ffff'
        btn5.bind("<Enter>", on_enter)
        btn5.bind("<Leave>", on_leave)
        btn6=Button(Frame3,text='     Use for calculation                                                           Yes',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_Group_Calculation)
        btn6.place(relx=0, rely=0.57, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn6['background'] = 'yellow'
        def on_leave(e):
            btn6['background'] = '#e6ffff'
        btn6.bind("<Enter>", on_enter)
        btn6.bind("<Leave>", on_leave)
        btn7=Button(Frame3,text='     Method of allocation in Purchase Invoice                           Not Applicable',borderwidth="0",background="#e6ffff",
                                             foreground="black",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_MethodofAllocation)
        btn7.place(relx=0, rely=0.62, relheight=0.10, relwidth=0.999)
        def on_enter(e):
            btn7['background'] = 'yellow'
        def on_leave(e):
            btn7['background'] = '#e6ffff'
        btn7.bind("<Enter>", on_enter)
        btn7.bind("<Leave>", on_leave)
        Label5 = Label(Frame3,text='  Statutory Details',bd=0, width=5, background="#e6ffff",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 10 -weight bold",anchor="w")
        Label5.place(relx=0, rely=0.70, relheight=0.06, relwidth=0.999)
        btn8=Button(Frame3,text='     TDS Details',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_TDSDetails)
        btn8.place(relx=0, rely=0.76, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn8['background'] = 'yellow'
        def on_leave(e):
            btn8['background'] = '#e6ffff'
        btn8.bind("<Enter>", on_enter)
        btn8.bind("<Leave>", on_leave)
        btn9=Button(Frame3,text='     TDS Details (History)',borderwidth="0",background="#e6ffff",
                                             foreground="#808080",width=78,font="-family {Segoe UI} -size 10 ",anchor="w",command=AccountingMasters_TDSDetails)
        btn9.place(relx=0, rely=0.82, relheight=0.06, relwidth=0.999)
        def on_enter(e):
            btn9['background'] = 'yellow'
        def on_leave(e):
            btn9['background'] = '#e6ffff'
        btn9.bind("<Enter>", on_enter)
        btn9.bind("<Leave>", on_leave)
        # # Create a Button
        btn10 = Button(Frame3, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=200, rely=0.89, relheight=0.08, relwidth=0.20)

        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_Group_NameAndAlias():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.370, rely=0.400, relheight=0.220, relwidth=0.290)
        Label5 = Label(Frame2,text='Name and Alias',bd=0, width=5, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.10, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.33, rely=0.26, relwidth=0.340, height=0)
        Label5 = Label(Frame2,text='Name',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.37, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.36, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.37, relheight=0.15, relwidth=0.600)
        Label5 = Label(Frame2,text='(alias)',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Helvetica} -size 11 -slant italic ")
        Label5.place(relx=0.03, rely=0.55, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.54, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.55, relheight=0.15, relwidth=0.600)
        # # Create a Button
        btn10 = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=150, rely=0.75, relheight=0.15, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_Group_LanguageAlias():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.370, rely=0.400, relheight=0.300, relwidth=0.290)
        Label5 = Label(Frame2,text='Language Alias',bd=0, width=5, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.07, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.33, rely=0.20, relwidth=0.340, height=0)
        Label5 = Label(Frame2,text='English',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.27, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.24, relheight=0.15, relwidth=0.05)
        Label5 = Label(Frame2,text='Name',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.10, rely=0.38, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.35, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.36, relheight=0.10, relwidth=0.600)
        Label5 = Label(Frame2,text='(alias)',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Helvetica} -size 11 -slant italic ")
        Label5.place(relx=0.10, rely=0.49, relheight=0.08, relwidth=0.200)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.300, rely=0.46, relheight=0.15, relwidth=0.05)
        Entry1 = Entry(Frame2,width=60,borderwidth="3")
        Entry1.place(relx=0.350, rely=0.48, relheight=0.10, relwidth=0.600)
        # # Create a Button
        btn10 = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=140, rely=0.70, relheight=0.15, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_Group_GroupBehaviour():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.350, rely=0.400, relheight=0.200, relwidth=0.290)
        Label5 = Label(Frame2,text='Group Behaviour',bd=0, width=5, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.25, rely=0.07, relheight=0.15, relwidth=0.500)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.33, rely=0.20, relwidth=0.340, height=0)
        Label5 = Label(Frame2,text='Group behaves like a sub-ledger',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.33, relheight=0.15, relwidth=0.600)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.650, rely=0.31, relheight=0.15, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.730, rely=0.32, relheight=0.13, relwidth=0.230)
        # # Create a Button
        btn10 = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=140, rely=0.65, relheight=0.20, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)

def AccountingMasters_Group_NettCreditdebitbalance():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.350, rely=0.400, relheight=0.200, relwidth=0.290)
        Label5 = Label(Frame2,text='Nett Credit/Debit Balances',bd=0, width=5, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.15, rely=0.07, relheight=0.15, relwidth=0.700)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.20, rely=0.22, relwidth=0.595, height=0)
        Label5 = Label(Frame2,text='Nett Debit/Credit Balances for Reporting',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.33, relheight=0.15, relwidth=0.680)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.720, rely=0.32, relheight=0.15, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.750, rely=0.32, relheight=0.13, relwidth=0.230)
        # # Create a Button
        btn10 = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=140, rely=0.65, relheight=0.20, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_Group_Calculation():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.300, rely=0.400, relheight=0.200, relwidth=0.400)
        Label5 = Label(Frame2,text='Calculation',bd=0, width=5, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.30, rely=0.07, relheight=0.15, relwidth=0.400)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.41, rely=0.22, relwidth=0.190, height=0)
        Label5 = Label(Frame2,text='Used for calculation (for example: taxes, discounts)',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.33, relheight=0.15, relwidth=0.680)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.700, rely=0.32, relheight=0.15, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Yes", "No"])
        combo.place(relx=0.730, rely=0.32, relheight=0.13, relwidth=0.230)
        # # Create a Button
        btn10 = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=195, rely=0.65, relheight=0.20, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_MethodofAllocation():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  Group Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowMore)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.250, rely=0.400, relheight=0.200, relwidth=0.500)
        Label5 = Label(Frame2,text='Method of Allocation',bd=0, width=5, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12 -weight bold ",anchor="center")
        Label5.place(relx=0.30, rely=0.07, relheight=0.15, relwidth=0.400)
        # Separator object
        separator = ttk.Separator(Frame2, orient='horizontal')
        separator.place(relx=0.36, rely=0.22, relwidth=0.275, height=0)
        Label5 = Label(Frame2,text='Method to allocate when used in purchase invoice',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.03, rely=0.33, relheight=0.15, relwidth=0.680)
        Label5 = Label(Frame2,text=':',bd=0, width=5, background="white",
                                            foreground="black",anchor="w",
                                            font="-family {Segoe UI} -size 10 ")
        Label5.place(relx=0.600, rely=0.32, relheight=0.15, relwidth=0.05)
        combo = ttk.Combobox(Frame2,values=["Not Applicable", "Appropriate by Qty", "Appropriate by Value"])
        combo.place(relx=0.640, rely=0.32, relheight=0.15, relwidth=0.330)
        # # Create a Button
        btn10 = Button(Frame2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white",command=CompanyFeaturesAlteration)
        btn10.place(x=195, rely=0.65, relheight=0.20, relwidth=0.20)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)


def AccountingMasters_TDSDetails():
    
        global Frame1
        Frame1 = tk.Frame( background="#B0B0B0", relief="ridge",bd=0)
        Frame1.place(relx=0, rely=0.07, relheight=0.890, relwidth=.880)
        Label5 = Label(Frame1,text='  MoreDetails TDSDetails',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="w")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.250)
        Label5 = Label(Frame1,text='Abc',bd=0, width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ",anchor="center")
        Label5.place(relx=0.20, rely=0, relheight=0.03, relwidth=0.600)
        # Create a Button
        btn = Button(Frame1, text = 'X   ', bd = '2',background="#3385ff",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="#00254a",anchor="e",command=AccountingMasters_Group_ShowInactive)
        btn.place(x=900, rely=0, relheight=0.03, relwidth=0.250)


        global Frame2
        Frame2 = tk.Frame(Frame1, background="#ffffff",relief="ridge")
        Frame2.place(relx=0.370, rely=0.400, relheight=0.220, relwidth=0.290)
        Label6 = Label(Frame2,text='You need to enable the TDS feature \n for your Company.',
                       borderwidth="0", width=20, background="white",foreground="black",font="-family {Arial UI} -size 10",anchor="w")
        Label6.place(relx=0.20, rely=0.07, relheight=0.40, relwidth=0.950)
        Label6 = Label(Frame2,text='Enable now?',
                       borderwidth="0", width=20, background="white",foreground="black",font="-family {Arial UI} -size 10",anchor="w")
        Label6.place(relx=0.40, rely=0.50, relheight=0.10, relwidth=0.950)
        btn = Button(Frame2, text = 'Yes', bd = '2',background="white",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="blue",anchor="w")
        btn.place(relx=0.37, rely=0.750, relheight=0.15, relwidth=0.10)
        Label6 = Label(Frame2,text='or',borderwidth="0", width=20, background="white",
                                             foreground="black",font="-family {Arial UI} -size 10",anchor="center")
        Label6.place(relx=0.47, rely=0.750, relheight=0.15, relwidth=0.10)
        btn = Button(Frame2, text = 'No', bd = '2',background="white",borderwidth="0",
                       font="-family {Segoe UI} -size 12  ",foreground="blue",anchor="w")
        btn.place(relx=0.57, rely=0.750, relheight=0.15, relwidth=0.10)
        
        global Canvas3
        Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
        Canvas3.place(relx=0.880, rely=0.07, relheight=0.82, relwidth=0.130)



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
                                     foreground="black",width=78,font="-family {Segoe UI} -size 12 ",command=SpecifyPath)
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
