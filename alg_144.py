sm = float(input("\nDigite o saldo médio: "))
cred = 0
if (sm <= 500):
    cred = 0
elif (sm > 501 and sm <= 1000):
    cred = sm * 0.3
elif (sm > 1001 and sm <= 3001):
    cred = sm * 0.4
else:
    cred = sm * 0.5

if (cred == 0):
    print(f"\nComo seu saldo era de: {sm}, seu crédito será de: {cred}")
else:
    print(f"\nComo seu saldo era de: {sm}, seu crédito será de: {cred}.")
print("\n")

