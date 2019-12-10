import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import * #MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = { #TocMachine(
    "states" : [
        'user', 
        'menu',
        'single',
        'notsingle',
        'queen',
        'war',
        'guanyin',
        'cing',
        'location',
        'time',
        'phone',
        'draw',
        'notice'
    ],
    "transitions": [
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "single",
            "conditions": "is_going_to_single",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "notsingle",
            "conditions": "is_going_to_notsingle",
        },
        {
            "trigger": "advance",
            "source": ["single", "notsingle"],
            "dest": "queen",
            "conditions": "is_going_to_queen",
        },
        {
            "trigger": "advance",
            "source": ["single", "notsingle"],
            "dest": "war",
            "conditions": "is_going_to_war",
        },
        {
            "trigger": "advance",
            "source": "single",
            "dest": "guanyin",
            "conditions": "is_going_to_guanyin",
        },
        {
            "trigger": "advance",
            "source": ["single", "notsingle"],
            "dest": "cing",
            "conditions": "is_going_to_cing",
        },
        {
            "trigger": "advance",
            "source": ["queen", "war", "guanyin", "cing"],
            "dest": "location",
            "conditions": "is_going_to_location",
        },
        {
            "trigger": "advance",
            "source": ["queen", "war", "guanyin", "cing"],
            "dest": "time",
            "conditions": "is_going_to_time",
        },
        {
            "trigger": "advance",
            "source": ["queen", "war", "guanyin", "cing"],
            "dest": "phone",
            "conditions": "is_going_to_phone",
        },
        {
            "trigger": "advance",
            "source": ["queen", "war", "guanyin", "cing"],
            "dest": "draw",
            "conditions": "is_going_to_draw",
        },
        {
            "trigger": "advance",
            "source": ["queen", "war", "guanyin", "cing"],
            "dest": "notice",
            "conditions": "is_going_to_notice",
        },
        {
            "trigger": "advance",
            "source":["location", "time", "phone", "draw", "notice"],
            "dest": "queen",
            "conditions": "back_to_queen",
        },
        {
            "trigger": "advance",
            "source": ["location", "time", "phone", "draw", "notice"],
            "dest": "war",
            "conditions": "back_to_war",
        },
        {
            "trigger": "advance",
            "source": ["location", "time", "phone", "draw", "notice"],
            "dest": "guanyin",
            "conditions": "back_to_guanyin",
        },
        {
            "trigger": "advance",
            "source": ["location", "time", "phone", "draw", "notice"],
            "dest": "cing",
            "conditions": "back_to_cing",
        },
        {
            "trigger": "advance",
            "source": ["queen", "war", "guanyin", "cing"], 
            "dest": "user",
            "conditions": "back_to_user",
        },
    ],
    "initial":"user",
    "auto_transitions":False,
    "show_conditions":True,
}

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

"""try:
    line_bot_api.push_message('U06538a5ba60fdf5d470b458296993e3d', TextSendMessage(text='想拜月老卻不知道該拜哪一間嗎？讓我來幫助你吧！請輸入開始以便使用本服務'))
    except LineBotApiError as e:
    error handle
    raise e"""
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        text = event.message.text
        if text == 'test':
            line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text = "test success")
            )
        else:
            line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
            )

    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)       
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        
        if isinstance(event, FollowEvent):
            message = TextSendMessage(text = '歡迎使用本服務~~\n想拜月老卻不知道該拜哪一間嗎？讓我來幫助你吧！請點選「我要問事」以便使用本服務。\n溫馨小提醒：沒有規定一定要拜某一間廟的月老，以下提供的資訊只是幫助你更快做出選擇。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    text='點擊下方按鈕即可開始使用',
                    actions=[
                        MessageAction(
                            label='我要問事',
                            text='我要問事'
                        )
                    ]
                )
            )
            reply_token = event.reply_token
            line_bot_api.reply_message(reply_token, [message, button])
        if not isinstance(event, MessageEvent) and not isinstance(event, PostbackEvent):
            continue
        if isinstance(event, MessageEvent) and isinstance(event.message, StickerMessage):
            message = StickerSendMessage(package_id='2', sticker_id='172')
            reply_token = event.reply_token
            line_bot_api.reply_message(reply_token, message)
        if isinstance(event, MessageEvent) and (not isinstance(event.message, TextMessage)):
            continue
        if isinstance(event, MessageEvent) and (not isinstance(event.message.text, str)):
            continue
        if isinstance(event, MessageEvent) and isinstance(event.message.text, str):
            if event.source.user_id not in machine:
                machine[event.source.user_id] = TocMachine(
                    states = machine["states"],
                    transitions = machine["transitions"],
                    initial = machine["initial"],
                    auto_transitions = machine["auto_transitions"],
                    show_conditions = machine["show_conditions"],
                )
        print(f"\nFSM STATE: {machine[event.source.user_id].state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine[event.source.user_id].advance(event)
        if response == False:
            send_text_message(event.reply_token, "我去幫忙月老啦！請你再試試看別的選項。要不要試試按返回什麼主選單呢？\n小提示：在廟宇選單內按下返回首頁可以回到一開始的歡迎訊息喔！")

    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    if "graph" not in machine:
        machine["graph"] = TocMachine(
            states = machine["states"],
            transitions = machine["transitions"],
            initial = machine["initial"],
             auto_transitions = machine["auto_transitions"],
            show_conditions = machine["show_conditions"],
            )
    machine["graph"].get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)