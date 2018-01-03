import telegram
#bot='https://api.telegram.org/bot529449700:AAG6dcqs0NaI2Od1pefXfpJEFG1eoEbBzqM/'
#webhook='https://53592887.ngrok.io'
#bot = telegram.Bot(token='529449700:AAG6dcqs0NaI2Od1pefXfpJEFG1eoEbBzqM')
#bot.deleteWebhook()
import  sys
import random
import  telegram 
from  flask  import  Flask ,  request
import requests
from bs4 import BeautifulSoup
import subprocess
import json
import time
app  =  Flask ( __name__ ) 
bot  =  telegram . Bot (token='529449700:AAG6dcqs0NaI2Od1pefXfpJEFG1eoEbBzqM' )
text=None
mes_id=0
chat_id=0
state=0
bi=False
de=False
low=0
up=0
num=0
country=[]
c=[]
data=[]
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"
ini="This bot have some functions\n\n if you want a song type /song \n\n if you want binary to decimal type  /bconv\n\n if you want play number game type /game \n\n if you want to find resistance table type /res\n\n if you want to exchang NTD to other currency type /exc "
cur=""
NTD=[]
port=0
choose=0
def geuss(g):
    global num
    global up
    global low
    if(g>num and g<up):
        up=g
    elif(g<num and g>low):
        low=g
    return " guess a number between "+str(low)+" and "+str(up)+" \n\n(if want to quit type /exit)"
def worm():
    global url
    global data
    global country
    global cur
    global NTD
    get=requests.get(url)
    soup=BeautifulSoup(get.text,'html.parser')
    rows=soup.find('table','table').tbody.find_all('tr')
    data1=[]
    for row in rows:
        data1.append([s for s in row.stripped_strings])
    for a in range (len(data1)):
        c.append(data1[a][0])
        country.append(("("+str(a)+") "+data1[a][0]))
        cur=cur+country[a]+"\n"
        data.append(data1[a][3])
        NTD.append(data1[a][2])
def  _set_webhook ():
    p=subprocess.Popen(r'ngrok.exe http -bind-tls=true 5000')
    global port
    time.sleep(3) # to allow the ngrok to fetch the url from the server
    port=input()
    localhost_url = "http://localhost:"+str(port)+"/api/tunnels" #Url with tunnel details
    tunnel_url = requests.get(localhost_url).text #Get the tunnel information
    j = json.loads(tunnel_url)
    print(j['tunnels'][0]['public_url'])
    status  =  bot . set_webhook ( j['tunnels'][0]['public_url']+'/hook' ) 
    if  not  status : 
        print ( 'Webhook setup failed' ) 
        sys . exit ( 1 )

def getlastmesg():
    f=open('record.txt','r')
    global mes_id
    a=f.read()
    if(str.isnumeric(a)):
        mes_id=int(a)
    else:
        mes_id=0
    f.close()
def write_mes_id():
    f=open('record.txt','w')
    global mes_id
    f.write(str(mes_id))
    f.close()
def convertb(_in):
    global de
    global n
    n=False
    new=""
    if(_in[0]=='-' ):
        n=True
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
        new='first bit is sign bit '+'1'+new
    else:
        temp=str(bin(int(_in)))
        temp='first bit is sign bit '+'0'+temp[2:]
        new=temp
    return new
@app.route ( '/hook' ,  methods = [ 'POST' ]) 
def  webhook_handler ():
    global mes_id
    global chat_id
    global bot
    global state
    global low
    global up
    global num
    global choose
    if  request . method  ==  "POST" : 
        update  =  telegram . Update . de_json ( request . get_json ( force = True ),  bot )
        print(update.message.message_id)
        if(mes_id<update.message.message_id):
            mes_id=update.message.message_id
            chat_id=update.message.chat_id
            write_mes_id();
            if(update.message.text is not None):
                if(update.message.text=="/start" and state==0):
                   update . message . reply_text( "Welcom to my bot ,this bot can do somthing\nyou can type /help to understand")
                   state=0
                elif(update.message.text=="/help" and state==0):
                    update . message . reply_text(ini)
                    state=0
                elif(update.message.text=="/res" and state==0):
                    bot.send_photo(chat_id,photo=open('res.jpg','rb'))
                    state=0
                elif(update.message.text=="/song" and state==0 ):
                    update . message . reply_text("Wait for minutes")
                    d=open('1.txt','r')
                    r=d.read()
                    update . message . reply_text(str(r))
                    d.close()
                    bot.send_audio(chat_id,audio=open('1.mp3','rb'))
                    state=0
                elif(update.message.text=="/bconv" and state==0):
                    update . message . reply_text("input decimal number \n\n(if want to quit type /exit)")
                    state=1;
                elif(update.message.text=="/game" and state==0):
                    update . message . reply_text("we start a game , and input upper bound \n\n(if want to quit type /exit) ")
                    state=2;
                elif(state==2 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        up=0
                        low=0
                        if(str.isnumeric(update.message.text)):
                            state=3
                            up=int(update.message.text)
                            update . message . reply_text(" input lower bound\n\n (if want to quit type /exit)")
                        else:
                            state=2
                            update . message . reply_text("input a number!!")
                elif(state==3 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            low=int(update.message.text)
                            if(low>=up):
                                state=2
                                update . message . reply_text("(lower need to small than upper input upper bound \n\n(if want to quit type /exit)")
                            else:
                                state=4
                                num=random.randrange(low,up,1)
                                print(num)
                                update . message . reply_text(" guess a number between "+str(low)+" and "+str(up)+" \n\n(if want to quit type /exit)")
                        else:
                            state=3
                            update . message . reply_text("input a number!!")
                elif(state==4 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            if(num==int(update.message.text)):
                                update . message . reply_text("you find the number the number is "+update.message.text+"\nyou can look up /help and doing something") 
                                state=0
                                
                            else:   
                                update . message . reply_text(geuss(int(update.message.text)))
                        else:
                            update . message . reply_text("input a number!!")
                            
                            
                elif(state==1 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            state=0
                            update . message . reply_text(ini)
                            update . message . reply_text(convertb(update.message.text))
                        else:
                            state=1
                            update . message . reply_text("input a number!!")
                elif(update.message.text=="/exc" and state==0):
                    update . message . reply_text("匯率換算!!!\n\n若台幣兌換其他貨幣輸入1,若其他貨幣兌換台幣輸入2"+" \n\n(if want to quit type /exit)")
                    state=5
                elif(state==5 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(update.message.text=='1'):
                            state=6
                            update . message . reply_text('選擇所要換貨幣(輸入括號內數字)'+cur+" \n\n(if want to quit type /exit)")
                        elif(update.message.text=='2'):
                            state=7
                            update . message . reply_text('選擇所要換貨幣(輸入括號內數字)'+cur+" \n\n(if want to quit type /exit)")
                        else:
                            state=5
                            update . message . reply_text("輸入錯誤！！"+"匯率換算!!!\n\n若台幣兌換其他貨幣輸入1,若其他貨幣兌換台幣輸入2"+" \n\n(if want to quit type /exit)")
                elif(state==6 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            choose=int(update.message.text)
                            if(choose>18 or choose<0):
                               update . message . reply_text("輸入錯誤！！\n"+'選擇所要換貨幣(輸入括號內數字)'+cur+" \n\n(if want to quit type /exit)")
                               state=6
                            else:
                                state=8
                                update . message . reply_text("輸入你所擁有的台幣")
                        else:
                            state=6
                            update . message . reply_text("輸入錯誤！！\n"+'選擇所要換貨幣(輸入括號內數字)'+cur+" \n\n(if want to quit type /exit)")
                elif(state==8 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            a=int(update.message.text)
                            if(a<0):
                                update . message . reply_text("輸入錯誤,不能是負數！！\n"+"輸入你所擁有的台幣")
                                state=8
                            else:
                                state=0
                                update . message . reply_text("共 "+str(a/float(data[choose]))+" "+c[choose])
                                update . message . reply_text(ini)
                            
                        else:
                            state=8
                            update . message . reply_text("輸入錯誤！！\n"+'選擇所要換貨幣(輸入括號內數字)\n'+cur+" \n\n(if want to quit type /exit)")
                elif(state==7 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            choose=int(update.message.text)
                            if(choose>18 or choose<0):
                               update . message . reply_text("輸入錯誤！！\n"+'選擇所要換貨幣(輸入括號內數字)\n'+cur+" \n\n(if want to quit type /exit)")
                               state=7
                            else:
                                state=9
                                update . message . reply_text("輸入你所擁有的"+c[choose])
                        else:
                            state=6
                            update . message . reply_text("輸入錯誤！！\n"+'選擇所要換貨幣(輸入括號內數字)\n'+cur+" \n\n(if want to quit type /exit)")
                elif(state==9 and update.message.text is not None):
                    if(update.message.text=="/exit"):
                        state=0
                        update . message . reply_text(ini)
                    else:
                        if(str.isnumeric(update.message.text)):
                            a=int(update.message.text)
                            if(a<0):
                                update . message . reply_text("輸入錯誤,不能是負數！！\n"+"輸入你所擁有的"+c[choose])
                                state=9
                            else:
                                state=0
                                update . message . reply_text("共 "+str(a*float(NTD[choose]))+" 台幣")
                                update . message . reply_text(ini)
                            
                        else:
                            state=9
                            update . message . reply_text("輸入錯誤！！\n"+'選擇所要換貨幣(輸入括號內數字)\n'+cur+" \n\n(if want to quit type /exit)")
            elif(update.message.sticker is not None):
                update . message .reply_sticker(update.message .sticker)
            else:
                update . message . reply_text("I know you give me somthing but I don't want to reply you")
            
        else:
            print("old")
     
    return  'ok'

if  __name__  ==  "__main__" :
    _set_webhook ()
    getlastmesg()
    worm()
    state=0;
    app . run ()
