import os

from linebot import LineBotApi, WebhookParser
from transitions.extensions import GraphMachine
from linebot.models import *
from utils import send_text_message
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
"""
文字訊息傳遞範例
message = TextSendMessage(text="Trigger state2")
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)
        #send_text_message(reply_token, "Trigger state2")
        self.go_back()
"""
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
# is going to #

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "開始"

    def is_going_to_single(self, event):
        text = event.message.text
        return text.lower() == "單身"

    def is_going_to_notsingle(self, event):
        text = event.message.text
        return text.lower() == "非單身"

    def is_going_to_queen(self, event):
        text = event.message.text
        return text.lower() == '單戀或曖昧中，求紅線' or text.lower() == '希望感情加溫'

    def is_going_to_war(self, event):
        text = event.message.text
        return text.lower() == '想砍掉爛桃花'

    def is_going_to_guanyin(self, event):
        text = event.message.text 
        return text.lower() == '無喜歡對象，求姻緣'
       
    def is_going_to_cing(self, event):
        text = event.message.text
        return text.lower() == '求感情復合' or  text.lower() == '求感情修復'
        
# enter #

    def on_enter_menu(self, event):
        print("I'm entering menu")
        message = TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=ButtonsTemplate(
        thumbnail_image_url='https://3.bp.blogspot.com/-3JxaP3B7Jq0/XHYDSYUtNUI/AAAAAAADRLs/FaBdkYzY5BwFlwhkZdsf3ps3nQbUqGnZACLcBGAs/s1600/1_Z40RUlwMP9bQGorLNxxfIg.png',
        title='請選擇感情狀態',
        text='本服務不會蒐集個人資料，請放心回答',
        actions=[
            MessageTemplateAction(
                label='單身',
                text='單身'
            ),
            MessageTemplateAction(
                label='非單身',
                text='非單身'
            )
        ]
    )
)
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)
        #self.go_back()

    def on_enter_single(self, event):
        print("I'm entering single")
        message = TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=ButtonsTemplate(
        thumbnail_image_url='https://3.bp.blogspot.com/-3JxaP3B7Jq0/XHYDSYUtNUI/AAAAAAADRLs/FaBdkYzY5BwFlwhkZdsf3ps3nQbUqGnZACLcBGAs/s1600/1_Z40RUlwMP9bQGorLNxxfIg.png',
        title='對月老有什麼祈求？',
        text='不同廟的月老有不同的專長，說出你的願望我能幫你選擇適合的月老喔！',
        actions=[
            MessageTemplateAction(
                label='想砍掉爛桃花',
                text='想砍掉爛桃花'
            ),
            MessageTemplateAction(
                label='求感情復合',
                text='求感情復合'
            ),
            MessageTemplateAction(
                label='無喜歡對象，求姻緣',
                text='無喜歡對象，求姻緣'
            ),
            MessageTemplateAction(
                label='單戀或曖昧中，求紅線',
                text='單戀或曖昧中，求紅線'
            )
        ]
    )
)
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)
        #self.go_back()
    
    def on_enter_notsingle(self, event):
        print("I'm entering notsingle")
        message = TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=ButtonsTemplate(
        thumbnail_image_url='https://3.bp.blogspot.com/-3JxaP3B7Jq0/XHYDSYUtNUI/AAAAAAADRLs/FaBdkYzY5BwFlwhkZdsf3ps3nQbUqGnZACLcBGAs/s1600/1_Z40RUlwMP9bQGorLNxxfIg.png',
        title='對月老有什麼祈求？',
        text='不同廟的月老有不同的專長，說出你的願望我能幫你選擇適合的月老喔！',
        actions=[
            MessageTemplateAction(
                label='想砍掉爛桃花',
                text='想砍掉爛桃花'
            ),
            MessageTemplateAction(
                label='求感情修復',
                text='求感情修復'
            ),
            MessageTemplateAction(
                label='希望感情加溫',
                text='希望感情加溫'
            )
        ]
    )
)
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def on_enter_queen(self, event):
        print("I'm entering queen")
        message = TextSendMessage(text="Trigger queen")
        message2 = TextSendMessage(text="queen")
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, [message, message2])
        #send_text_message(reply_token, "Trigger state2")
        self.go_back()
    def on_enter_war(self, event):
        print("I'm entering war")
        reply_token = event.reply_token
        send_text_message(reply_token, "war")
        self.go_back()
    def on_enter_guanyin(self, event):
        print("I'm entering guanyin")
        reply_token = event.reply_token
        send_text_message(reply_token, "guanyin")
        self.go_back()
    def on_enter_cing(self, event):
        print("I'm entering cing")
        reply_token = event.reply_token
        send_text_message(reply_token, "cing")
        self.go_back()
# exit #

    def on_exit_queen(self):
        print("Leaving queen")

    def on_exit_war(self):
        print("Leaving war")
    
    def on_exit_guantin(self):
        print("Leaving guanyin")
    
    def on_exit_cing(self):
        print("Leaving cing")
        