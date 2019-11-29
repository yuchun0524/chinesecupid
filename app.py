import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine(
    states=[
        "user", 
        "menu",
        "single",
        "notsingle",
        "queen",
        "war",
        "guanyin",
        "cing"
    ],
    transitions=[
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
            "trigger": "go_back",
            "source": [
                "queen", 
                "war",
                "guanyin",
                "cing"
            ], 
            "dest": "menu"
        }
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

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
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)