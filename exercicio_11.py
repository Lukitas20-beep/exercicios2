A = [0] * 30

quant = 0

buscar = int(input("Digite qual número você quer botar: "))

for x in range(30):
    A[x] = int(input("Digite um número: "))

for y in A:
    if y == buscar:
        quant += 1

print("O número:", buscar, "apareceu", quant, "vezes")