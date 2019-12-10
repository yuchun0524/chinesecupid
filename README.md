# Chinese cupid
## 說明
這個聊天機器人可以幫助你找到適合的月老

## 功能
藉由詢問兩個問題來找出適合使用者的月老，目前只有列出府城四大月老

四大月老分別是大天后宮、祀典武廟、大觀音亭和重慶寺的月老

每間廟都會有自己的選單，選單會有兩個部分，左邊會有廟的照片及關於該廟的概述、右邊則是該廟月老的照片及關於該月老的簡述，選單功能包含
* 位置
* 開放時間
* 聯絡方式
* 流程(求籤、求紅線流程等等)
* 注意事項
* 返回首頁

## 特別功能
* 每個連進 Bot 的用戶都有獨立的 machine
一開始`我要問事`按鈕的actions是MessageAction，也就是使用者點選後會送出訊息，藉由使用者送出訊息來取得使用者的id，就可以為不同的使用者建立不同的machine
## Finite State Machine
![fsm](./fsm.png)
* **`user`**：列出歡迎訊息和`我要問事`按鈕，廟宇選單中的返回首頁是用postback的方式回到該狀態
* **`menu`**：列出詢問感情狀態的按鈕，收到特定text之後會進入該狀態
***
* **`single` **：詢問單身使用者有什麼祈求，使用者在`menu`按下按鈕後會用postback的方式進來此狀態
* **`notsingle`**：詢問非單身使用者有什麼祈求，使用者在`menu`按下按鈕後會用postback的方式進入此狀態
***
* **`queen`**：列出大天后宮選單
* **`war`**：列出祀典武廟選單
* **`guanyin`**：列出大觀音亭選單
* **`cing`**：列出大觀音亭選單
* **`location`**：會送出location message和返回button，根據不同的postback來決定要回應哪間廟的位置
* **`time`**：會送出時間的message和返回button，根據不同的postback來決定要回應哪間廟的開放時間
* **`phone`**：會送出電話的message和返回button，根據不同的postback來決定要回應哪間廟的聯絡方式
* **`draw`**：會送出流程的message和返回button，根據不同的postback來決定要回應哪間廟求籤、求紅線或是攪醋矸流程
* **`notice`**：會送出注意事項的message和返回button，根據不同的postback來決定要回應哪間廟的注意事項，只有重慶寺的不同，其他三間廟的是一樣的
## Usage
The initial state is set to `user`.

一開始會有歡迎訊息和`我要問事`按鈕

點選按鈕之後會進入`menu`state，根據選項不同會分別進入`single`和`notsingle`state

`single`和`notsingle`state會根據選項不同分別進入`queen`、`war`、`guanyin`和`cing`state

這四個state代表不同廟宇，分別是大天后宮、祀典武廟、大觀音亭和重慶寺

四個不同的state有不同的選單，選單可查看廟宇資訊，廟宇資訊有`位置`、`開放時間`、`聯絡方式`、`流程`和`注意事項`

另外有在廟宇主選單設置`返回首頁`按鈕，按下即可回到一開始的`user`state，會呈現歡迎繼續使用的訊息

## Demo畫面
### **一開始的畫面**
![fsm](./img/start.png)
### **點選我要問事之後**
![fsm](./img/menu.png)
### **點選單身之後的畫面**
![fsm](./img/single.png)
### **點選非單身之後的畫面**
![fsm](./img/notsingle.png)
### **大天后宮主選單**
![fsm](./img/temple.png)
### **祀典武廟主選單**
![fsm](./img/war.png)
### **大觀音亭主選單**
![fsm](./img/guanyin.png)
### **重慶寺主選單**
![fsm](./img/cing.png)
### **點選返回首頁之後會回到一開始的畫面**
![fsm](./img/continue.png)
