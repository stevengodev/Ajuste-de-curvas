import numpy as np

#Devuelve el valor de b y a respectivamente
def ajuste_lineal(x, y):
    #Funcion: a + bx
    b, a = np.polyfit(x, y, 1)                  #Sirve para ajustar una línea recta a los datos (1 es el grado)
    return b, a

#Devuelve el valor de b y a respectivamente
def ajuste_potencial(x,y):
    n = len(x)                                  #tamaño

    log_x = np.log10(x)                         #logaritmos de x
    log_x2 = log_x * log_x                      #logaritmos de x elevados al cuadrado    
    sum_log_x2 = np.sum(log_x2)                 #Suma de los logaritmos de x al cuadrado
    sum_log_x = np.sum(log_x)                   #suma de los logaritmos de x

    log_y = np.log10(y)                         #logaritmos de y
    sum_log_y = np.sum(log_y)                   #suma de los logaritmos de y

    mul_log_xy = np.multiply(log_x, log_y)      #producto de logaritmos de x e y
    sum_mul_log_xy = np.sum(mul_log_xy)         #Suma del producto de los logaritmos

    b = ((n*sum_mul_log_xy)-(sum_log_x*sum_log_y))/((n * sum_log_x2)-(sum_log_x**2))
    _a = (sum_log_y / n) - b * (sum_log_x/ n)
    a = 10**_a
    return b, a