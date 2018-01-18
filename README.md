# currency_chatbot
## 簡介
這是一個基於Line平台的聊天機器人，主要提供匯率查詢功能，並從台灣銀行資料庫下載即時匯率資料，提供使用者便利的查詢。
## 如何安裝
您必須在Line開發者中註冊並創立一聊天機器人，再將這個專案的所有檔案部屬到有提供url與ssl連線的平台上，這邊我主要以heroku實作。同時您必須新增兩個環境變數
```
LINEBOT_CHANNEL_ACCESS_TOKEN
LINEBOT_CHANNEL_SECRET
```
裡面存放Line開發者介面提供的```CHANNEL_ACCESS_TOKEN```與```SECRET```，完成以後基本上就可以運行了。
## 執行結果
<img src="https://i.imgur.com/YCeHOFC.jpg" width="350"/>
