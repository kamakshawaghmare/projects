def fun():
    l=[[8,3,4],
       [1,5,9],
       [6,7,2]]
    i=0
    sum1=0
    sum2=0
    sum3=0
    while i<len(l):
        j=0
        while j<len(l[i]):
            if i==0:
                sum1+=l[i][j]
            elif i==1:
                sum2+=l[i][j] 
            elif i==2: 
                sum3+=l[i][j] 
            row=sum1,sum2,sum3     
            j+=1
        i+=1
    print("row1",sum1)
    print("row2",sum2)
    print("row3",sum3) 
    print(row) 
    i=0
    sum1=0
    sum2=0
    sum3=0
    while i<len(l):
        j=0
        while j<len(l[i]):
            if j==0:
                sum1+=l[i][j]
            elif j==1:
                sum2+=l[i][j] 
            else:
                sum3+=l[i][j]
                col=sum1,sum2,sum3
            j+=1
        i+=1    
    print("col1",sum1)
    print("col2",sum2)
    print("col3",sum3)
    print(col) 
    i=0
    dright=0
    lright=0
    while i<len(l):
        j=0
        while j<len(l[i]):
            if i==j:
                dright+=l[i][j]
            if i+j==len(l[i])-1:
                lright+=l[i][j]
                d=dright,lright 
            j+=1
        i+=1
    print("right d",dright) 
    print("left d",lright) 
    if col==row and dright==lright and sum1==sum2==sum3:
        print("it is magic square") 
    else:
        print("it is not magic square")
fun()