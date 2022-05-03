

fil=open('output.txt','r').readlines()


for i in fil:
    flag2=''
    try:
        for j in range(8):
            if j %2==0:
                flag2+=str(int(i[j])^0x0)
            else:
                flag2+=str(int(i[j])^0x1)
    except:
        print()
    print(chr(int(flag2,2)),end='')
    
    

    
    

    