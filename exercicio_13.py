vetorNums = []
vetorPares = []
vetorMaiorMenor = []
somaNums = 0
numMaior = 0
numMenor = 1
acimaMedia = 0

for x in range(30):
    num = int(input("Digite os números: "))
    vetorNums += [num]
    somaNums += num

for y in range(30):
    if vetorNums[y] % 2 == 0:
        vetorPares += [vetorNums[y]]

for z in range(30):
    if vetorNums[z] >= numMaior:
        numMaior = vetorNums[z]
    if vetorNums[z] <= numMenor:
        numMenor = vetorNums[z]

vetorMaiorMenor += [numMenor] + [numMaior]

media = somaNums / 30

for i in range(30):
    if vetorNums[i] > media:
        acimaMedia += 1

print("TEMOS:",vetorNums,"Números")
print("Os números pares são:", vetorPares)
print("O menor e o maior número do vetor são, respectivamente:",vetorMaiorMenor)
print("Há:", acimaMedia, "Números acima da média")