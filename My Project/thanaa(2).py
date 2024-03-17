key=['cout','cin','using','namespace','int','long','double','char','string','float','main','include','std','iostream','if','for',]
op=['+','-','*','^','/','=','<','>','>>','<<']
sy=['#','(',')',';','{','}','[',']']
f1=open('in.txt','r')
a=f1.read()
f1.close()
f2=open('out.txt','w')
text=''
for line in a:
    if line!='\n':
        text=text+line
j='';z='';m='';n=''
for i in range(len(text)):
    if not(text[i]in op)and not( text[i]in sy )and not(text[i].isspace())and not(text[i].isnumeric())and text[i]!='':
        j=j+text[i]
    elif (  text[i]in sy or text[i]in op or text[i].isspace() )and j!='':
        if j in key:
            f2.write(j+'_____ keyword\n')
            j='' 
        else:
            f2.write(j+'______identifire\n')
            j='' 
    if text[i]in op:
        z=z+text[i]
    else:
        if z in op:
            f2.write(z+'_____ operator\n')
            z=''
    if text[i]in sy:
        m=m+text[i]
    else:
        if m in sy:
             f2.write(m+'_______Symbol\n')
             m=''
    if text[i].isnumeric()or text[i]=='':
        n=n+text[i]
    elif(text[i] in sy or text[i]in op or text[i] in op or text[i].isspace()or text[i]in key or text[i]=='\n') and n!='':
        f2.write(n+'______numeric\n')
        n=''  
f2.close()
