preco = 100 

imposto = 30


def calc_impost(preco, imposto):
    resultado = preco * (imposto/100)
    return resultado

print(calc_impost(preco,imposto))


calculo = lambda x,y: x * (y/100)

print(calculo(preco,imposto))
