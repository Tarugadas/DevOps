#17/03/2026
I = int(input("Bienvenido a la calculadora MLR\nSelecciona una operacion\nMatematicas(1)\nLogica(2)\nRelacionales(3)\n"))

#Matematicas
if I == 1:
    M = int(input("Selecciona una operacion matematica\nSuma(1)\nResta(2)\nMultiplicacion(3)\nDivision(4)\nExponencial(5)\n"))
    if M == 1:
        Sm1 = int(input("Escogiste Suma, introduza los dos numeros:\nNumero 1:"))
        Sm2 = int(input("Numero 2:"))
        print ("La resta de los numeros", Sm1, "y", Sm2, "da igual a", (Sm1 + Sm2))
    elif M == 2:
        Rt1 = int(input("Escogiste Resta, introduza los dos numeros:\nNumero 1:"))
        Rt2 = int(input("Numero 2:"))
        print ("La resta de los numeros", Rt1, "y", Rt2, "da igual a", (Rt1 - Rt2))
    elif M == 3:
        Mp1 = int(input("Escogiste Multiplicacion, introduza los dos numeros:\nNumero 1:"))
        Mp2 = int(input("Numero 2:"))
        print ("La multiplicacion de los numeros", Mp1, "y", Mp2, "da igual a", (Mp1 * Mp2))
    elif M == 4:
        Dv1 = int(input("Escogiste Division, introduza los dos numeros:\nNumero 1:"))
        Dv2 = int(input("Numero 2:"))
        print ("La division de los numeros", Dv1, "y", Dv2, "da igual a", (Dv1 / Dv2))
    elif M == 5:
        Ex1 = int(input("Escogiste Exponencial, introduza los dos numeros:\nNumero:"))
        Ex2 = int(input("Exponencial:"))
        print ("La exponencial", Ex1,"^",Ex2, "da igual a", (Ex1 ** Ex2))

#Logica
elif I == 2:
    L = int(input("Selecciona una operacion logica\nAnd(1)\nOr(2)\nNot(3)\n"))
    if L == 1:
        A1 = int(input("Escogiste And, aqui la tabla de logica:\n| A | B | S |\n| 0 | 0 | 0 |\n| 1 | 0 | 0 |\n| 0 | 1 | 0 |\n| 1 | 1 | 1 |\n introduza los dos datos (0/1):\nDato 1:"))
        A2 = int(input("Dato 2:"))
        print ("Aqui tu problema de logica\n| A | B | S |\n|",A1,"|",A2,"|",(A1 and A2),"|")
    elif L == 2:
        O1 = int(input("Escogiste Or, aqui la tabla de logica:\n| A | B | S |\n| 0 | 0 | 0 |\n| 1 | 0 | 1 |\n| 0 | 1 | 1 |\n| 1 | 1 | 1 |\n introduza los dos datos (0/1):\nDato 1:"))
        O2 = int(input("Dato 2:"))
        print ("Aqui tu problema de logica\n| A | B | S |\n|",O1,"|",O2,"|",(O1 or O2),"|")
    elif L == 3:
        N1 = int(input("Escogiste Not, aqui la tabla de logica:\n| A | S |\n| 0 | 1 |\n| 1 | 0 |\n introduza el dato (0/1):\nDato 1:"))
        print ("Aqui tu problema de logica\n| A | S |\n|",N1,"|",(not N1),"|")

#Recional
elif I == 3:
    R = int(input("Selecciona una operacion racional\nIgual a(1)\nMayor que(2)\nMenor que(3)\nMayor igual(4)\nMenor igual(5)\nDiferente a(6)\n"))
    if R == 1:
        G1 = int(input("Escogiste Igual a, introduza los dos numeros:\nNumero 1:"))
        G2 = int(input("Numero 2:"))
        print ("La igualdad de los numeros", G1, "y", G2, "es", (G1 == G2))
    elif R == 2:
        M1 = int(input("Escogiste Mayor que, introduza los dos numeros:\nNumero 1:"))
        M2 = int(input("Numero 2:"))
        print ("La relacion", M1, ">", M2, "es", (M1 > M2))
    elif R == 3:
        Me1 = int(input("Escogiste Menor que, introduza los dos numeros:\nNumero 1:"))
        Me2 = int(input("Numero 2:"))
        print ("La relacion", Me1, "<", Me2, "es", (Me1 < Me2))
    elif R == 4:
        Mi1 = int(input("Escogiste Mayor igual, introduza los dos numeros:\nNumero 1:"))
        Mi2 = int(input("Numero 2:"))
        print ("La relacion", Mi1, ">=", Mi2, "es", (Mi1 >= Mi2))
    elif R == 5:
        Mei1 = int(input("Escogiste Menor igual, introduza los dos numeros:\nNumero 1:"))
        Mei2 = int(input("Numero 2:"))
        print ("La relacion", Mei1, "<=", Mei2, "es", (Mei1 <= Mei2))
    elif R == 6:
        D1 = int(input("Escogiste Diferente a, introduza los dos numeros:\nNumero 1:"))
        D2 = int(input("Numero 2:"))
        print ("La relacion", D1, "!=", D2, "es", (D1 != D2))
