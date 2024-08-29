#this opens a file in append mode
f = open("C:\\Users\\eduar\\Documentos\\Prog Python\\Hello.txt", "a+")

#text input to write in file
txt = input("Enter input to write in file: ")

#writes in file
f.write("\n" + txt)
#close file

#move cursor to the beggining of file
f.seek(0)

#print content of file
print("\n" + f.read())

f.close()