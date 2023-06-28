

# def saudacao(nome, sobrenome,segundoNome=None):
#     print(segundoNome)
#     print(nome)
#     print(sobrenome)
#     print('ola a todos meu nome é {} {}'.format(nome,sobrenome))


# a = 'Guilherme'
# b = 'Schardong'

# saudacao(sobrenome=b,nome=a)



# frutas = ['maçã', 'banana', 'laranja']
# print("Lista original:", frutas)

# frutas.append(a)

# print(frutas)

# a = 10
# b = 5
# c = b-a
# print(abs(b-a))



#crie um jogo de pedra papel e tesoura o jogo deve dizer se 
#o usuario ganhou ou perdeu e se empatar         
#deve pedir ao usurio para selecionar uma opção nova


# crie um programa que conte quantas vogais a na string passada pelomusuario



import random

def gerador_de_senhas():
    caracteres = 'abcdefghijklmnopqrstuvyxzABCDEFGHIJKLMNOPQRSTUVYXZ0123456789'
    tamanho = int(input('Qual o tamanha da senha que você deseja: '))
    senha=''

    for i in range(tamanho):
        caract = random.choice(caracteres)
        senha += caract
    
    print(senha)

if(__name__=='__main__'):
    gerador_de_senhas()

