f1=open('input.txt','r')
a=f1.read()
f1.close()
f2=open('output.txt','w')
i=1
Name=[]
Value=[]
while i < len(a):
    if a[i]=='#' and a[i+1]=='d' and a[i+2]=='e'and a[i+3]=='f'and a[i+4]=='i'and a[i+5]=='n'and a[i+6]=='e':
        i=i+8
        while  a[i] != ' ':
            Name.append(a[i])
            i=i+1
        i=i+1
        while  a[i] != '\n':
            Value.append(a[i])
            i=i+1
        i=i+1
    x=i
    s=0
    for q in range(0,len(Name)):
        if Name[q]==a[x] :
            x=x+1
        else :
            s=1
    if s==0 :
        for q in range(0,len(Value)):
            f2.write(Value[q])
        for q in range(0,len(Name)):
            i=i+1
    f2.write(a[i])
    i=i+1
f2.close()

define او القيمة الثابتة
