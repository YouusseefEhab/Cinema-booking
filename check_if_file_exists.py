# removing file
import os
os.remove("myfile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# create file
import os
if not os.path.exists("myfile.txt"):
  f = open("myfile.txt", "x")
  f.write("Now the file has more content!")
  f.close()
else:
  print("The file does not exist")