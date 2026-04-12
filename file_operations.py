#Creating file using 'w' mode
file = open("sample.txt","w")
file.write("Hello World\nPython\n")
file.close()
print("After 'w' mode 	(created file):")
file = open("sample.txt","r")
content = file.read()
print("Content reading = ",content)
file.close()
# Read and Write using 'r+'
file = open("sample.txt","r+")
print("\nUsing 'r+' mode (original content ) : ",file.read())
file.seek(0)
file.write("Hi")
file.close()
file = open("sample.txt","r")
print("Content after modification : ",file.read())
file.close()
#Append uisng 'a' mode
file = open("sample.txt","a")
file.write("New line added using 'a'(mode)")
file.close()
file = open("sample.txt","r")
print("After 'a' mode:")
print(file.read())
file.close()
#Append and Read using 'a+' mode
file = open("data.txt", "a+")
file.write("Extra Line using a+\n")

file.seek(0)
print("\nUsing 'a+' mode:")
print(file.read())

file.close()

