#LatexTable

inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')

outFile.write("\\begin{tabular}{}\n")
outFile.write("\t\hline\n")

for line in inFile:
	inList = line.split("\t") #splits the input line into a list of values/words
	if(len(inList)<=1): continue #empty lines are ignored
	
	outList = ["\t"] #starts building the output line
	
	# insert "[tab]&" after each value/word
	for i in inList:
		outList.append(i)
		outList.append("\t& ")
		
	# remove the last element in the list, which is a "[tab]&"
	outList.pop()
	
	# removes "\n" and/or "\r" from the end of the last value/word by
	# adding a new element and removing the old
	while (outList[-1].endswith("\n") or outList[-1].endswith("\r")):
		outList.append(outList[-1][:-1])
		outList.pop(-2)
		
	outList.append("\t\\\ \hline\n")
	outFile.write(''.join(outList))
	
outFile.write("\end{tabular}")
inFile.close()
outFile.close()
