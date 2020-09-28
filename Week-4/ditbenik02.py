import time

x = 0

print('Hello You! ik ben Jaymar.')
time.sleep(1)

print("Wie ben jij?")
naam = input()
time.sleep(1)

print("Hallo " + naam + ", kan je raden hoe oud ik ben?")
print("a). 16")
print("b). 18")
print("c). 20")
time.sleep(1)

antwoord_1 = input()
if antwoord_1.lower() == "b" or antwoord_1.lower() == "18":
  time.sleep(1)
  print("Dat is goed, volgende vraag!")
  x = x + 1
elif antwoord_1.lower() == "a" or antwoord_1.lower() == "16":
  time.sleep(1)
  print("Dat is net niet goed, iets hoger. Ik ben namelijk 18, volgende vraag!")
elif antwoord_1.lower() == "c" or antwoord_1.lower() == "20":
  time.sleep(1)
  print("Dat is net niet goed, iets lager. Ik ben namelijk 18, volgende vraag!")
else:
  time.sleep(1)
  print("Gaat het wel goed met je? Laat maar, volgende vraag.")
time.sleep(2)

print("Oké " + naam + ", waar denk je dat ik woon?")
print("a). Amsterdam")
print("b). Amersfoort")
print("c). Almere")
time.sleep(1)


split = 0


while split < 1:
  antwoord_2 = input()
  if antwoord_2.lower() == "a" or antwoord_2.lower() == "amsterdam":
    time.sleep(1)
    split = split + 1
    print("Dat is niet goed, ik woon namelijk in Almere. Hoewel ik wel eens in de 2 weken naar mijn vader in amsterdam ga,")
    time.sleep(1)
  elif antwoord_2.lower() == "b" or antwoord_2.lower() == "amersfoort":
    time.sleep(1)
    print("Dat is niet goed, probeer maar opnieuw.")
  elif antwoord_2.lower() == "c" or antwoord_2.lower() == "almere":
    time.sleep(1)
    print("Dat is helemaal waar, laatste vraag!")
    x = x + 1
    split = split + 2
  else:
    time.sleep(1)
    print("Uhhm... probeer maar opnieuw.")
time.sleep(2)



if split == 1:
  print("Laatste vraag, waar in amsterdam denk je dat ik dan heen ga?")
  print("a). Amsterdam Noord")
  print("b). Amsterdam West")
  print("c). Amsterdam Zuid-oost")
  time.sleep(1)

  antwoord_4 = input()
  if antwoord_4.lower() == "a" or antwoord_4.lower() == "amsterdam noord":
    time.sleep(1)
    print("Dat is goed, Punt erbij!")
    x = x + 1
  elif antwoord_4.lower() == "b" or antwoord_4.lower() == "amsterdam west":
    time.sleep(1)
    print("Dat is niet goed, ik ga naar Amsterdam Noord")
  elif antwoord_4.lower() == "c" or antwoord_4.lower() == "amsterdam zuid-oost":
    time.sleep(1)
    print("Dat is niet goed, ik ga naar Amsterdam Noord")
  else:
    time.sleep(1)
    print("Nou, uhhm... ")
    time.sleep(3)
    print("ooookeeej...")
  time.sleep(2)


  
else:
  print("Laatste vraag " + naam + ", welke van deze 3 opties is een hobby van mij?")
  print("a). Piano spelen")
  print("b). Gamen")
  print("c). Vechtsport")
  time.sleep(1)

 
  
  antwoord_3 = input()
  if antwoord_3.lower() == "a" or antwoord_3.lower() == "piano spelen":
    time.sleep(1)
    print("Dat is goed! Ze waren eigenlijk alle 3 goed maar toch een punt erbij!")
    x = x + 1
  elif antwoord_3.lower() == "b" or antwoord_3.lower() == "gamen":
    time.sleep(1)
    print("Dat is goed! Ze waren eigenlijk alle 3 goed maar toch een punt erbij!")
    x = x + 1
  elif antwoord_3.lower() == "c" or antwoord_3.lower() == "vechtsport":
    time.sleep(1)
    print("Dat is goed! Ze waren eigenlijk alle 3 goed maar toch een punt erbij!")
    x = x + 1
  else:
    time.sleep(1)
    print("Nou, uhhm... ")
    time.sleep(3)
    print("ooookeeej...")
  time.sleep(2)

if x == 3:
  print("Je had alles goed! Goed gedaan.")
else:
  print("Dat waren de vragen die ik voor je had!")
  

time.sleep(3)


