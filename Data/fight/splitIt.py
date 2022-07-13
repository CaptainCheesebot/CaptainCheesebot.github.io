name="fight"
for k in range(1,4):
        f=open(name+str(k)+'.txt','r')
        s=f.readline()
        i=1
        while(len(s)>0):
                f2=open('../../'+name+str(k)+'/'+str(i),'w')
                f2.write(s)
                f2.close()
                s=f.readline()
                i=i+1
