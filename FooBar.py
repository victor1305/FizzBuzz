def fizzbuzz(n):

    for k in range (0,n+1):

        nombre = ""

        if (k%3==0) and (k%5==0):

            nombre = "FizzBuzz"

        elif (k%3==0) and (k%5!=0):

            nombre = "Fizz"

        elif (k%3!=0) and (k%5==0):

            nombre = "Buzz"

        else:

            nombre = k

        print (nombre)

    preguntaOtroNumero()

def ejecucionFizzbuzz():

    n = int(input ("Introduzca el número hasta el que quiera obtener el Fizzbuzz: "))

    fizzbuzz(n)

def preguntaOtroNumero():

    q = input("\n¿Quiere obtenter el Fizzbuzz de otro número?\n")

    if q == "Sí":

        ejecucionFizzbuzz()

    elif q == "No":

        print ("\nEl programa ha finalizado.")

    else:

        print ("Responda correctamente escribiendo Sí o No.")
        
        preguntaOtroNumero()

ejecucionFizzbuzz()