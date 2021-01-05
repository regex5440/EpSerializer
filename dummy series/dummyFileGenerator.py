import os
directory=os.path.dirname(os.path.abspath(__file__))

available_files=(len(os.listdir(directory))-1)
print("\n",available_files,"samples found!")

files_required=int(input("\nNumber of sample Required: "))

files_required+=available_files

for _ in range(available_files+1, files_required+1):
    f=open(os.path.join(os.path.dirname(__file__),"file"+str(_)),"w")
    f.write("file"+str(_))
    f.close
print(files_required-available_files, "sample created!\n")
print(files_required,"total samples available!")
