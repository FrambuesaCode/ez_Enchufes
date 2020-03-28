#Coded By La Frambuesa Code. Ez Codes.
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
enchufes = [3,4] #Tus GPIOS
minutoEmpieza = time.strftime("%M:%S")

def usar(pin, k):
   if k == "out":
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
   if k == "in" or k == None:
      GPIO.setup(pin, GPIO.IN)


def tiempo():
  tiempoDuracion = input("Tiempo de duracion?(seg): ")
  activador = True
  calculo1 = int(minutoEmpieza.split(":")[1]) + tiempoDuracion
  minuto = minutoEmpieza.split(":")[0]
  fin = []
  if calculo1 >= 60:
     segLimpio = calculo1 - 60
     minutoLimpio = int(minuto) + 1
     if segLimpio < 10:
        lol = "0" + str(segLimpio)
        fin.append(str(minutoLimpio)+":"+lol)
     else:
        fin.append(str(minutoLimpio)+":"+str(segLimpio))
  else:
     if calculo1 < 10:
       lol = "0" + str(calculo1)
       calculo1 = int(lol)
     fin.append(minuto+":"+str(calculo1))
  print(fin)
  cont1 = 0
  while activador:
     hora = time.strftime("%M:%S")
     if hora > fin[0]:
        print("el acabose")
        activador = False
        quitarT()
     else:
        if cont1 < 1:
          for x in enchufes:
             usar(x,"out")
        cont1 += 1

  else:
     for x in enchufes:
        usar(x, "in")


def quitarT():
  for x in enchufes:
     usar(x,None)

def kill():
    quitarT()
    quit()

if __name__ == '__main__':
    try:
        tiempo()
    except KeyboardInterrupt:
        kill()
