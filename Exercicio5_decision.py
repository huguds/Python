# O programa faz a verificação de login
import time

# Cadastro do usuário
cnome = input("Digite o nome para cadastro: ");
csenha = input("Digite a senha para cadastro: ");
print ("");
print ("Carregando...");
time.sleep(3);
print ("");
print ("Usuário:",cnome);
print ("Cadastrado com sucesso !");

# Decisão

tent = 5;
dec = input ("Deseja efetuar o login: Digite S ou N: ");

if (dec == "S" or "s"):
    while (tent > 0):
        print ("")
        nome = input ("Digite seu nome: ")
        senha = input ("Digite a senha: ")
        if (nome != cnome or senha != csenha):
            print ("Tente novamente")
            tent -= 1
            print ("")
            print ("Numero de tentativas: ",tent)
            if (tent == 0):
                time.sleep(3)
                print ("")
                print ("Excedeu o numero de tentativas")
        else:
            print ("")
            print ("Login efetuado com sucesso")
            print ("Bem-vindo ",nome)
            break
elif (dec == "N" or "n"):
    print ("Programa encerrado")
else:
    print ("Error")