def suma(a,b):
    return a+b
    
def resta(a,b):
    return a-b

#multiplicacion

#division

while True:
    print("Menu calculator")

    print("1, suma")
    print("2, resta")
    #multiplicacion

    #division
    print("3, salir")

    usuario = input("")

    match usuario:
        case "1":
            print("suma")
            n1 = int(input("inserte el primer numero: "))
            n2 = int(input("inserte el segundo numero: "))

            print(f"la suma de {n1} + {n2} es = {suma(n1,n2)}")

        case "2":
            print("resta")
            n1 = int(input("insete el primer numero: "))
            n2 = int(input("inserte el segundo numero: "))

            print(f"la resta de {n1} - {n2} es = {suma(n1,n2)}")

        case "3":
            print("Bye")
            break

        case _:
            print("No es una opcion valida")
