fw = open("Cru.txt",'w')
fw.write("Cru searching PW\n")
fw.write("Cru finding PW\n")
fw.write("Cru getting PW\n")
fw.close()

fr=open("Cru.txt",'r')
textStr = fr.read()
print(textStr)
fr.close()