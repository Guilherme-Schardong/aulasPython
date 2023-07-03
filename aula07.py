#open("data/teste.txt","x")

# f = open("data/teste.txt","w")

# f.write("\nDiogo")
# #print(f.readlines())

# f.close()

# nome = str(input('digite seu nome: '))

# with open("data/teste.txt","r+") as f:   
#     f.write('\n'+nome)
#     print(f.readlines())

with open("data/teste.txt","r") as a:
    for line in a:
        if(len(line)<5):
            print(line)
