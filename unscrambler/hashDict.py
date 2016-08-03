#!/usr/bin/python

import sys


def hashFile(file):
     f = open( "dictionary.txt", 'r')
     f1 = open( file, "w");
     for line in f:
	  f1.write(hashLine(line)+":"+line)

def hashLine(line):
     minIndex = 0
     li = convertToList(line); 
     i = 0;
     j = 0;
     #START OF SELECTION SORT
     while(i< len(li)-1):
	  j = i+1
	  minIndex = i 
	  while(j<len(li)):
	       if (ord(li[j]) < ord(li[minIndex])):
		    minIndex = j 
	       j+=1 
	  temp = li[i]
	  li[i] = li[minIndex] 
	  li[minIndex] = temp
	  i+=1
     #END OF SELECTION SORT 

     
     li2 = list()
     count = 0
     iteration = 0
     currentChar = li[0]
     for c in li:
	  iteration += 1 
	  
	  isEnd = 1 if iteration == len(li) else 0

	  if (c != currentChar or isEnd): 
	       if(isEnd):
		    count+=1
	       if(currentChar != '\r' and  currentChar != '\n'):
		    li2.append(str(count))
		    li2.append(currentChar)
	       count=0
	       currentChar = c 
	  count+=1
     return convertToString(li2) 
     
def convertToList(str):
     returnMe = list()
     for c in str:
	       returnMe.append(c)
     return returnMe 

def convertToString(li):
     return ''.join(li)


if( len(sys.argv) < 2):
     arg1 = "dictionary_hash.txt"
else:
     arg1 = sys.argv[1] 
print "The resulting file will be saved to " + arg1

hashFile(arg1)
