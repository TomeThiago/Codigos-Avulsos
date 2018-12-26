from random import randint
import time

print("############################################################")
print("                      ADIVINHE O NUMERO!")
print("############################################################")

jogo = input("Se deseja começar o jogo responda 'Sim': ")

if (jogo.lower() == "sim"):

    print("Seja Bem-Vindo!\n")

    time.sleep(3)

    print("As regras são simples.\nO jogador tem 10 chances de adivinhar qual é o número que o computador gerou aleatoriamente de 1 a 100.")
    time.sleep(1)
    print("Se o número do chute for baixo, o computador retornará 'BAIXO', se o número chutado for alto, o computador retornará 'ALTO'\n")

    time.sleep(1)

    print("Vamos começar!")

    time.sleep(1)

    numero = randint(1,100)
    tentativas = 0
    ganhou = False

    time.sleep(1)

    while ((tentativas <= 10) and (ganhou == False)):

        chute = int(input("Digite um número de 1 a 100: "))
        
        if (chute != numero):
            tentativas = tentativas + 1
            if (chute < numero):
                print("MAIOR!")
            else:
                print("MENOR!")
        else:
            ganhou = True

    if (tentativas == 11):
        print("\nGame Over!")
        time.sleep(1)
        print("O número era "+ str(numero))
    else:
        print("\nParabens você acertou!")
else:
    print("\nAté a próxima!")
    time.sleep(3)