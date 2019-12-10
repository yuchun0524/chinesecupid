# Chinese cupid
## 說明
這個聊天機器人可以幫助你找到適合的月老
## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.



## 功能
藉由詢問兩個問題來找出適合使用者的月老，此處只有列出台南中西區有名的四大月老

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
* **`single` 單身**：列出詢問使用者有什麼祈求的按鈕，使用者在`menu`按下按鈕後會用postback的方式進來此狀態
* **`notsingle`非單身**：列出詢問使用者有什麼祈求的按鈕，使用者在`menu`按下按鈕後會用postback的方式進入此狀態
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


* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"
## Demo畫面
* 一開始的畫面
![fsm](./img/start.png)
* 點選我要問事之後
![fsm](./img/menu.png)
* 點選單身之後的畫面
![fsm](./img/single.png)
* 廟宇主選單
![fsm](./img/temple.png)
* 點選返回首頁之後會回到一開始的狀態
![fsm](./img/continue.png)

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
