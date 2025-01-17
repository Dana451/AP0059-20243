import clase

object1 = clase.Square(None)


object2 = clase.add_sub(None, None, None, None)
r = "1"
print("\n")
print("****CALCULADORA****\n")

while r == "1":
    
    print("---------------------------------------------------------------------\n")
    
    print("Agregue la altura del cuadrado:\n")

    c = int(input("h = "))
    print("\n")

    object1.getval(c)
    object1.ResultadoArea()
    print("\n")
    print("Agregue los valores de los datos:\n")

    # Capturamos las variables a sumar
    a = int(input("Escriba el valor de (a): "))
    b = int(input("Escriba el valor de (b): "))
    print("\n")

    # Llamamos a los métodos add y sub con las variables capturadas
    object2.add(a, b)
    object2.sub(a, b)
    object2.div(a, b)
    object2.mul(a, b)

    # Mostramos los resultados
    object2.imprimirResultado(a, b)
    print("\n")
    
    r = input("Si quiere seguir calculando valores escriba 1: ")
    print("\n")
