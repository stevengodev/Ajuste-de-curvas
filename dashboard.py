from tkinter import *
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from modelos import *
from ajustes import *
from scipy.optimize import curve_fit


class Dashboard:
    def iniciarDashboard(entrada_x:str, entrada_y:str):

        # ==============================================================================
        # ================== DATOS ORIGINALES ==========================================
        # ==============================================================================
        
        arreglo_x = entrada_x.split(",")
        arreglo_y = entrada_y.split(",")
        lista_x = [float(numero_x) for numero_x in arreglo_x]
        lista_y = [float(numero_y) for numero_y in arreglo_y]

        x = np.array(lista_x)                           #Conjunto de datos x
        y = np.array(lista_y)                           #Conjunto de datos y

        coeficiente_corr_original = np.corrcoef(x, y)[0, 1]
        coeficiente_det_original = coeficiente_corr_original**2

        # ==============================================================================
        # ================== AJUSTE LINEAL =============================================
        # ==============================================================================

        b_lineal, a_lineal = ajuste_lineal(x, y)
        nueva_y_lineal = linear_func(x, a_lineal, b_lineal)
        coeficiente_corr_lineal = np.corrcoef(x, nueva_y_lineal)[0, 1]
        coeficiente_det_lineal = coeficiente_corr_lineal**2

        # ==============================================================================
        # ================== AJUSTE EXPONENCIAL ========================================
        # ==============================================================================

        coef_exp = np.polyfit(x, np.log(y), 1)

        a_exp = np.exp(coef_exp[1])
        b_exp = coef_exp[0] 
        nueva_y_exp = exponential_func(x,a_exp, b_exp)

        coeficiente_corr_exp = np.corrcoef(x, nueva_y_exp)[0, 1]
        coeficiente_det_exp = coeficiente_corr_exp**2

        # ==============================================================================
        # ================== AJUSTE LOGARITMICO ========================================
        # ==============================================================================  

        coef_log = np.polyfit(np.log(x), y, 1)
        a_log = coef_log[1]
        b_log = coef_log[0]
        nueva_y_log = logarithmic_func(x, a_log, b_log)

        coeficiente_corr_log = np.corrcoef(x, nueva_y_log)[0, 1]
        coeficiente_det_log = coeficiente_corr_log**2  

        # ==============================================================================
        # ================== AJUSTE POTENCIAL ==========================================
        # ============================================================================== 

        b_pot, a_pot = ajuste_potencial(x,y)
        nueva_y_pot = potential_func(x, a_pot, b_pot)
        coeficiente_corr_pot = np.corrcoef(x, nueva_y_pot)[0, 1]
        coeficiente_det_pot = coeficiente_corr_pot**2

        # ==============================================================================
        # ================== AJUSTE HIPERBOLICO ========================================
        # ==============================================================================
        popt, pcov = curve_fit(hiperbolic_func, x, y)
        a_hiper = popt[0]
        b_hiper = popt[1]
        nueva_y_hip = hiperbolic_func(x,a_hiper, b_hiper)

        coeficiente_corr_hip = np.corrcoef(x, nueva_y_hip)[0, 1]
        coeficiente_det_hip = coeficiente_corr_hip**2

        # ==============================================================================
        # ================== CREACION DE LA INTERFAZ ===================================
        # ==============================================================================
        window = Tk()

        window.title("Proyecto")
        window.geometry("1366x768")
        window.resizable(0, 0)
        window.state('zoomed')
        window.config(background='white')

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================

        header = Frame(window, bg='#009df4')
        header.place(x=0, y=0, width=1800, height=60)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        heading = Label(window, text='Ajuste de curvas', font=("", 15, "bold"), bg='#009df4')
        heading.place(x=600, y=15)

        # body frame 1
        bodyFrame1 = Frame(window, bg='#ffffff')
        bodyFrame1.place(x=0, y=60, width=1800, height=1000)

        # =============================================================================
        # ============= GRAFICA =======================================================
        # =============================================================================        

        fig = Figure(figsize=(7.5, 6.5))
        ax = fig.add_subplot(111)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        ax.set_title("Ajustes de curvas")
        ax.scatter(x, y, label='Funcion original')
        ax.plot(x, nueva_y_lineal, color='orange', label='Modelo lineal')
        ax.plot(x, nueva_y_exp, color='green', label='Modelo exponencial')
        ax.plot(x, nueva_y_log, color='red', label='Ajuste logarítmico')
        ax.plot(x, nueva_y_pot, color='yellow', label='Ajuste potencial')
        ax.plot(x, nueva_y_hip, color='pink', label='Modelo hiperbólico')
        ax.legend()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().place(x=0, y=60)

        # =============================================================================
        # ============= TABLA  ========================================================
        # =============================================================================
         
        df = Dashboard.crearTabla(x,y,nueva_y_lineal,nueva_y_exp,nueva_y_log,nueva_y_pot,nueva_y_hip)
        data_str = df.to_string(index=False)

        table_title = Label(window, text='Muestra de datos', font=("", 15, "bold"), bg='white')
        table_title.place(x=900, y=110)

        txt_widget_tabla = tk.Text(window, height=10, width=30, bg="#77dd77", padx=10, pady=10)
        txt_widget_tabla.place(x=700, y=140, width=620, height=190)

        # Insertar la cadena de texto en el widget Text
        txt_widget_tabla.insert(tk.END, data_str)
        txt_widget_tabla.configure(borderwidth=1, relief="solid", state=tk.DISABLED)

        # =============================================================================
        # ============= MODELOS DE AJUSTES ============================================
        # =============================================================================

        # body frame 2
        bodyFrame2 = Frame(window, bg='#ff94a2', padx=10, pady=10)
        bodyFrame2.place(x=700, y=370, width=620, height=150)

        Title_models = Label(bodyFrame2, text="Modelos de ajustes", bg='#ff94a2', font=("", 12, "bold"), fg='black')
        Title_models.place(x=5, y=5)

        Lbl_models = Label(bodyFrame2, bg='#ff94a2', fg='black', padx=10, pady=10)
        Lbl_models.config(text="Modelo lineal: y = {:.6f} + {:.6f}x\nModelo exponencial: y = {:.6f}e^({:.6f}x)\nModelo logaritmico: y = {:.6f} + {:.6f} Ln(x)\nModelo potencial: y = {:.6f}x^{:.6f}\nModelo hiperbolico: y = {:.6f} + ( {:.6f} / x )".format(a_lineal, b_lineal, a_exp, b_exp, a_log, b_log, a_pot, b_pot, a_hiper, b_hiper))

        Lbl_models.place(x=5, y=30)        
        
        # =============================================================================
        # ============= COEFICIENTES R Y R^2 ===========================================
        # =============================================================================

        # body frame 3
        bodyFrame3 = Frame(window, bg='#84b6f4', padx=10, pady=10)
        bodyFrame3.place(x=700, y=550, width=620, height=150)

        # Body Frame 3
        title_correlation_coefficients = Label(bodyFrame3, text="Coeficientes r y r^2", bg='#84b6f4', font=("", 12, "bold"), fg='black')
        title_correlation_coefficients.place(x=5, y=5)

        Lbl_coefficients = Label(bodyFrame3, bg='#84b6f4', fg='black', padx=10, pady=10)
        Lbl_coefficients.config(text="Modelo lineal: R = {:.6f} y R^2 = {:.6f}\nModelo exponencial: R = {:.6f} y R^2 = {:.6f}\nModelo logaritmico: R = {:.6f} y R^2 = {:.6f}\nModelo potencial: R = {:.6f} y R^2 = {:.6f}\nModelo hiperbolico: R = {:.6f} y R^2 = {:.6f}"
                                .format(coeficiente_corr_lineal, coeficiente_det_lineal, 
                                        coeficiente_corr_exp, coeficiente_det_exp,
                                        coeficiente_corr_log, coeficiente_det_log,
                                        coeficiente_corr_pot, coeficiente_det_pot,
                                        coeficiente_corr_hip, coeficiente_det_hip))
        Lbl_coefficients.place(x=5, y=30)     

        window.mainloop()

    def crearTabla(x,y,y_lin,y_exp,y_log,y_pot,y_hip):
        tabla = {
                'x': x, 
                'y': y, 
                'lineal': y_lin,
                'exponencial': y_exp,
                'logaritmica': y_log,
                'potencial': y_pot,
                'hiperbolico': y_hip,
             }

        return pd.DataFrame(tabla)