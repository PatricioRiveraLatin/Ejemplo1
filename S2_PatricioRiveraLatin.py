import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.config(width=400, height=200)
root.title("Cálculo de Edad Futura")

# Variables para las cajas de texto
nombre_var_prl = tk.StringVar()  # Variable para el nombre
edad_var_prl = tk.StringVar()    # Variable para la edad

#Titulo
titulo_general = ttk.Label(root, text="Calcular edad dentro de una década", font=(10))
titulo_general.place(x=45, y=10)

# Caja Nombre
label_nombre = ttk.Label(root, text="Ingrese su Nombre:")
label_nombre.place(x=50, y=50)
entry1 = ttk.Entry(root, textvariable=nombre_var_prl)  # Asociar la variable
entry1.place(x=50, y=70)

# Caja Edad
label_edad = ttk.Label(root, text="Ingrese su Edad:")
label_edad.place(x=50, y=100)
entry2 = ttk.Entry(root, textvariable=edad_var_prl)  # Asociar la variable
entry2.place(x=50, y=120)

# Función para el botón
def funcion_calcular_resultado():
    nombre = nombre_var_prl.get().strip()  # Obtener y limpiar el nombre
    edad = edad_var_prl.get().strip()      # Obtener y limpiar la edad

    # Validar campos
    if not nombre or not edad:
        print("Por favor, completa ambos campos.")
        return

    if not edad.isdigit():  # Validar que la edad sea un número
        print("Error: La edad debe ser un número válido.")
        return

    edad = int(edad)  # Convertir edad a entero
    decada = 10
    resultado = edad + decada

    # Mostrar resultado en consola
    print("La edad que tendrá", nombre, "dentro de una década será", resultado, "años.")

# Botón
button = ttk.Button(root, text="Calcular Resultado", command=funcion_calcular_resultado)
button.place(x=50, y=150)

# Ejecutar la ventana
root.mainloop()