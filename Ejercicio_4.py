#18/03/2026
print ("Hola, quieres contarme sobre ti")
A= "Y"
B= "N"
input()
if "Y":
    n= str(input("Cual es tu nombre? "))
    e= int(input("Cual es tu edad? "))
    pt= str(input("Que te gusta hacer en tu tiempo libre? "))
    c= str(input("Cual es tu comida favorita? "))
    a= str(input("Te interesa aprender algo nuevo "))
    print ("Hola " + n ,"Tu edad es:", e , "Lo que te gusta hacer en tu tiempo libre es " + pt, "\nTu comida favorita es " + c, "Algo que quieres aprender es " + a)
elif "N":
    print ("Hasta pronto")
