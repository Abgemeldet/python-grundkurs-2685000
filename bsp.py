#!/usr/bin/env python3
#input
a = float(input("Sag zahl du Huso: "))
b = float(input("nochmal: "))
#output
print(
  f"Die Summe ist: {a+b}\n"
  f"Die Differenz ist: {a-b} oder {b-a}\n"
  f"Das Produkt ist: {a*b}"
  )
#input_danke
antwort = input("Sag Danke: ")
#final_response
if antwort == "Danke":
  print("Bessser isses")
elif antwort == "danke":
  print("Schreibt man gross aber ok")
else: 
  print("Fick dich, fick sich und deine Mudda du Hurensohn, ich brech dir die Beine!!")
#end

