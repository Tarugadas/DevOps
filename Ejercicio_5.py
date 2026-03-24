#19/03/2026
Materias = ("Fundamentos", "Ingles", "Full Stack", "Computacion en la Nube", "Gestion de Redes")
print ("Escribe tus calificaciones: ")
Calificaciones = int(input("")),int(input("")),int(input("")),int(input("")),int(input(""))

print ("Quieres calcular tu promedio?")
input ()
if "Y" in input().upper():
    Calificaciones = [int(c) for c in Calificaciones]

    print("Estas son tus materias:")
    print(list(Materias))
    print("Sus respectivas calificaciones")
    print(Calificaciones)

    suma= sum(Calificaciones)
    promedio= suma / len(Calificaciones)

    print("La suma de tus calificaciones es:")
    print(suma)

    print("Este es tu promedio:")
    print(promedio)

    if promedio == 10:
        print("Excelente promedio")
    elif promedio >= 7:
        print("Tu promedio es aceptable")
    elif promedio == 6:
        print("Podrias mejorar")
    elif promedio <= 5:
        print("Deberias esforzarte mas")
    elif promedio == 0:
        print("Muy mal espero mejores")

elif "N" in input().upper():
    print("Hasta pronto")
