import math
import sys
import argparse
from collections import defaultdict as dd
import itertools
import codecs
try:
    parser = argparse.ArgumentParser(description="build a character lm fst")
    parser.add_argument('trainFile', help='data to get counts from')
    parser.add_argument('nGramSize', type=int, default=2, help='What NGram model the user wants to have')
    parser.add_argument('countsToRemove', type=int, default=0, help='Zero by default, can be made to (n) not include counts <= (n)')
    parser.add_argument("--outfile", "-o", default='Non_Trained.wfsa', help='name of file to write')
    args = parser.parse_args()
except:
    print "Bad Input."
    print "Correct Input Format:"
    print "bash LanguageModel.sh <Train.data> <Smooth.data> <size of model> <# counts to be excluded>"
    sys.exit()

trainFile = args.trainFile
nGramSize = args.nGramSize
countsToRemove = args.countsToRemove
reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')

trainText = [line.rstrip('\n') for line in reader(open(trainFile))]
#These will be the probabilities that are used for building the levels of the WFST
previousDist = [] #Index 0 will be dict of unigram probabilites and index 1 bigram, etc
prevCounts = [] #Index 0 will be unigram counts, index 2 bigrams, etc...


currentCounts = {} #In the form (Example for bigram counts) (A,B):Count where P(B|A) = Count(A,B)/Count(A), size nG + 1
previousCounts = {} #Counts of N-Gram size nG
currentProbabilities = {} #Current probabilites of N-Gram size nG+1
previousProbabilities = {} #Probabilities with N-Gram size nG

#Now preprocess the text so to tokenize it:
for i in range(0,len(trainText)):
    if ((trainText[i].count('"') % 2) == 1) or (trainText[i].count('"') == 0):
        print "Error bad input format in train file on line",i+1
        sys.exit()
    line = list(trainText[i])

    firstQuote = False #Used to signal whether first quote has been seen or not
    tokens = []
    token = ""
    for char in line:
        #In the process of getting token
        if firstQuote:
            if char == "\"":
                firstQuote = False
                tokens.append(token)
                token = ""
            else:
                token +=char
        #In the process of ignoring all characters until next quote is seen
        else:
            if char == "\"":
                firstQuote = True
                token = ""
    trainText[i] = tokens

for nG in range(0,nGramSize):
    
    #Getting current nGramCounts nG is one less than the current n-gram size counts being collected
    for i in range(0,len(trainText)): 
        sentence = trainText[i][:]
        sentence.insert(0,"START")
        sentence.append("END")

        for j in range(0,len(sentence)-nG):
            tup = []
            for k in range(0,nG+1):
                tup.append(sentence[j+k])
            tup = tuple(tup)
            if tup not in currentCounts:
                currentCounts[tup] = 1
            else:
                currentCounts[tup] += 1
    
    #Remove any counts < countsToRemove
    keyToDelete = []
    for tup in currentCounts:
        if currentCounts[tup] <= countsToRemove:
            keyToDelete.append(tup)
    for key in keyToDelete:
        del currentCounts[key]

    if nG == 0:
        totalLetterCount = 0
        for tup in currentCounts:
            if tup[0] != "START":
                totalLetterCount+=currentCounts[tup]

    #Now lets get current Probabilities
    #Special case if unigram probabilities
    if nG == 0:
        for tup in currentCounts:
            if tup[0] != "START":
                currentProbabilities[tup] = currentCounts[tup]/float(totalLetterCount)
    else:
        for tup in currentCounts:
            newTup = []
            for i in range(0,len(tup)-1):
                newTup.append(tup[i])
            newTup = tuple(newTup)
            currentProbabilities[tup] = currentCounts[tup]/float(previousCounts[newTup])

    if (nG != 0) and (countsToRemove !=0): #
        # now to reweight probabilities if counts are removed
        reweighting = {} #In the for prevTup :sum

        for tup in currentProbabilities:
            prevKey = tuple(list(tup)[0:len(tup)-1])
            if prevKey not in reweighting:
                reweighting[prevKey] = currentProbabilities[tup]
            else:
                reweighting[prevKey] += currentProbabilities[tup]


        for tup in currentProbabilities:
            prevKey = tuple(list(tup)[0:len(tup)-1])
            currentProbabilities[tup] = currentProbabilities[tup]/reweighting[prevKey]

    prevCounts.append(currentCounts)
    previousDist.append(currentProbabilities)

    previousProbabilities = currentProbabilities
    previousCounts = currentCounts
    currentProbabilities = {}
    currentCounts = {}
    


LMFile = writer(open(args.outfile,'w'))
LMFile.write("END\n") #The final state

#Build unigram/bi state to start since special case

unigramProbs = previousDist[0]
bigramProbs = previousDist[1]

LMFile.write("(START (UNI *e* *e* ))\n")
LMFile.write("(START (BI_START *e* *e* ))\n")

currentCountGroup = 1


#Arrage similar counts for bigrams
currCounts = {} #In the form count:[N-gram,N-gram,]
for tup in prevCounts[0]:
    if prevCounts[0][tup] not in currCounts:
        currCounts[prevCounts[0][tup]] = []
        currCounts[prevCounts[0][tup]].append(tup)
    else:
        currCounts[prevCounts[0][tup]].append(tup)

countNumbers  =  sorted(currCounts)

groups = []

for i in range(0,len(countNumbers),1):
    groups.append(countNumbers[i:1+i])

countLookUp = {} #In the form tup:groupNumber

for i in range(0,len(groups)):
    for j in range(0,len(groups[i])):
        tempList = currCounts[groups[i][j]]
        for k in range(0,len(tempList)):
            countLookUp[tempList[k]] = i + currentCountGroup
currentCountGroup += len(groups)

# numeric id for each token to avoid carmel mischief
# warning: P stuff, END, START not mapped
states = dd(itertools.count().next)
#Build first connections for unigrams
for tup in unigramProbs:
    if tup[0] != "END":
        endingState= str(states["~" + tup[0] + "~"])
        LMFile.write("(UNI (" +endingState+" *e* \""+tup[0]+"\" "+str(unigramProbs[tup])+ "!))\n")

        #Now connections going to next stage
        startingState = endingState
        endingState = startingState+"P"

        LMFile.write("("+startingState+" (" +endingState+ " *e* *e* !"+str(countLookUp[tup])+"))\n")
        LMFile.write("("+startingState+" (UNI *e* *e* ))\n")
    else:
        endingState = "END"
        LMFile.write("(UNI (" +endingState+" *e* *e*" +str(unigramProbs[tup])+ "!))\n")

#Now for bigrams starting from the START symbol
for tup in bigramProbs:
    if tup[0] == "START":
        CharTransduced = tup[1]
        endingState= str(states["~" + tup[1] + "~"])
        LMFile.write("(BI_START (" +endingState+" *e* \""+CharTransduced+"\" "+str(bigramProbs[tup])+ "!))\n")

#Build the rest of the layers
#for i in range(2,nGramSize):
for i in range(1,nGramSize-1):
    alreadySeen = {} #Used to make sure that

    #Arrage similar counts for unigrams
    currCounts = {} #In the form count:[N-gram,N-gram,]
    for tup in prevCounts[i]:
        if prevCounts[i][tup] not in currCounts:
            currCounts[prevCounts[i][tup]] = []
            currCounts[prevCounts[i][tup]].append(tup)
        else:
            currCounts[prevCounts[i][tup]].append(tup)

    countNumbers  =  sorted(currCounts)
    groups = []

    for j in range(0,len(countNumbers),1):
        groups.append(countNumbers[j:1+j])

    countLookUp = {} #In the form tup:groupNumber

    for z in range(0,len(groups)):
        for j in range(0,len(groups[z])):
            tempList = currCounts[groups[z][j]]
            for k in range(0,len(tempList)):
                countLookUp[tempList[k]] = z + currentCountGroup

    currentCountGroup += len(groups)

    for tup in previousDist[i]:
        if tup[0] != "START":
            startState = []
            for j in range(0,len(tup)-1):
                startState.append(tup[j])
            startState = ''.join(startState)
            startState = str(states["~"+startState+"~"])+"P"
            if tup[-1] != "END":
                finalState = []
                for j in range(0,len(tup)):
                    finalState.append(tup[j])
                finalState = ''.join(finalState)
                finalState = str(states["~" + finalState + "~"])
            else:
                finalState = "END"

            if tup[-1] == "END":
                LMFile.write("("+startState+" (" + finalState + " *e* *e* " + str(previousDist[i][tup])+ "!))\n")
            else:
                LMFile.write("("+startState+" (" +finalState+" *e* \""+tup[-1]+"\" " +str(previousDist[i][tup])+ "!))\n")


            if (finalState not in alreadySeen) and (finalState!= "END"):
                alreadySeen[finalState] = 1
                LMFile.write("("+finalState+" (" +finalState+"P *e* *e* !"+str(countLookUp[tup])+"))\n")

                newFinal = []
                for j in range(1,len(tup)):
                    newFinal.append(tup[j])

                newFinal = ''.join(newFinal)
                newFinal = str(states["~"+newFinal+"~"])
                LMFile.write("("+finalState+" (" +newFinal+" *e* *e* ))\n")

#Now for the final Stage

for tup in previousDist[-1]:
    if tup[0] != "START":
        prevState = []
        for i in range(0,len(tup)-1):
            prevState.append(tup[i])
        prevState = ''.join(prevState)
        prevState = str(states["~" + prevState + "~"])+"P" 

        if tup[-1] != "END":
            endingState = []
            for i in range(1,len(tup)):
                endingState.append(tup[i])
            endingState = ''.join(endingState)
            endingState = str(states["~" + endingState + "~"])
            CharTransduced = tup[-1]
            LMFile.write("("+prevState+" (" +endingState+" *e* \""+CharTransduced+"\" " +str(previousDist[-1][tup])+ "!))\n")
        else:
            LMFile.write("("+prevState+" (END *e* *e* " +str(previousDist[-1][tup])+ "!))\n")

currentCountGroup = currentCountGroup - 1
#print "Size of language Model:",nGramSize
print "Number of lambdas being trained:",currentCountGroup

