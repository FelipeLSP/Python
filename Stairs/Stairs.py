def fibonnaci(n):
    x = 1
    y = 2

    if n == 1:
        sum = 1

    if n == 2:
        sum = 2
    else:

        for i in range(2, n):

            sum = x + y
            x = y
            y = sum

        return sum

#-----------------------------------CORPO DO PROGRAMA--------------------------------------------

n = int(input("Digite o número de degraus da escada: "))

qtd_formas_de_subir = fibonnaci(n)

print("Posso subir a escada de ",n, " degraus de", qtd_formas_de_subir, "formas diferentes")