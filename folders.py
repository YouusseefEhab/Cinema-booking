import os
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
else:
    print("myfolder already exist")

import os
os.rmdir("myfolder")

# create folder in specific path
directory = "GeeksforGeeks"

# Parent Directory path
parent_dir = "try"

# Path
path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
    os.makedirs(path)

# creating file
f = open(os.path.join(path, "myfile.txt"), "x")
f.write("Now the file has more content!")
f.close()
