# file handling 

#when you want to copy a data from one file to anoather file

# f=open("demo.txt","r")
# f1=open("demo1.txt","w")
# reading=f.read()
# for i in f:
#     f1.write(i)
# f.close()
# f1.close()

# f = open("demo.txt", "r")
# f1 = open("demo1.txt", "w")

# # Read all content from the first file
# content = f.read()

# # Write the content to the second file
# f1.write(content)

# # Close the files
# f.close()
# f1.close()


f = open("myfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")
