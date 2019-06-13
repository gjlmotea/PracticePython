#需將file.dat 與 read_file.py放到同一個資料夾

fileObj = open("file.dat","r", encoding="utf-8")

for line in fileObj:
    print(line, end='')
    
fileObj.close()
