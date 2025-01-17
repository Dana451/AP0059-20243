class add_sub:
    def __init__(self, r, d, y, j):
        self.r = None
        self.d = None
        self.y = None
        self.j = None
    
    def add(self, y, a, b):
        if y == "+":
            self.r = a + b  # Guardamos el resultado de la suma en self.r
            return self.r
        else:
            self.r = None
            return self.r

    def sub(self, y, a, b):
        if y == "-":
            self.d = a - b  # Guardamos el resultado de la suma en self.r
            return self.d
        else:
            self.d = None
            return self.r
    
    def mul(self, y, a, b):
        if y == "*":
            self.y = a * b  # Guardamos el resultado de la suma en self.r
            return self.y
        else:
            self.y = None
            return self.y
    
    def div(self, y, a, b):
        if y == "/":
            if b != 0:
                self.j = a / b
            else:
                self.j = "- No se puede dividir entre cero."
            return self.j
        else:
            self.j = None
            return self.j


    def imprimirResultado(self, a, b):
        
        if self.r is not None:
            print(f"- Resultado de la suma entre ({a} + {b}) es: {self.r}")
        else:
            if self.d is not None:
                print(f"- Resultado de la resta entre ({a} - {b}) es: {self.d}")
            else:
                if self.y is not None:
                    print(f"- Resultado de la multipicación entre ({a} * {b}) es: {self.y}")
                else:
                    if self.j is not None:
                        if not isinstance(self.j, str):  # Verifica si self.j no es un string
                            print(f"- Resultado de la división entre ({a} / {b}) es: {self.j}")
                        else:
                            print(f"{self.j}")
                    else:
                        print("No ha escrito bien la operación que desea realizar.")
                    
    
