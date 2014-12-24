#Turns training file into correct input for EM training
import sys
import argparse
import codecs

try:
    parser = argparse.ArgumentParser(description="convert data for training a LM in carmel")
    parser.add_argument('smoothFile', help='data to get counts from')
    parser.add_argument('--separator', default='_', help='token dividing words')
    parser.add_argument("--outfile", "-o", default='smooth_em_input.data', help='name of file to write')
    args = parser.parse_args()

    smoothFile = str(sys.argv[1])
except:
    print "Bad Input."
    print "Correct Input Format:"
    print "bash LanguageModel.sh <Train.data> <Smooth.data> <size of model> <# counts to be excluded>"
    sys.exit()

smoothFile = args.smoothFile
separator = args.separator
reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')

inputLines = [line.rstrip('\n') for line in reader(open(smoothFile))]

outputLines = writer(open(args.outfile,'w'))


for i in range(0,len(inputLines)):
	sentence = inputLines[i]
	line = ""
	for j in range(0,len(sentence)):
		if sentence[j] == ' ':
			line+= "\"%s\" " % separator
		else:
			line+= "\""+sentence[j]+"\" "
	outputLines.write("\n")	
	outputLines.write(line+"\n")
