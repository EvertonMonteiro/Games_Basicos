import random

def jogar():
    print("*"*30)
    print("Bem vindo ao jogo de adivinhação!")
    print("*"*30)
    rodada = 1
    pontos = 1000
    total_tentativas = 0
    nivel = int(input("Escolha a dificuldade: (1) Fácil (2) Médio (3) Difícil"))
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    elif nivel == 3:
        total_tentativas = 5
    else:
        print('opção inválida!')
    num_secreto = random.randrange (1, 101)
    for rodada in range (1, total_tentativas + 1):
        print(f'Tentativa {rodada} de {total_tentativas}.')
        palpite = int(input("Qual o seu palpite? (de 0 a 100)"))
        if palpite < 1 or palpite > 100:
            print('Opção Inválida! Escolha um número de 0 a 100.')
            continue
        rodada += 1

        acertou = palpite == num_secreto
        maior = palpite > num_secreto
        menor = palpite < num_secreto

        if acertou:
            print(f"Parabens! Você acertou e fez {pontos}!")
            break
        else:
            if maior:
                print("ERRADO! Você digitou um número maior que o secreto")
                if rodada == total_tentativas:
                    print(f"O número secreto era {num_secreto} e você fez {pontos}!")
            elif menor:
                print("ERRADO! Você digitou um número menor que secreto")
                if rodada == total_tentativas:
                    print(f"O número secreto era {num_secreto} e você fez {pontos}!")
            pontos_perdidos = abs(num_secreto - palpite)
            pontos = pontos - pontos_perdidos


    print("Fim de jogo!")