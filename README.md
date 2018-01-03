# Simple Telegram Bot　
> [name=倪祺婷]
```
檔案主要兩個，一個是bot.py 另一個是，Call_bind.py
State有19個
共有9個功能
```
## 功能介紹
* 傳貼圖
  - 會回傳貼圖給你，傳完直接回到第一個state
* 傳除了貼圖和文字之外的東西
  - 會傳一段文字回去，傳完直接回到第一個state
* 傳/start
  - 會回傳使用說明，傳完直接回到第一個state
* 傳/help
  - 會回傳可用的指令，傳完直接回到第一個state
* 傳/reg
  - 會回傳一張電阻計算的圖片，傳完直接回到第一個state
* 傳/song
  - 會回傳一首歌和歌詞，傳完直接回到第一個state
* 傳/game
  - 可以和bot玩猜數字遊戲，若途中輸入/exit則會回到最原本的state
* 傳/exc
  - 可以看你想要用臺幣換其他貨幣或者其他貨幣市場幣皆可
  - 若傳不合理的值則要求重新屬輸入，若途中輸入/exit則會回到最原本的state
* 傳/bconv
  - 可將十進位轉二進位，若遇負數則以二補數表示，若途中輸入/exit則會回到最原本的state
## 檔案說明
* a.py
    - 為產生fsm的圖的python檔
* 1.txt 和 1.mp3
    - 是歌曲及歌詞
* call_bind.py
    - 為建立伺服器的呼叫檔
* record.txt
    - 紀錄目前的訊息id，以免重開伺服器時吃到一堆垃圾
* res.jpg
    - 電阻計算的圖片
* bot.py
    - 執行bot的主要檔案
* ngrok.exe
    - 建立伺服器
* others
    - function to build bot

## fsm diagram
![](https://i.imgur.com/lXrZWYJ.png)