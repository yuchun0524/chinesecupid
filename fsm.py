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
        if event.type == 'message':
            text = event.message.text
            return text.lower() == "開始"
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "return"

    def is_going_to_single(self, event):
        if event.type == 'message':
            text = event.message.text
            return text.lower() == "單身"
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "single"

    def is_going_to_notsingle(self, event):
        if event.type == 'message':
            text = event.message.text   
            return text.lower() == "非單身"
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "not_single" 

    def is_going_to_queen(self, event):
        if event.type == 'message':
            text = event.message.text
            return text.lower() == '單戀或曖昧中，求紅線' or text.lower() == '希望感情加溫'
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "lovesomeone" or text.lower() == "warm" or text.lower() == "queen_return"

    def is_going_to_war(self, event):
        if event.type == 'message':
            text = event.message.text
            return text.lower() == '想砍掉爛桃花'
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "bad"    

    def is_going_to_guanyin(self, event):
        if event.type == 'message':
            text = event.message.text 
            return text.lower() == '無喜歡對象，求姻緣'
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "none"
       
    def is_going_to_cing(self, event):
        if event.type == 'message':
            text = event.message.text
            return text.lower() == '求感情復合' or  text.lower() == '求感情修復'
        elif event.type == 'postback':
            text = event.postback.data
            return text.lower() == "again" or text.lower() == "fix"
    def is_going_to_location(self, event):
        text = event.postback.data
        return text.lower() == "queen_location"    
    def is_going_to_time(self, event):
        text = event.postback.data
        return text.lower() == "queen_time"
    def is_going_to_phone(self, event):
        text = event.postback.data
        return text.lower() == "queen_phone"
    def is_going_to_draw(self, event):
        text = event.postback.data
        return text.lower() == "queen_draw"
    def is_going_to_notice(self, event):
        text = event.postback.data
        return text.lower() == "queen_notice" 

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
            PostbackAction(
                label='單身',
                data='single'
            ),
            PostbackAction(
                label='非單身',
                data='not_single'
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
            PostbackAction(
                label='想砍掉爛桃花',
                data='bad'
            ),
            PostbackAction(
                label='求感情復合',
                data='again'
            ),
            PostbackAction(
                label='無喜歡對象，求姻緣',
                data='none'
            ),
            PostbackAction(
                label='單戀或曖昧中，求紅線',
                data='lovesomeone'
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
            PostbackAction(
                label='想砍掉爛桃花',
                data='bad'
            ),
            PostbackAction(
                label='求感情修復',
                data='fix'
            ),
            PostbackAction(
                label='希望感情加溫',
                data='warm'
            )
        ]
    )
)
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def on_enter_queen(self, event):
        print("I'm entering queen")
        Carousel= TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                #thumbnail_image_url='顯示在開頭的大圖片網址',
                title='大天后宮',
                text='你適合的是大天后宮，它是國定一級古蹟，起源於明鄭時期，目前是台灣規模數一數二的媽祖廟。',
                actions=[
                    PostbackAction(
                        label='位置',
                        data='queen_location'
                    ),
                    PostbackAction(
                        label='開放時間',
                        data='queen_time'
                    ),
                    PostbackAction(
                        label='聯絡方式',
                        data='queen_phone'
                    )
                ]
            ),
            CarouselColumn(
                #thumbnail_image_url='顯示在開頭的大圖片網址',
                title='大天后宮',
                text='據說本廟月老的專長是為愛情加溫和牽紅線，如果有明確對象，可以到大天后宮求月老紅線。',
                actions=[
                    PostbackAction(
                        label='抽籤流程',
                        data='queen_draw'
                    ),
                    PostbackAction(
                        label='注意事項',
                        data='queen_notice'
                    ),
                    PostbackAction(
                        label='返回',
                        data='return'
                    )
                ]
            )
        ]
    )
    )
        #message = TextSendMessage(text="Trigger queen")
        #message2 = TextSendMessage(text="queen")
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, Carousel)
        #send_text_message(reply_token, "Trigger state2")
        #self.go_back()
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
    def on_enter_location(self, event):
        print("I'm entering location")
        if event.postback.data == "queen_location":
            location = LocationSendMessage(
                title='大天后宮地址',
                address='台南市中西區永福路二段227巷18號',
                latitude=22.996434,
                longitude=120.201710
            )
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊返回即可查看更多資訊',
                    text='可返回原先介面',
                    actions=[
                        PostbackAction(
                            label='返回',
                            data='queen_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        """line_bot_api.push_message('U06538a5ba60fdf5d470b458296993e3d', location)
        line_bot_api.reply_message(reply_token, button)"""
        line_bot_api.reply_message(reply_token, [location,button])
    def on_enter_time(self, event):
        print("I'm entering time")
        if event.postback.data == "queen_time":
            message = TextSendMessage(text = '大天后宮開放時間：\n早上六點到晚上九點')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊返回即可查看更多資訊',
                    text='可返回原先介面',
                    actions=[
                        PostbackAction(
                            label='返回',
                            data='queen_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, [message, button])
    def on_enter_phone(self, event):
        print("I'm entering phone")
        if event.postback.data == "queen_phone":
            message = TextSendMessage(text = '大天后宮聯絡方式：\n電話：06-2227194、06-2211178')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊返回即可查看更多資訊',
                    text='可返回原先介面',
                    actions=[
                        PostbackAction(
                            label='返回',
                            data='queen_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, [message, button])   
    def on_enter_draw(self, event):
        print("I'm entering draw")
        if event.postback.data == "queen_draw":
            message = TextSendMessage(text = '抽籤流程：\n1、先向月老上香，並稟明個人資料以及想請示的感情問題。\n2、祈畢插香，持筊過爐三圈淨化，懇請月老賜籤，接著擲筊；若得聖筊，才可繼續求籤。\n3、接著連續擲筊三次，由其顯示的筊型，可得相對應的籤詩。\n4、取籤之後，可自行翻閱籤詩本解籤或請廟方人員解籤。\n\n提醒：此為簡單概述，詳細情形請依廟內規定或洽詢廟方人員。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊返回即可查看更多資訊',
                    text='可返回原先介面',
                    actions=[
                        PostbackAction(
                            label='返回',
                            data='queen_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, [message, button]) 
    def on_enter_notice(self, event):
        print("I'm entering notice")
        if event.postback.data == "queen_notice":
            message = TextSendMessage(text = '注意事項：\n1、在寺廟中要先拜主神再拜月老。\n2、多處廟方人員表示，求月老只能求一家，請自行斟酌。\n3、月老只是協助，重點還是在個人造化。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊返回即可查看更多資訊',
                    text='可返回原先介面',
                    actions=[
                        PostbackAction(
                            label='返回',
                            data='queen_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, [message, button]) 
    
# exit #

    def on_exit_queen(self, event):
        print("Leaving queen")

    def on_exit_war(self, event):
        print("Leaving war")
    
    def on_exit_guantin(self, event):
        print("Leaving guanyin")
    
    def on_exit_cing(self, event):
        print("Leaving cing")

    def on_exit_location(self, event):
        print("Leaving location")

    def on_exit_time(self, event):
        print("Leaving time")

    def on_exit_phone(self, event):
        print("Leaving phone")

    def on_exit_draw(self, event):
        print("Leaving draw")

    def on_exit_notice(self, event):
        print("Leaving notice")

    def on_exit_return(self, event):
        print("Leaving return")
        