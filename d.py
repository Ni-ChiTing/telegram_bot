new=""
def convertb(_in):
    global de
    global n
    global new
    n=False
    de=True
    for c in range (len(_in)):
        if((_in[c]>'9' or _in[c]<'0')and c!=0):
            de=False
        if(_in[c]=='-' and c==0):
            n=True
    if(de):
        if(n):
            temp=str(bin(-int(_in)))
            d=False
            for c in range (len(temp)-1,0,-1):
                if(d==False):
                    new=temp[c]+new
                if(d):
                    if(temp[c]=='1'):
                        new='0'+new
                    else:
                        new='1'+new
                if(d==False and temp[c]=='1'):
                    d=True
                    continue
            new='1'+new
        else:
            temp=str(bin(int(_in)))
            temp='0'+temp[2:]
            new=temp
    else:
        print("error input")
while(1):
    a=input()
    convertb(str(a))
    print(new)
