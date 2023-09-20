import math as m
x = float(input("\nDigite o valor de x: "))
fx = 0

if (x > 4 or x <(-4)):
    fx = (5 * x + 3) / m.sqrt(x ** 2 -16)
    print(f"\nf(x): {fx:.2f}")
else:
    print("\nNAO PODE SER FEITA")

