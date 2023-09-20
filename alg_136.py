nome = str(input("\nEntre com o nome: "))
idade = int(input("\nEntre com a idade: "))
if (idade <= 10):
    print("\n", nome, "\npagará R$30,00")
elif (idade > 10 and idade <= 29):
    print("\n", nome, "\npagará R$60,00")
elif (idade > 29 and idade <= 45):
    print("\n", nome, "\npagará R$120,00")
elif (idade > 45 and idade <= 59):
    print("\n", nome, "\npagará R$150,00")
elif (idade > 59 and idade <= 65):
    print("\n", nome, "\npagará R$250,00")
else:
    print("\n", nome, "\npagará R$400,00")
print("\n")

