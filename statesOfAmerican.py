import os
import re
americanFile = open('..\American.txt','r')
americanContent = str(americanFile.readlines())
americanRegex = re.compile(r'[A-Z][a-z]+')
listofamerican = []
for groups in americanRegex.findall(americanContent):
    listofamerican.append(groups)
listofamerican.sort()
print  listofamerican
americanFile.close()
