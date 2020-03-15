def fooBar(n):

    for k in range (1,n+1):

        if (k%3==0) and (k%5==0):

            print("FizzBuzz")

        elif (k%3==0) and (k%5!=0):

            print("Fizz")

        elif (k%3!=0) and (k%5==0):

            print("Buzz")

        else:

            print(k)

    preguntaOtroNumero()

def ejecucionFoobar():

    n = int(input ("Introduzca el número hasta el que quiera obtener el Fizzbuzz: "))

    fooBar(n)

def preguntaOtroNumero():

    q = input("\n¿Quiere obtenter el Fizzbuzz de otro número?\n")

    if q == "Sí":

        ejecucionFoobar()

    elif q == "No":

        print ("\nEl programa ha finalizado.")

    else:

        print ("Responda correctamente escribiendo Sí o No.")
        
        preguntaOtroNumero()

ejecucionFoobar()