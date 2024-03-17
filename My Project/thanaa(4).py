a=f1.read()
f1.close()
f2=open('out.txt','w')
counter=0
while counter < len(a) :
    if a[counter] == '/' :
        if a[counter+1] == '/':
            while a[counter]!='\n' :
                counter=counter+1        
    f2.write(a[counter])
    counter=counter+1
f2.close()

 حذف التعليقاتت
