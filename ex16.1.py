from sys import argv# That is a pakege from argv

script, filename = argv#This is define  the pakege

txt= open(filename)#that line told at computer ...open the file

print(f"Here's your file {filename}:")#print the text...and in {the name of file to open in extension txt}
print ( txt.read())

print("Type the filename again:")#print the text.."Type the fil....again"
file_again = input ( " > ")# the name of file

txt_again = open ( file_again)#open file again

print (txt_again.read())#printeaza continutul fisierului ...prin the cont of file again
