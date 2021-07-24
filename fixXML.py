
import os


path = '.'
cwd = os.getcwd()

for filenameeach in os.listdir(cwd):
                if not filenameeach.endswith('.xml'): continue
                fullname = os.path.join(path, filenameeach)

                #print(filenameeach)
                #print(fullname)
                

                with open(filenameeach,'rb') as f:
                    f.seek(-2,os.SEEK_END)
                    while f.read(1) != b'\n':
                        f.seek(-2, os.SEEK_CUR)
                    last_line = f.readline().decode()

                #    print(last_line)
                #u = open(filenameeach, "r")
                #print(u.read()) 
                #print only last line 
                #last_line = u.readlines()[-1]
                #print(last_line)   
                
                #check if last line contains proper closing xml syntax
                if last_line == "</nmaprun>\n":
                    #print("ayiiiii ok")
                    continue
                else: 
                    print("prob brokn " + filenameeach)
                    
                    #open file, give it append permission - a
                    print("   appending xml fix")
                    o = open(filenameeach, "a")
                    o.write("</nmaprun>\n")
                    o.close()
                
                
