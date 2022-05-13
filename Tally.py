from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk


def account():
    
        global Canvas1
        Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
        Canvas1.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
        Label5 = Label(Canvas1,text='Company Creation',borderwidth="0", width=5, background="#3385ff",
                                            foreground="#00254a",
                                            font="-family {Segoe UI} -size 10 -weight bold ")
        Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


        global Canvas2
        Canvas2 = tk.Canvas(Canvas1, background="white",borderwidth="1", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
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
        Label13.place(x=550, rely=0.15, relheight=0.06, relwidth=0.210)
        Label14 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.755, rely=0.15, relheight=0.06, relwidth=0.02)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=790, rely=0.16, relheight=0.04, relwidth=0.200)
        Label13 = Label(Canvas2,text='Books beginning from',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label13.place(x=545, rely=0.20, relheight=0.06, relwidth=0.170)
        Label14 = Label(Canvas2,text=':',borderwidth="0", width=8, background="white",
                                            foreground="black",
                                            font="-family {Segoe UI} -size 12  ")
        Label14.place(relx=0.740, rely=0.20, relheight=0.06, relwidth=0.05)
        Entry2 = Entry(Canvas2,width=60,borderwidth="3")
        Entry2.place(x=790, rely=0.21, relheight=0.04, relwidth=0.200)
        # Create a Button
        btn = Button(Canvas2, text = 'Save', bd = '2',background="green",
                        font="-family {Segoe UI} -size 12  ",foreground="white")
        btn.place(x=500, rely=0.90, relheight=0.06, relwidth=0.08)

       
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
          
sbmibtn=Button(screen,text='K:Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=account).place(x=20,y=10)
sbmibtn=Button(screen,text='Y:Data',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=180,y=10)
sbmibtn=Button(screen,text='Z:Exchange',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=340,y=10)
sbmibtn=Button(screen,text='G:Go To',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=600,y=10)
sbmibtn=Button(screen,text='O:Import',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=850,y=10)
sbmibtn=Button(screen,text='E:Export',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=990,y=10)
sbmibtn=Button(screen,text='M:E-mail',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)
sbmibtn=Button(screen,text='P:Print',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1270,y=10)
sbmibtn=Button(screen,text='F1:Help',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1400,y=10)

global Canvas1
Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.820, relwidth=.850)
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
# Creating Listbox
Lb = Listbox(Canvas2, height=6,  background="#e6ffff", font="-family {Segoe UI} -size 12  ",justify='right')
# Inserting items in Listbox
Lb.insert(0, 'Create Company')
Lb.insert(1, 'Select Remote Company')
Lb.insert(2, 'Specify Path')
Lb.insert(3, 'Select From Drive')
Lb.place(relx=0.0, rely=0.07, relheight=0.13, relwidth=0.999)


global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.82, relwidth=0.150)
screen.mainloop()
