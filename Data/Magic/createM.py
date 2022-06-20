name="m"

M=['W','U','B','R','G']
N=['','','','','','W','U','B','R','G']
i=1
for j in range(1,9):
        for e in M:
                for f in N:
                        f2=open('../../'+name+'/'+str(i),'w')
                        s=", {"+str(j)+e+f+"} | Kreatur - "
                        f2.write(s)
                        f2.close()
                        i=i+1
                        
