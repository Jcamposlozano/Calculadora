
class Calculadora:

    def oparacion(self, a:float, b:float, entrada:str):
        if entrada == '+':
            return self.suma(a,b) 
        if entrada == '-':
            return self.resta(a,b)
        if entrada == '*':
            return self.multiplicacion(a,b)
        if entrada == '/':
            return self.divicion(a,b)
        else:
            return 'Error'        

    def suma(self, a:float, b:float): 
        resultado = a + b
        return (resultado)

    def resta(self, a:float, b:float): 
        resultado = a - b
        return (resultado)

    def multiplicacion(self, a:float, b:float): 
        resultado = a * b
        return (resultado)

    def divicion(self, a:float, b:float): 
        if b != 0:
            resultado = a / b
            return (resultado)
        else:
            return 0
