import os

# path = (r'C:\Users\Aluno\Desktop')

# os.chdir(path)

# print(os.getcwd())


# print(os.listdir())

# os.startfile(r'C:\Users\Aluno\Desktop\turma python\python\teste.txt')

# os.rename('teste.txt','testemodificado.txt')


#os.remove(r'C:\Users\Aluno\Desktop\turma python\python\oi.txt')

# print(os.path.isfile(r'C:\Users\Aluno\Desktop\turma python\python\testemodificado.txt'))

#print(os.path.isdir(r'C:\Users\Aluno\Desktop\turma python\python\testemodificado.txt'))


for root, dirs, files in os.walk(os.getcwd()):
    print(files)