#To open the file, use the built-in open() function.
#The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())

#Read Only Parts of the File By default the read() method
#returns the whole text,
#but you can also specify how many characters you want to return:
f = open("demofile.txt", "r")
print(f.read(5))

#Read Lines You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())

#By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)

#Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()

'''
#Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

#Open the file "demofile.txt" and overwrite the content:

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
'''

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

#Create a file called "myfile.txt":
f = open("myfile.txt", "x")