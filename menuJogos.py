import aula02
import aula03
print('************************************')
print('************************************')
print('Selecione o jogo que voce quer jogar')
print('************************************')
print('************************************')
selecao = int(input('Digte\n (1)Adivinhação\n (2)Cara ou Coroa '))

if(selecao == 1):
    aula02.jogar()
else:
    aula03.jogar()