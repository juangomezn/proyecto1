from Modulos.calculadora import *

while True:
    print("Sistema Calculadora \n \n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Division")
    print("5. Potenciacion")
    print("0. Salir")
    opc = input(" ---> Elija una opcion: ")

    if opc == "0":
        break

    if opc == "1":
        n1 = int(input("Primer Numero: "))
        n2 = int(input("Segundo Numero: "))
        print(f"\nLa suma de los numeros es {suma(n1,n2)}")

    if opc == "2":
        n1 = int(input("Primer Numero: "))
        n2 = int(input("Segundo Numero: "))
        print(f"\nLa resta de los numeros es {resta(n1,n2)}")

    if opc == "3":
        n1 = int(input("Primer Numero: "))
        n2 = int(input("Segundo Numero: "))
        print(f"\nLa Multiplicacion de los numeros es {multiplicacion(n1,n2)}")

    if opc == "4":
        n1 = int(input("Primer Numero: "))
        n2 = int(input("Segundo Numero: "))
        print(f"\nLa division de los numeros es {division(n1,n2)}")

    if opc == "5":
        n1 = int(input("Ingrese el numero que desea potenciar: "))
        n2 = int(input("Ingrese a que potencia desea el elevar el numero ingresado: "))
        print(f"\nLa potencia de los numeros es {potenciacion(n1,n2)}")
