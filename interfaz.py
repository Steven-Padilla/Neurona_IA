import tkinter as tk

class Interfaz():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x400")
        self.window.eval("tk::PlaceWindow . center")
        self.window.title('Algoritmo genetico')
        self.window.columnconfigure(0, weight=1)

        self.label1=tk.Label(self.window,text="Ingrese el valor de aprendizaje:")
        self.label1.grid(column=0, row=0)
        self.aprendizaje=tk.DoubleVar()

        self.entry1=tk.Entry(self.window, width=20, textvariable=self.aprendizaje )
        self.entry1.grid(column=0, row=1)
        
        
        self.label2=tk.Label(self.window,text="Ingrese el margen de error:")
        self.label2.grid(column=0, row=2)
        self.e_margen=tk.DoubleVar()

        self.entry2=tk.Entry(self.window, width=20, textvariable=self.e_margen )
        self.entry2.grid(column=0, row=3)

        self.boton=tk.Button(self.window, text="Aceptar",command=self.aplicar_datos)
        self.boton.grid(column=0, row=4)

        self.window.mainloop()

    def aplicar_datos(self):
        self.window.destroy()
    def get_datos(self):
        return {'aprendizaje':self.aprendizaje.get(),'margen_error': self.e_margen.get()}


