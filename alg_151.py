peso = float(input("\nDigite seu peso: "))
altura = float(input("\nDigite sua altura: "))
imc = peso / (altura ** 2)
if imc < 20:
    print("\nAbaixo do peso.")
elif imc > 21 and imc <= 25:
    print("\nNormal.")
elif imc > 25 and imc <= 30:
    print("\nExcesso de peso.") 
elif imc > 30 and imc <= 35:
    print("\nObesidade.")
else:
    print("\nObesidade mórbida.")
print("\n")


