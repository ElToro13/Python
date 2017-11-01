import numpy

class Userdata:
    def __init__(self, dd=""):
        self.dd = dd

    def FilterData(self, ddd=""):
        comma = [",", "?", "!", ":", ";", "/", ".", "@", "#", "$", "%", "^", "&", "*","\"","\\","_","-","(",")","\'s","[","]"] # All the characters that will be filter out
        data = []
        text = ddd
        f = list(text)
        for i in range(0,len(comma)):
            for j in range(0,len(text)):
                if(comma[i] == f[j]):
                    data.append(int(j))
        data = sorted(data)
        data2 = numpy.array(data)
        for k in range(0,len(data2)):
            del f[int(data2[k])]
            data2=data2-1

        d = ''.join(f)
        return d

    def SensorWords(self,dato=""):
        words = ['fuck', 'shit', 'bhenchod', 'madarchod','lode','chutiye','asshole','motherfucker', 'motherfucking', 'fucking', 'Fuck','fucks', 'shits', 'bhenchods', 'madarchods','lodes','chutiyes','assholes','motherfuckers', 'motherfucking', 'fucking', 'Fucks']
        data=[]
        listo = dato.split()
        for i in range(0,len(listo)):
            for j in range(0,len(words)):
                if(words[j] == listo[i]):
                    l = len(listo[i])-1
                    g = list(listo[i])
                    for j in range(1,l):
                            del g[j]
                            g.insert(j,'*')
                    j = ''.join(g)
                    del listo[i]
                    listo.insert(i,j)
        d = ' '.join(listo)
                    

        return d

    def FilterOut(self, datc=""):
        comma = ['fuck', 'shit', 'bhenchod', 'madarchod','lode','chutiye','asshole','motherfucker', 'motherfucking', 'fucking', 'Fuck','fucks', 'shits', 'bhenchods', 'madarchods','lodes','chutiyes','assholes','motherfuckers', 'motherfucking', 'fucking', 'Fucks']# All the words that will be filter out
        data = []
        text = datc
        f = text.split()
        for i in range(0,len(f)):
            for j in range(0,len(comma)):
                if(comma[j] == f[i]):
                    data.append(i)
        data = sorted(data)
        data2 = numpy.array(data)
        for k in range(0,len(data2)):
            del f[int(data2[k])]
            data2=data2-1

        d = ' '.join(f)
        return d
        
        

