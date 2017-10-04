import numpy

comma = [",", "?", "!", ":", ";", "/", ".", "@", "#", "$", "%", "^", "&", "*"] # All the characters that will be filter out
data = []
text = input("Ask me something: \n")

f = list(text)

for i in range(0, len(comma)):
    for j in range(0, len(text)):
        if(comma[i] == f[j]):
            data.append(int(j))
         
data = sorted(data)
data2 = numpy.array(data)

for k in range(0, len(data2)):
    del f[int(data2[k])]
    data2 = data2 - 1


d = ''.join(f)
print(d)
