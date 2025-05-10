#print ("¿Cual es tu nombre?")
#nombre = input ()
print ("¿Cual es tu peso en Kg?")
peso = float(input ())
print ("¿Cual es tu estatura en Metros?")
estatura = float(input ())

imc = peso / (estatura * estatura)
print ("Tu Indice de Masa Corporal es de: ", round(imc, 2))
#print (nombre,"tu peso es de ", peso , "Kg")

if imc < 18.5:
    print ("Estas flaco, come más")
elif imc < 25:
    print ("Estas en buen peso")
elif imc < 29.9:
    print ("Tienes sobrepeso, mídete")
elif imc < 39.99:
    print ("Estas en obecidad, bajale que ya estás teniendo consecuencias")
elif imc > 40:
    print ("Eres un obeso mórbido, esto es grave")
'''
print ("Menos de 18,5 está por debajo de lo normal y tienen un peso insuficiente.")
print ("Entre 18,5 y 24,9 peso normal y saludable.")
print ("Entre 25 y 29,9 nos encontramos en situación de sobrepeso.")
print ("Entre 30 y 39,99 estamos en situación de obesidad.")
print ("De 40 en adelante, indica obesidad tipo 3 conocida como obesidad mórbida o extrema.\n")

'''

print ("\nVe algunas referencias.\nMenos de 18,5 está por debajo de lo normal y tienen un peso insuficiente. \nEntre 18,5 y 24,9 peso normal y saludable.\nEntre 25 y 29,9 nos encontramos en situación de sobrepeso. \nEntre 30 y 39,99 estamos en situación de obesidad. \nDe 40 en adelante, indica obesidad tipo 3 conocida como obesidad mórbida o extrema.")

