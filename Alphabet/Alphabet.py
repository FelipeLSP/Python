def palavras_geradas(n, vetor_letras):

    vetor_palavras_geradas=[]

    for i in range(0, n):
        vetor_palavras_geradas.append(vetor_letras[i])

    for t in range(1, n):
        if t==1:
            for i in range(0, n):
                for j in range(0, n):

                    palavras_geradas = vetor_letras[i] + vetor_palavras_geradas[j]
                    vetor_palavras_geradas.append(palavras_geradas)
        if t == 2:
            for i in range(0, n):
                for j in range(0, (n**t)):

                    palavras_geradas = vetor_letras[i] + vetor_palavras_geradas[(j+(n**(t-1)))]
                    vetor_palavras_geradas.append(palavras_geradas)
        if t > 2:
            for i in range(0, n):
                for j in range(0, (n**t)):

                    palavras_geradas = vetor_letras[i] + vetor_palavras_geradas[((j+n)+(n**(t-1)))]
                    vetor_palavras_geradas.append(palavras_geradas)

    return vetor_palavras_geradas

#-----------------------------------CORPO DO PROGRAMA--------------------------------------------

nome = input("Digite as letras: ")
vetor_letras = nome.split()

n = len(vetor_letras)

vetor_palavras = palavras_geradas(n, vetor_letras)

print(vetor_palavras)
