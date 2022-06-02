#Declaramos una variables
calificacion = input("Introduce tu calificación de la AZ-900: ")
calificacion = int(calificacion)
# Preguntamos si la calificación es menor que 700
if calificacion < 700 :
    print("Ves, por ver nesflis")  # Si la calificación es menor que 700, muestra esto.
elif calificacion > 1000 :
    print("Ay si tu, no se puede sacar más de 1000")
else :  # si no se cumple el if anterior, pasa esta linea
    print("Felicidades, pasa por tu certificado!") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad)
if edad >= 18 and edad <=100 :
    print("Bienvenido, pasele marchante")
elif edad > 100 :
    print("Tienes un descuento del 90% si vienes con tu abuelito")
elif edad < 0 :
    print("Achis, achis los mariachis")
else :
    print("Regresa en unos años")





