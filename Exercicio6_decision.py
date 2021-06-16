from time import sleep

def leiaInt (msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print ('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print (' Usuário não digitou um número')
            return 0
        else:
            return n

def linha (tam=42):
    return '-'*tam

def cabecalho (txt):
    print (linha())
    print (txt.center(42))
    print (linha())

def menu (lista):
    cabecalho ('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -\033[34m {item}\033[m')
        c += 1
    print (linha())
    opc = leiaInt('\033[33mSua opção:\033[m');
    return opc
    
while True:
    resposta = menu(['Cadastrar','Consultar','Sair'])
    if resposta ==1:
        print ("")
        print ('Opção 1')
        print (linha())
        print ("\033[31mCarregando..\033[m")
        print (linha())
        sleep(2)
    elif resposta ==2:
        print ('Opção 2')
    elif resposta ==3:
        print ('Saindo do sistema... Até logo !')
        break
    else:
        print ('\033[31mERROR: Digite uma opção válida\033[m')
    sleep(2);


