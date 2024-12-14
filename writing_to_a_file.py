# a, w
# append in a file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

# Create - will create a file, returns an error if the file exist
f = open("myfile.txt", "x")
f.write("Now the file has more content!")

f.close()

# remove file
#import os
#os.remove("myfile.txt")
