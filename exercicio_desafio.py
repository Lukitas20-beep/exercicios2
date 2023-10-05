login = [0,0,0,0,0]
senha = [0,0,0,0,0]
cont = 0

for x in range(5):
    login[x] = input("Digite seu login: ")
    senha[x] = input("Digite a sua senha: ")

#for y in range(5):
#    print(login[y], y)
#    print(senha[y], y)

try_login = 0
while try_login < 3:
    nome_login = input("Usuário: ")
    for y in range (5):
        if login[y] == nome_login:
            try_login = 3
            print("Usuário válido")
            for z in range(3):
                password_login = input("Senha: ")
                if senha[y] == password_login:
                    print("Login realizado com sucesso")
                    break
                else:
                    print("Senha inválida")
    if try_login < 3:
        print("Usuário inválido")
    try_login += 1
