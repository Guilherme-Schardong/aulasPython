#import aula02

#from aula02 import jogar

#from aula02 import *






# lista é uma coleção ordenada e mutavel. permite membros duplicados


lista = ["carro", True, 2, 3.5]
print(type(lista))
print(lista)
print('-'*30)

# Tupla é uma coleção ordenada imutavel. Permite membros duplicados
tupla =("carro", True, 2, 3.5)
print(type(tupla))
print(tupla)
print('-'*30)
# o dicionário é uma coleção ordenanda e mutavel. Nenum membro dulpicado

dicionario = {"nome": "carro", "logica": True, "numeroInt": 2, "numeroFloat": 3.5}

print(type(dicionario))
print(dicionario)

print(dicionario["logica"])
print('-'*30)
# set é uma coleção não ordenada e não indexada. nenhum membro duplicado

conjunto = {"carro", True, 2, 3.5}
print(type(conjunto))
print(conjunto)



data = '25/12/2005'

print(data)

dataLimpa = data.split('/')
dataLimpa = set(dataLimpa)  # cast para conjunto
dataLimpa = list(dataLimpa) # cast para lista
dataLimpa = tuple(dataLimpa) # cast para tupla

print(dataLimpa)

import random

def jogar():
    print('Escolha cara ou coroa: ')
    numeroDoJogador = int(input('(1)Cara (2)Coroa'))
    numeroDeJogadas = int(input('numero de jogadas: '))
    contVitoria = 0
    contDerrota = 0
    for i in range(numeroDeJogadas):
        moeda = random.randint(1,2)
        if(numeroDoJogador == moeda):
            contVitoria = contVitoria + 1
        else:
            contDerrota = contDerrota + 1
    print('Voce ganhou {} vezes de {}'.format(contVitoria, numeroDeJogadas))
    print('Voce perdeu {} vezes de {}'.format(contDerrota, numeroDeJogadas))
if(__name__ == '__main__'):
    jogar()

print(__name__)
def novafuncao():
    print('ola')