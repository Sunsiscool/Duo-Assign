def suma(a,b):
    return a+b
    
def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b


while True:
    print("Menu calculator")

    print("1, suma")
    print("2, resta")
    print("3, multiplicacion")
    print("4, division")
   
    print("5, salir")

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

            print(f"la resta de {n1} - {n2} es = {resta(n1,n2)}")

        case "3":
            print("multiplicacion")
            n1 = int(input("insete el primer numero: "))
            n2 = int(input("inserte el segundo numero: "))

            print(f"la multiplicacion de {n1} * {n2} es = {multiplicacion(n1,n2)}")

        case "4":
            print("division")
            n1 = int(input("insete el primer numero: "))
            n2 = int(input("inserte el segundo numero: "))

            if n2 == 0:
                print("no se puede hacer una division entre 0")
            else:
                print(f"la division de {n1} / {n2} es = {division(n1,n2)}")
            
        case "5":
            print ("bye")
            break 

