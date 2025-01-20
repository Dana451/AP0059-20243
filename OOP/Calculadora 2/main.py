import operaciones


object2 = operaciones.add_sub(None, None, None, None)
r = "1"
print("\n")
print("****CALCULADORA****\n")

while r == "1":
    
    print("---------------------------------------------------------------------\n")
    print("Agregue los datos:\n")

    a = int(input("Escriba el valor de (a): "))
    b = int(input("Escriba el valor de (b): "))
    print("\n")

    y = input("Escriba el signo de la operación que quiere realizar:")
    print("\n")
    
    object2.add(y, a, b)
    object2.sub(y, a, b)
    object2.div(y, a, b)
    object2.mul(y, a, b)

    # Mostramos los resultados
    object2.imprimirResultado(a, b)
    print("\n")
    
    r = input("Si quiere seguir calculando valores escriba 1: ")
    print("\n")
