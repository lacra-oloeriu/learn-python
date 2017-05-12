from sys import argv#import argv

script, input_file = argv#define argv

def print_all(f):#function print text
    print(f.read())#read and print the text

def rewind(f):#funtion rewind
    f.seek(0)

def print_a_line(line_count, f):#funtion ptint a line
    print(line_count, f.readline())#real line

current_file = open(input_file)#open file

print("First let's print the whole file:\n")#print the file

print_all(current_file)#^print all

print("Now let's rewind, kind of like a tape.")#print the text

rewind(current_file)#reread curent file

print("Let's print three lines:")#print the 3lines

current_line = 1#ptint line 1
print_a_line(current_line, current_file)

current_line = current_line + 1#print line 2
print_a_line(current_line, current_file)

current_line = current_line + 1#print line 3
print_a_line(current_line, current_file)
