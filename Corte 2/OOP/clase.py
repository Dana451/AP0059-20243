class Square:
    def __init__(self, val):
        self.val = None
        
    def getval(self, c):
        self.val = c * c
        return self.val
    
    def ResultadoArea (self):
        print(f"El área del cuadrado es: {self.val}")

class add_sub:
    def __init__(self, r, d, y, j):
        self.r = None
        self.d = None
        self.y = None
        self.j = None
    
    def add(self, a, b):
        self.r = a + b  # Guardamos el resultado de la suma en self.r
        return self.r

    def sub(self, a, b):
        self.d = a - b  # Guardamos el resultado de la resta en self.d
        return self.d
    
    def mul(self, a, b):
        self.y = a * b
        return self.y
    
    def div(self, a, b):
        if b != 0:
            self.j = a / b
        else:
            self.j = "- No se puede dividir entre cero."
        return self.j

    def imprimirResultado(self, a, b):
        print(f"- Resultado de la suma entre ({a} + {b}) es: {self.r}")
        print(f"- Resultado de la resta entre ({a} - {b}) es: {self.d}")
        print(f"- Resultado de la multipicación entre ({a} * {b}) es: {self.y}")
        if not isinstance(self.j, str):  # Verifica si self.j no es un string
            print(f"- Resultado de la división entre ({a} / {b}) es: {self.j}")
        else:
            print(f"{self.j}")
                    
