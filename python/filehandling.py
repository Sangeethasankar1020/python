# file handling
f = open("demofile2.txt", "a")
f.write("Now the file has more content! good")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()
import os
if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
else:
  print("The file does not exist")