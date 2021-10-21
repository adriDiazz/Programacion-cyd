from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as ms
import csv

#Funciones



def guardar():
    #recogemos informacion-------
    gnombre=nombre.get()
    gapellido=apellidos.get()
    gemail=email.get() + emailadress.get()
    print(gemail)
    ggender=gender.get()

    #-------if vacio-----------
    if(gnombre == "" or gapellido== ""):
        print("Error")
        messagebox.showerror("Error",message="Error escribe los campos obligatorios")
        gnombre=nombre.set("")
        gapellido=apellidos.set("")
        gemail=email.set("")
    else:
        print("Registrado correctamente")

        with open ('clientes.csv','a',newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([gnombre,gapellido,gemail,ggender])
        csvfile.close

def clear():
    gnombre=nombre.set("")
    gapellido=apellidos.set("")
    gemail=email.set("")

def ayuda():
    messagebox.showerror("Ayuda",message="Escribe la informacion y pulsa guardar")







#GUI
window = Tk()
window.config(background="light grey")
window.geometry("600x400")

#-------Creamos las variables que vamos a usar----------------------------------------
nombre=StringVar()
apellidos=StringVar()
email= StringVar()
emailadress=StringVar()
gender=IntVar()
#--------------------------------------------------------------------------------------
heading=Label(window,bg="light grey",text="NUEVO CLIENTE ",font=('Arial',14,"bold"))
heading.place(relx = 0.65,rely = 0.0,anchor='ne')
#-------------Name---------------------------------------------------------------------
name=Label(window,bg="light grey",text="Nombre: ",font=('Arial',8,"bold"))
name.place(relx = 0.243,rely = 0.25,anchor='ne')
entryName=Entry(window,textvariable=nombre)
entryName.place(relx = 0.4544,rely = 0.25,anchor='ne')
#------------Apellido-------------------------------------------------------------------
apellLbl=Label(window,bg="light grey",text="Apellidos:  ",font=('Arial',8,"bold"))
apellLbl.place(relx = 0.25,rely = 0.35,anchor='ne')
entrysurName=Entry(window,textvariable=apellidos)
entrysurName.place(relx = 0.4544,rely = 0.35,anchor='ne')
#------------------Email------------------------------------------------------------------
maillbl=Label(window,bg="light grey",text="Email:   ",font=('Arial',8,"bold"))
maillbl.place(relx = 0.25,rely = 0.45,anchor='ne')
entryMail=Entry(window,textvariable=email)
entryMail.place(relx = 0.4544,rely = 0.45,anchor='ne')

list1=['@hotmail.com','@gmail.com','@yahoo.com']
droplist=OptionMenu(window,emailadress,*list1)
emailadress.set('@hotmail.com')
droplist.place(relx = 0.67,rely = 0.44,anchor='ne')
#----------------Gender-------------------------------------------------------------------
lblgender=Label(window,bg="light grey",text="Gender:  ",font=('Arial',8,"bold"))
lblgender.place(relx = 0.246,rely = 0.55,anchor='ne')

radiobutton1=Radiobutton(window,text="Male",variable=gender,value=1,font=('Arial',8,"bold"))
radiobutton1.place(relx = 0.33,rely = 0.55,anchor='ne')
radiobutton2=Radiobutton(window,text="Female",variable=gender,value=2,font=('Arial',8,"bold"))
radiobutton2.place(relx = 0.50,rely = 0.55,anchor='ne')
#-------------------botones----------------------------------------------------------------
button1=Button(window,text="Guardar",command=guardar)
button1.place(relx = 0.70,rely = 0.70,anchor='ne')
button2=Button(window,text="Clear",command=clear)
button2.place(relx = 0.50,rely = 0.70,anchor='ne')
button3=Button(window,text="Ayuda",command=ayuda)
button3.place(relx = 0.30,rely = 0.70,anchor='ne')

window.mainloop()