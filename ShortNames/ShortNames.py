
def abreviar(lista_todos_os_nomes):

    lista_nomes_abreviados=[]
    lista_final=[]


    for i in range(0, len(lista_todos_os_nomes)):
        abreviado = ""
        if len(lista_todos_os_nomes[i]) <=2:

            inicial = lista_todos_os_nomes[i][0]
            final = lista_todos_os_nomes[i][1]

        else:
            inicial = lista_todos_os_nomes[i][0]

            final = lista_todos_os_nomes[i][len(lista_todos_os_nomes[i])-1]

        for j in range(1, len(lista_todos_os_nomes[i])-1):

            if lista_todos_os_nomes[i][j] != "e":
                if   lista_todos_os_nomes[i][j] != "de":
                    if   lista_todos_os_nomes[i][j] != "da":
                        if   lista_todos_os_nomes[i][j] != "das":
                            if   lista_todos_os_nomes[i][j] != "do":
                                if   lista_todos_os_nomes[i][j] != "dos":
                                    abreviado = abreviado + " " + lista_todos_os_nomes[i][j][0] + "."


        nome_abreviado = inicial + " " + abreviado + " " + final
        lista_final.append(nome_abreviado)

    return lista_final

def imprimir(lista_final):

    for i in range(0, len(lista_final)):

        print(lista_final[i])


#-----------------------------------CORPO DO PROGRAMA--------------------------------------------

i=1
lista_todos_os_nomes=[]

while i == 1:

    nome = input("Digite o nome: ")
    if nome=="":
        break
    else:

       vetor_nome = nome.split()
    lista_todos_os_nomes.append(vetor_nome)

imprimir(abreviar(lista_todos_os_nomes))



