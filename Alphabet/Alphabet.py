def generatedWords(n, listLetters):

    listGeneratedWords=[]

    for i in range(0, n):
        listGeneratedWords.append(listLetters[i])

    for t in range(1, n):
        if t == 1:
            for i in range(0, n):
                for j in range(0, n):

                    generatedWords = listLetters[i] + listGeneratedWords[j]
                    listGeneratedWords.append(generatedWords)
        if t == 2:
            for i in range(0, n):
                for j in range(0, (n**t)):

                    generatedWords = listLetters[i] + listGeneratedWords[(j + (n ** (t - 1)))]
                    listGeneratedWords.append(generatedWords)
        if t > 2:
            for i in range(0, n):
                for j in range(0, (n**t)):

                    generatedWords = listLetters[i] + listGeneratedWords[((j + n) + (n ** (t - 1)))]
                    listGeneratedWords.append(generatedWords)

    return listGeneratedWords

#-----------------------------------CORPO DO PROGRAMA--------------------------------------------

name = input("Type the letters: ")
listLetters = name.split()

n = len(listLetters)

listWords = generatedWords(n, listLetters)

print(listWords)
