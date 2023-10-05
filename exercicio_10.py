N = int(input("Insira o tamanho do Array: "))

A = [0] * N
B = [0] * N
Soma = [0] * N

for x in range(N):
    A[x] = int(input("Digite o(s) número(s) de A: "))
for x in range(N):
    B[x] = int(input("Digite o(s) número(s) de B: "))

for x in range(N):
    Soma[x] = A[x] + B[x]

print(A)
print(B)
print(Soma)