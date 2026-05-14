import os, time
os.system("cls")

acceso = True
acumulador_depositos = 0
deposito = 0
cantidad_depositos = 0
tab_credito = 0
contador_cliente = 0

while acceso:
    print("    Menú del Sistema")
    print("========= BANCO FINANCIERO =========")
    print("1. Mostrar cuotas de ahorro")
    print("2. Simular depósito acumulado")
    print("3. Tabla de crédito")
    print("4. Contar clientes atendidos")
    print("5. Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            print("1. Mostrar cuotas de ahorro")
            monto = 0
            meses = 0
            while monto <= 0:
                monto = int(input("Ingrese ahorro mensual: \n"))
                if monto <= 0:
                    print("el monto debe ser superior a 0")
            while meses <= 0:
                meses = int(input("Ingrese cantidad de meses\n"))
                if meses <= 0:
                    print("la cantidad debe ser superior a 0")
            #aca puedo seguir trabajando
            for x in range(1, meses + 1):
                ahorro_por_mes = monto * x
                print(f"Mes {x}: ${ahorro_por_mes}")
            time.sleep(2)
            contador_cliente = contador_cliente +1
        elif opcion == 2:
            print("2. Simular depósito acumulado")
            while deposito >= 0:
                deposito = int(input("Ingrese depósito:\n"))
                acumulador_depositos = acumulador_depositos + deposito
                cantidad_depositos = cantidad_depositos + 1
                if deposito <= 0:
                    cantidad_depositos = cantidad_depositos - 1
                    break
            print(f"Total acumulado en deposito: ${acumulador_depositos}")
            print(f"Cantidad de depositos: {cantidad_depositos}")
            time.sleep(2)
            contador_cliente = contador_cliente +1
        elif opcion == 3:
            print("3. Tabla de crédito")
            while tab_credito == 0:
                tab_credito = int(input("Ingrese monto del credito: \n"))
                if tab_credito <= 0:
                    print("Monto debe ser superior a 0")
            for x in range(1, 13):
                resultado_cred = tab_credito * x
                print(f"{tab_credito} x {x}: $ {resultado_cred}")
            time.sleep(4)
            contador_cliente = contador_cliente +1
        elif opcion == 4:
            print("4. Contar clientes atendidos")
            if contador_cliente == 0:
                print("No se ha atendido a ningun cliente")
            else:
                for x in range(contador_cliente):
                    print(f"Cliente atendido N°{x+1}")
            time.sleep(2)
        elif opcion == 5:
            print("Gracias por utilizar el sistema financiero")
            acceso = False
        else:
            print("Opción no válida")
    except:
        print("el valor debe ser numerico")