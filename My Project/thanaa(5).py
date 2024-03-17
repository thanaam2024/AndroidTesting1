string=open('inp.txt','r')
a=string.read()
string.close()

string11=open('Aft.txt','w')
i=0
while i<len (a):
    if a[i]!="\t" and a[i]!="\n" and a[i]!=" ":
        string11.write(a[i])
    i+=1
string11.close()

 سبيسات 
