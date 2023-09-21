p=1
for i in range(1,6):
    for j in range(1,6):
        
        if(j<=i):
            if(i%2==0):
                print(p,end='')
                p+=1
                
            else:
                k=ord('@')+p
                print(chr(k),end='')
                p+=1
                
        else:
            print("",end='')
    print()

