# fruta = 'laranja'

# print('Suco de %s é o meu favorito'%fruta)

# %s substitui por uma variavel string
# %d substitui por uma varivel inteira decimal
# %f substitui por uma variavel float

# print('Suco de {} é o meu favorito'.format(fruta))

# cor1= 'azul'
# cor2= 'rosa'
# print('O céu é {1}, a flor é {0} e meu carro é {1}'.format(cor1, cor2))




# conta= 17/3
# print(conta)

# print('o resultado da conta é {:.2f}'.format(conta))

# {:7.2f}
# o primeiro numero é o tatal de caracteres e o segundo numero
# é a quantidade de numeros depois da virgula
# acerscentando um numero na o do 7 no caso voce pode pedir 
# para esse se o que completa os espaços em branco





# for i in range(1,11,3):
#     print(i)

# palavra = 'Matematica'
# for i in palavra:
#     print(i)

# lista = [2,4,6,7,8,80,54]

# for i in lista:
#     print(i)



# contador = 0
# while contador<10:
#     print(contador)
#     if contador==5:
#         print('chegou em 5')
#         continue
#     contador += 1  
# print('aqui nao é while')




import random

def jogar():

    print('*******************************')
    print('*****jogo de adivinhação*******')
    print('*******************************')

    numero_secreto_comp = random.random()

    random.seed(100)
    numero_secreto = random.randrange(1,101)

    print(numero_secreto_comp)
    print(numero_secreto)

    numero_tentativas = 3
    print('voce tem tres tentavias')
    for i in range (1,3+1):
        print('tentativa {}'.format(i))
        chute = int(input('Digite um numero: '))
        
        if chute == numero_secreto:
            print('voce acertou')
            break
        else:
            print('voce errou')

    print('Fim do jogo')
if(__name__ == '__main__'):
    numero = 2508



# variavel = 4
# conta =1
# for i in range(1, variavel+1):
#     conta *= i

# print(conta)

