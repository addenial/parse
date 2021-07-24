


import os
import sys
import subprocess

if len (sys.argv) != 2 :
    print("Usage: python results.cvs ")

    print("  use to show uniquue lines in CSV only ") 
    sys.exit (1)

mahcvss = sys.argv[1]

#cmd = "cat " + sys.argv[1] + " | sort -n | uniq "
#arg 0 is the csv,
#returned_output = subprocess.call(cmd, shell=True)
#print(returned_output.decode("utf-8"))

f = open(mahcvss, "r")
lines = set(f.readlines())

#print(lines)
e = sorted(lines, reverse=True)
#print(e)
print("\r".join(e))
#s = "," . join(lines)
#if fist character is , then strip it before priting
#also reverse sort this 


#print(s)

#to remove first character
#s = "hello"
#print s[1:]

#print("," . join(lines).strip(','))
#print(*lines, sep = ",")

#bash example-
#cat results.csv | sort -n | uniq 

