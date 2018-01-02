import requests
from bs4 import BeautifulSoup
data=[]
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"
get=requests.get(url)
soup=BeautifulSoup(get.text,'html.parser')
rows=soup.find('table','table').tbody.find_all('tr')
for row in rows:
    data.append([s for s in row.stripped_strings])
   
print(data)
