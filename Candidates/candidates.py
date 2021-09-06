def voteCount(candidatesNumber, candidatos, listVotes):

    whiteVotes = 0
    nullVotes = 0
    quantityVotes = []
    for i in range(0, candidatesNumber):

        totalVotes = listVotes.count(candidatos[i][1])
        quantityVotes.append(totalVotes)

    whiteVotes = listVotes.count(0)
    nullVotes = len(listVotes) - (whiteVotes + sum(quantityVotes))

    return quantityVotes, whiteVotes,nullVotes

def functionPrint(candidatesNumber, candidates, quantityVotes, whiteVotes):

    print("Election result: ")
    print()
    for i in range(0, candidatesNumber):

        print(str(candidates[i][0]) + " - " + str(candidates[i][1]) + " - with " + str(quantityVotes[i]) + " vote(s)")

    print("White - with - " + str(whiteVotes) + " vote(s)")
    print("Nulls - with - " + str(nullVotes) + " vote(s)")


#------------------------------Program Body--------------------------------------------------------------------


candidatesNumber = int(input("Type the number of candidates: "))

candidates = []
listVotes = []
quantityVotes = []
whiteVotes = 0
nullVotes = 0

for i in range(1, candidatesNumber + 1):

    name = input("Type the name and the number of the candidate: " + str(i) + ": ")
    parts = name.split("#")
    parts[1] = int(parts[1])
    candidates.append(parts)

while i >= 0:

    number = input("Type the number of your candidate: ")
    i = int(number)
    if i < 0:
        break
    else:
        parts = number.split()
        parts = int(parts[0])
    listVotes.append(parts)

quantityVotes, whiteVotes, nullVotes = voteCount(candidatesNumber, candidates, listVotes)

functionPrint(candidatesNumber, candidates, quantityVotes, whiteVotes)