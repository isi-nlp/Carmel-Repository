#Turns training file into correct input for EM training
import sys
import argparse
import codecs

try:
    parser = argparse.ArgumentParser(description="convert data for training a LM in carmel")
    parser.add_argument('smoothFile', help='data to get counts from')
    parser.add_argument("--outfile", "-o", default='smooth_em_input.data', help='name of file to write')
    args = parser.parse_args()

    smoothFile = str(sys.argv[1])
except:
    print "Bad Input."
    print "Correct Input Format:"
    print "bash LanguageModel.sh <Train.data> <Smooth.data> <size of model> <# counts to be excluded>"
    sys.exit()

smoothFile = args.smoothFile
reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')

inputLines = [line.rstrip('\n') for line in reader(open(smoothFile))]
outputLines = writer(open(args.outfile,'w'))

for i in range(0,len(inputLines)):
	sentence = inputLines[i]
	if sentence.count('"') %2 ==1 or sentence.count('"') ==0:
		print "Error bad input format in smooth file on line",i+1
		sys.exit()

	outputLines.write("\n")	
	outputLines.write(sentence+"\n")
