import random

print("welcome to the game 'guess the number'")

print("choose the start and end range")
#Para poder inicializar el while, se necesita que se cumpla una condicion 
#"Count" toma el valor de s
count = "s"
#count al valer igual a "s" hara que se cumpla la condicion, e inicializara el bucle
while count == "s":

   a = int(input("Star number "))
   b = int(input("end number "))
   #la variable "aleatorio" obtendra los valores que se le asignan al metodo random
   aleatorio = random.randint(a,b)
   #Se imprime el valor aleatorio, solo para la comprobacion que se hara mas adelante
   print(aleatorio)
   
   adivina = int(input("type number "))
   #Si el numero que introducimos es igual que el valor dado aleatoriamente entonces se a ganado el juego
   #Recordemos que se a imprimido el valor aleatorio 
   #para poder comprobar lo que ocurre si se cumple la condicion
   if adivina == aleatorio:
      print("congratulations")
      #si se cumple la condicion nos preguntara si queremos volver a jugar
      #count obtendra el valor, si es "s" se volvera a repetir el blucle del inicio
      count = input("Do you want to repeat? Writing a s")
   else:
      #Si no se cumple la condición, preguntara si se quiere volver a jugar
      #count obtendra el valor, si es "s" se volvera a repetir el blucle del inicio
      count = input("Do you want to repeat? Writing a s")
