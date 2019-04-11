import random
N=1000000
p2=0
p3=0
p4=0
p5=0
for i in range(N):
    k1=random.randint(1,6)
    k2=random.randint(1,6)
    if k1>k2:
        p2+=1
    else:
        k1=random.randint(1,6)
        k2=random.randint(1,6)
        if k1>k2:
            p3+=1
        else:
            k1=random.randint(1,6)
            k2=random.randint(1,6)
            if k1>k2:
                p4+=1
            else:
                k1=random.randint(1,6)
                k2=random.randint(1,6)
                if k1>k2:
                    p5+=1
                else:
                    pass
print(p2/N)
print(p3/N)
print(p4/N)
print(p5/N)

            
        
                      
    
