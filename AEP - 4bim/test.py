#this opens a file in append mode
file = open("C:\\Users\\eduar\\Documentos\\Prog Python\\Study\\TesteSenhaPython.csv", "a+")
#file = open("C:\\Users\\eduar\\Documentos\\Excel\\TesteSenhaPython.csv", "a+")


#text input to write in file
name = input("Name of the site (i.e www.udemy.com)")
url = input("Enter the URL: ")
user = input("Enter the Username: ")
pswrd = input("'Random shit we will generate': ")
note = input("Enter note (not needed): ")


txt = name + "," + url + "," + user + "," + pswrd + "," + note
#writes in file

"""if file.seek(0):
    file.write(txt+"\n")
else:"""

file.write("name,url,username,password,note\n"+txt+"\n")

#move cursor to the beggining of file
file.seek(0)

#print content of file
print("\n" + file.read())

#close file
file.close()