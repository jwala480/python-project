#Create and write to a file
file = open("data.txt","w")
file.write("Hello World!\n")
file.write("Welcome to vvitu\n")
file.close()
#Read the file and use tell()
file = open("data.txt","r")
print("Initial cursor position:",file.tell())
content = file.read(5)
print("Read content:",content)
print("Cursor position after reading 5 chars:",file.tell())
#use seek()
file.seek(0) # MOve cursor back beginning
print("Cursor position after seek(0):",file.tell())
content = file.read()
print("Full content after seek:\n",content)
#Append data using "a" mode
file = open("data.txt","a")
file.write("This is appended text.\n")
file.close()
print("Data appended successfully!")
#Read the file after appending data
file = open("data.txt","r")
content = file.read()
print("Content after appending = ",content)


