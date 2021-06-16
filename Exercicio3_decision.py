# Nome: Victor Hugo
# Data: 14/08/20
# O programa mostra o que for digitado de acordo com o usuario F ou M , invalido.

nome = input(" Digite a primeira letra, sendo F p/ Feminino e M p/ masculino: ");

if (nome == "F" or "f"):
    print (" Feminino");
elif (nome == "M" or "m"):
    print (" Masculino");
else:
    print (" invalido ")