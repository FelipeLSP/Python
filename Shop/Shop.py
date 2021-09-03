import random

def prod_preco(num_lojas,num_prod,vetor_produtos,vetor_lojas):

    lista_precos=[]
    for i in range(1,num_lojas+1):
        temp=vetor_lojas[i-1]
        preco_loja = []
        preco_loja.append(temp)
        for j in range(num_prod):
            min=vetor_produtos[j][1]
            max=vetor_produtos[j][2]
            preco_randomizado = round(random.uniform(min,max),2)

            preco_loja.append(preco_randomizado)

        lista_precos.append(preco_loja)

    return lista_precos
def menor_preco(qtd_lojas,qtd_produtos,vetor_precos):

    j=0
    vetor_menores_precos=[]

    for i in range(1, qtd_produtos + 1):
        menor_preco_produto = vetor_precos[0][i]
        for j in range(1, qtd_lojas):
            if vetor_precos[j][i] < menor_preco_produto:
                menor_preco_produto = vetor_precos[j][i]
        vetor_menores_precos.append(menor_preco_produto)

    return vetor_menores_precos


def loja_menor_preco(qtd_produtos,qtd_lojas,vetor_menores_precos,vetor_precos):

    nomes_lojas_menor_preco = []
    for i in range(1, qtd_produtos+1):
        compara = vetor_menores_precos[i-1]
        for j in range(qtd_lojas):
            if compara == vetor_precos[j][i]:
                nome_loja = vetor_precos[j][0]
        nomes_lojas_menor_preco.append(nome_loja)

    return nomes_lojas_menor_preco



def soma_menores(vetor_menores):

    soma_menores_precos=0
    soma_menores_precos=sum(vetor_menores)

    return soma_menores_precos


def imprimir(qtd_loja,qtd_produto,vetor_lojas,vetor_produtos,nomes_lojas_menor_preco,soma_menores_precos):

    print("Resultado da pesquisa: ")

    for i in range(0, qtd_produto+1):
        if i == 0:
            print(end="        ")
        else:
            print(vetor_produtos[i-1][0], end="     ")
    print()

    for j in range(0,qtd_loja):
        for k in range(0,qtd_produto+1):
            print(vetor_lojas[j][k],end="      ")
        print()
    print()

    print("Menores Preços: ")

    for i in range(0,qtd_produto):
        print(vetor_produtos[i][0]," ",nomes_lojas_menor_preco[i])
    print()

    print("Valor Total:")
    print(soma_menores_precos)

#-----------------------------------CORPO DO PROGRAMA--------------------------------------------


qtd_lojas = int(input("Digite a quantidade de lojas: "))
qtd_prod = int(input("Digite a quantidade de produtos: "))

vetor_lojas= []
vetor_produtos=[]

for i in range(qtd_lojas):
    nome=(input("Digite o nome da loja "+str(i+1)+ ": " ""))
    vetor_lojas.append(nome)

for i in range(1,qtd_prod+1):

    nome = (input("Digite o nome dos produto "+str(i)+ " seguido do preço mínimo e máximo: "))
    partes=nome.split()
    for ind in range(1, len(partes)):
        partes[ind] = float(partes[ind])
    vetor_produtos.append(partes)


vetor_precos = prod_preco(qtd_lojas,qtd_prod,vetor_produtos,vetor_lojas)
vetor_menores_precos = menor_preco(qtd_lojas,qtd_prod,vetor_precos)
soma_menores_precos = soma_menores(vetor_menores_precos)
nomes_lojas_menor_preco = loja_menor_preco(qtd_prod,qtd_lojas,vetor_menores_precos,vetor_precos)


imprimir(qtd_lojas,qtd_prod,vetor_precos,vetor_produtos,nomes_lojas_menor_preco,soma_menores_precos)