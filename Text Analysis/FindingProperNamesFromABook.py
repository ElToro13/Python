from FSC import Userdata
from collections import Counter
import os

file_1 = open("C:\\Users\\chinkasoni\\Desktop\\ebook\\NA2.txt","r")
foo = Userdata()
file_read = file_1.read()

file_read= foo.FilterData(file_read)
file_read = file_read.replace('\'s',' ')
file_write = open("testfile4.txt","w")
file_write.write(file_read)
data=[]
names=[]
ignore=['will','what','such','much','when','that','with','have','were','been','from','they','very','them','your','this','would','could','should','their','there','which','There','These','While','Having','Gutenbergtm','Gutenberg','After','Their','not','be']

file_2 = open("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\testfile4.txt","r")
file_3 = file_2.read()
if(os.stat("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\testfile4.txt").st_size == 0):
        file_write = open("testfile4.txt",'w')
        file_write.write(file_read)
        data=[]
        file_2 = open("C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\testfile4.txt","r")
        file_3 = file_2.read()
        print('Brought to you by BackUp.dt')

datos = file_3.split()
#print(type(datos))
for i in range(0,len(datos)):
    if(len(datos[i])>3 and len(datos[i])<20):
            for k in range(0,len(ignore)):
                    if(datos[i]==ignore[k]): 
                            del datos[i]
                            datos.append('*')
                            
            #print('')
            data.append(datos[i])

i=0
for i in range(0,len(datos)):
    if(datos[i].istitle() and len(datos[i])>3 and len(datos[i])<20):
            names.append(datos[i])                    
                    
                
print('--Popular Words--')

gg = Counter(data)
print(gg.most_common(100))

print('--Popular Names--')

gg2 = Counter(names)
print(gg2.most_common(100))

#data.append(datos[i])
#datos[i].istitle() and 
