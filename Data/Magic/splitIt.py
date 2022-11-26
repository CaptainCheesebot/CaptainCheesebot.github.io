name="a"

f=open(name+'.txt','r')
s=f.readline()
i=1
while(len(s)>0):
        f2=open('../../'+name+'/'+str(i),'w')
        f2.write(s)
        f2.close()
        s=f.readline()
        i=i+1
