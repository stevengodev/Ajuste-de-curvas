import tkinter as tk
from PIL import ImageTk, Image
from dashboard import Dashboard

# Crear la ventana principal
ventana = tk.Tk()

# Establecer las propiedades de la ventana
ventana.title("Ajustes de curvas")
ventana.geometry("1200x600")

# Cargar la imagen de fondo
imagen_fondo = Image.open("FONDO_curvas.jpg")
imagen_fondo = imagen_fondo.resize((1200, 600), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget de etiqueta para el fondo
fondo_etiqueta = tk.Label(ventana, image=fondo)
fondo_etiqueta.place(x=0, y=0, relwidth=1, relheight=1)



# Crear un label para indicar la entrada de datos


etiqueta_x = tk.Label(ventana, text="DATOS PARA X:", font=("Poppins"))
etiqueta_x.place(relx=0.5, rely=0.4, anchor="center")

entrada_x = tk.Entry(ventana, width=50, font=("Poppins", 14))
entrada_x.place(relx=0.5, rely=0.45, anchor="center")

etiqueta_y = tk.Label(ventana, text="DATOS PARA Y:", font=("Poppins"))
etiqueta_y.place(relx=0.5, rely=0.5, anchor="center")

entrada_y = tk.Entry(ventana, width=50, font=("Poppins", 14))
entrada_y.place(relx=0.5, rely=0.55, anchor="center")
from tkinter import ttk

# Crear estilo
style = ttk.Style()
style.configure("TButton", background="white", font=("Poppins ExtraLight", 14), borderwidth=0, relief="solid")

# Crear botón
boton = ttk.Button(ventana, text="CALCULAR AJUSTES", style="TButton", command=lambda: Dashboard.iniciarDashboard(entrada_x.get(), entrada_y.get()))
boton.place(relx=0.5, rely=0.65, anchor="center")



# Ejecutar la aplicación
ventana.mainloop()
