from tkinter import *
from Calculadora import *

class Form:

    def __init__(self):
        self.root = Tk()
        self.calculadora = Calculadora()
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.resultado = StringVar()


        self.formulario()

    def sumar(self):
        self.resultado.set(self.calculadora.suma( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()

    def restar(self):
        self.resultado.set(self.calculadora.resta( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()

    def multiplicar(self):
        self.resultado.set(self.calculadora.multiplicacion( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()

    def dividir(self):
        self.resultado.set(self.calculadora.divicion( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()

    def borrar(self):
        self.n1.set("")
        self.n2.set("")

    def formulario(self):
        self.root.config(bd=20)

        Label(self.root, text="NUMERO 1").pack()
        Entry(self.root, textvariable = self.n1 ).pack()

        Label(self.root, text="NUMERO 2").pack()
        Entry(self.root, textvariable = self.n2 ).pack()

        Label(self.root, text="RESULTADO").pack()
        Entry(self.root, textvariable = self.resultado, state="disabled" ).pack()

        Button(self.root, text="+", command = self.sumar).pack(side="left")
        Button(self.root, text="-", command = self.restar).pack(side="left")
        Button(self.root, text="*", command = self.multiplicar).pack(side="left")
        Button(self.root, text="/", command = self.dividir).pack(side="left")


        self.root.mainloop()




