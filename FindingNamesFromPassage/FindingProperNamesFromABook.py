from FSC import Userdata
from collections import Counter

file_1 = open("C:\\Users\\chinkasoni\\Desktop\\testytest.txt","r")  # Path of txt file of the book
foo = Userdata()
file_read = file_1.read()

file_read= foo.FilterData(file_read)
file_write = open("testfile3.txt","w")
file_write.write(file_read)
data=[]
file_2 = open("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\testfile2.txt","r") # Python Directory
file_3 = file_2.read()
if(os.stat("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\testfile4.txt").st_size == 0):
        file_write = open("testfile4.txt",'w')
        file_write.write(file_read)
        data=[]
        file_2 = open("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\testfile4.txt","r")
        file_3 = file_2.read()

datos = file_3.split()
for i in range(0,len(datos)):
	if(datos[i].istitle() and len(datos[i])>4 and len(datos[i])<20):
		data.append(datos[i])
		
print(Counter(data))
