import forca
import adivinhaçao
print("*"*30)
print("Escolha o seu jogo!")
print("*"*30)

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual a sua escolha? "))

if jogo == 1:
    print("Jogando forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhaçao.jogar()
else:
    print("Opção inválida")