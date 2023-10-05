Nomes = [0,0,0,0,0]
for x in range(5):
    Nomes[x] = input("Digite 5 nomes: ")
print(Nomes)

for y in range(5):
    print("Os nomes numa ordem normal são: ",Nomes[y])

for z in range(4,-1,-1):
    print("Os nomes em inverso são: ", Nomes[z])