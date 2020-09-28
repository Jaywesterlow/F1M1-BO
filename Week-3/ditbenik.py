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
  print("Dat is goed! Ik ben 18 jaar oud. Volgende vraag!")
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


antwoord_2 = input()
if antwoord_2.lower() == "a" or antwoord_2.lower() == "amsterdam":
  time.sleep(1)
  print("Nee-Heej... ik had geen zin meer om lang na te denken over een antwoord. Laatste vraag")
elif antwoord_2.lower() == "b" or antwoord_2.lower() == "amersfoort":
  time.sleep(1)
  print("Nee-Heej... ik had geen zin meer om lang na te denken over een antwoord. Laatste vraag")
elif antwoord_2.lower() == "c" or antwoord_2.lower() == "almere":
  time.sleep(1)
  print("Dat is helemaal waar, laatste vraag!")
  x = x + 1
else:
  time.sleep(1)
  print("Uhhm... Volgende vraag dan maar?")
time.sleep(2)

print("Laatste vraag " + naam + ", welke van deze is hobby van mij?")
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
  print("Ik had wat meer goeie antwoorden verwacht...")
  

time.sleep(3)


