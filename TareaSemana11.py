# importamos la libreria tkinter  

from distutils import command
from logging import root
from msilib.schema import Icon
from tkinter import Tk , Button, Label, filedialog, messagebox
from PIL import Image,ImageTk, ImageFilter


# Importamos la libreria para nuestra imagen 
#from PIL import Image 



class Mostrar():

    def __init__(self):
        self.archivo=""

    # Funcion para subir imagen desde los archivos 
    def carga_Imagen(self):
        self.archivo = filedialog.askopenfilename()
        Nuestra_Imagen = Image.open(self.archivo)
        tamaño = Nuestra_Imagen.resize((800,536),Image.Resampling.LANCZOS)
        llevar_a = ImageTk.PhotoImage(tamaño)
        Imagen.configure(image=llevar_a)
        Imagen.image = llevar_a
    # Funcion para aplicar efecto blanco y negro 
    def Blanco(self):
        if self.archivo !="":
            Nuestra_Imagen1 = Image.open(self.archivo)
            blanco_negro = Nuestra_Imagen1.convert("L")
            tamaño = blanco_negro.resize((800,536),Image.Resampling.LANCZOS)
            llevar_a = ImageTk.PhotoImage(tamaño)
            Imagen.configure(image=llevar_a)
            Imagen.image = llevar_a
            blanco_negro.save("BlacoNegro.jpg")
            messagebox.showinfo("Imagen","Se aplico efecto")
        else: 
            messagebox.showerror("Imagen", "Necesita cargar una imagen")
    # Funcion para aplicar efecto desenfocar
    def desenfocar(self):
        if self.archivo !="":
            Nuestra_Imagen1 = Image.open(self.archivo)
            blanco_negro = Nuestra_Imagen1.filter(ImageFilter.BLUR)
            tamaño = blanco_negro.resize((800,536),Image.Resampling.LANCZOS)
            llevar_a = ImageTk.PhotoImage(tamaño)
            Imagen.configure(image=llevar_a)
            Imagen.image = llevar_a
            blanco_negro.save("BlacoNegro.jpg")
            messagebox.showinfo("Imagen","Se aplico efecto")
        else: 
            messagebox.showerror("Imagen", "Necesita cargar una imagen")
    # Funcion para aplicar efecto contorno 
    def contorno(self):
        if self.archivo !="":
            Nuestra_Imagen1 = Image.open(self.archivo)
            blanco_negro = Nuestra_Imagen1.filter(ImageFilter.CONTOUR)
            tamaño = blanco_negro.resize((800,536),Image.Resampling.LANCZOS)
            llevar_a = ImageTk.PhotoImage(tamaño)
            Imagen.configure(image=llevar_a)
            Imagen.image = llevar_a
            blanco_negro.save("BlacoNegro.jpg")
            messagebox.showinfo("Imagen","Se aplico efecto")
        else: 
            messagebox.showerror("Imagen", "Necesita cargar una imagen")
    # Funcion para aplicar efecto resaltar
    def Resal(self):
        if self.archivo !="":
            Nuestra_Imagen1 = Image.open(self.archivo)
            blanco_negro = Nuestra_Imagen1.filter(ImageFilter.EMBOSS)
            tamaño = blanco_negro.resize((800,536),Image.Resampling.LANCZOS)
            llevar_a = ImageTk.PhotoImage(tamaño)
            Imagen.configure(image=llevar_a)
            Imagen.image = llevar_a
            blanco_negro.save("BlacoNegro.jpg")
            messagebox.showinfo("Imagen","Se aplico efecto")
        else: 
            messagebox.showerror("Imagen", "Necesita cargar una imagen")


# Creamos nuestra interfaz 

Interfaz = Tk ()

# Componentes para  nuestra ventana 
Interfaz.title("Edicion de Imagen") # Añadimos titulo
Interfaz.geometry("1600x950") # Añadimos expansion 
Interfaz.iconbitmap(r'C:\edicion.ico')
Interfaz.config(bg= "#1A1818") # Para cambiar el color de la ventana

# Label de cargar Imagen 
Imagen = Label(Interfaz,text="Debes subir imagen",bg = "white")
Imagen.place(x= 260,y=110, width=800,height=536)


laclase = Mostrar()
# Este es el boton para cargar la imagen 
Cargar_Imagen = Button(Interfaz, text="Subir Imagen", bg= "deep sky blue", command=laclase.carga_Imagen)
Cargar_Imagen.place(x=360, y= 670, width=600,height=30)


Cargar_Imagen = Button(Interfaz, text="Blanco/Negro", bg= "deep sky blue",command= laclase.Blanco )
Cargar_Imagen.place(x=1200, y= 200, width=100,height=30)

Cargar_Imagen = Button(Interfaz, text="Desenfocar", bg= "deep sky blue", command=laclase.desenfocar)
Cargar_Imagen.place(x=1200, y= 300, width=100,height=30)

Cargar_Imagen = Button(Interfaz, text="Contorno", bg= "deep sky blue", command=laclase.contorno )
Cargar_Imagen.place(x=1200, y= 400, width=100,height=30)

Cargar_Imagen = Button(Interfaz, text="Resaltar", bg= "deep sky blue",command=laclase.Resal )
Cargar_Imagen.place(x=1200, y= 500, width=100,height=30)

# Mostrar la interfaz
Interfaz.mainloop() 
