import os

from linebot import LineBotApi, WebhookParser
from transitions.extensions import GraphMachine
from linebot.models import *
from utils import send_text_message
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
# is going to #
    def back_to_user(self, event):
        if event.type == 'postback':
            text = event.postback.data
            return text.lower() == "return"

    def is_going_to_menu(self, event):
        if event.type == 'message':
            text = event.message.text
            return text.lower() == "我要問事"

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
            return text.lower() == "lovesomeone" or text.lower() == "warm" 

    def back_to_queen(self, event):
        if event.type == 'postback':
            text = event.postback.data
            return text.lower() == "queen_return"

    def back_to_war(self, event):
        if event.type == 'postback':
            text = event.postback.data
            return text.lower() == "war_return"
    
    def back_to_guanyin(self, event):
        if event.type == 'postback':
            text = event.postback.data
            return text.lower() == "guanyin_return"

    def back_to_cing(self, event):
        if event.type == 'postback':
            text = event.postback.data
            return text.lower() == "cing_return"  

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
        return text.lower() == "queen_location" or text.lower() == "war_location" or text.lower() == "guanyin_location" or text.lower() == "cing_location"
    
    def is_going_to_time(self, event):
        text = event.postback.data
        return text.lower() == "queen_time" or text.lower() == "war_time" or text.lower() == "guanyin_time" or text.lower() == "cing_time"
    
    def is_going_to_phone(self, event):
        text = event.postback.data
        return text.lower() == "queen_phone" or text.lower() == "war_phone" or text.lower() == "guanyin_phone" or text.lower() == "cing_phone"
    
    def is_going_to_draw(self, event):
        text = event.postback.data
        return text.lower() == "queen_draw" or text.lower() == "war_draw" or text.lower() == "guanyin_draw" or text.lower() == "cing_draw"
    
    def is_going_to_notice(self, event):
        text = event.postback.data
        return text.lower() == "queen_notice" or text.lower() == "war_notice" or text.lower() == "guanyin_notice" or text.lower() == "cing_notice"

# enter #
    def on_enter_user(self, event):
        print("I'm entering user")
        message = TextSendMessage(text = '歡迎繼續使用本服務\n想拜月老卻不知道該拜哪一間嗎？讓我來幫助你吧！請輸入「我要問事」以便使用本服務。\n\n溫馨小提醒：以下提供的資訊只是幫助你能夠更快做出選擇。')
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)
    def on_enter_menu(self, event):
        print("I'm entering menu")
        message = TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=ButtonsTemplate(
        thumbnail_image_url='https://3.bp.blogspot.com/-3JxaP3B7Jq0/XHYDSYUtNUI/AAAAAAADRLs/FaBdkYzY5BwFlwhkZdsf3ps3nQbUqGnZACLcBGAs/s1600/1_Z40RUlwMP9bQGorLNxxfIg.png',
        title='請選擇感情狀態',
        text='沒有一言難盡的選項喔！',
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
        #thumbnail_image_url='https://blog.accupass.com/wp-content/uploads/2017/08/000000000002-768x516.jpg',
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
                thumbnail_image_url='https://2.bp.blogspot.com/-MBB02c7m240/W12Y6Yk7RiI/AAAAAAAACkY/X3SS1KsgYUE7oNKHG3hPtZ8y5oafpuwkQCLcBGAs/s1600/%25E5%25A4%25A7%25E5%25A4%25A9%25E5%2590%258E%25E5%25AE%25AE.png',
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
                thumbnail_image_url='https://blog.accupass.com/wp-content/uploads/2017/08/000000000002-768x516.jpg',
                #thumbnail_image_url='https://2.bp.blogspot.com/-MBB02c7m240/W12Y6Yk7RiI/AAAAAAAACkY/X3SS1KsgYUE7oNKHG3hPtZ8y5oafpuwkQCLcBGAs/s1600/%25E5%25A4%25A7%25E5%25A4%25A9%25E5%2590%258E%25E5%25AE%25AE.png',
                title='大天后宮',
                text='本廟月老的專長是為愛情加溫和牽紅線，如果有明確對象，可以到大天后宮求月老紅線。',
                actions=[
                    PostbackAction(
                        label='求籤流程',
                        data='queen_draw'
                    ),
                    PostbackAction(
                        label='注意事項',
                        data='queen_notice'
                    ),
                    PostbackAction(
                        label='返回首頁',
                        data='return'
                    )
                ]
            )
        ]
    )
    )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, Carousel)

    def on_enter_war(self, event):
        print("I'm entering war")
        Carousel= TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                #thumbnail_image_url='https://blog.accupass.com/wp-content/uploads/2017/08/e14db151308ad410ad859e6545a8d0f5.jpg',
                thumbnail_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t31.0-8/859031_1099317400081235_8660042414913866148_o.jpg?_nc_cat=109&_nc_ohc=oCTAlch7OWwAQmXNpErna_bxzlgLKa-lMxDU-G37vfvEudliENCNFOwZw&_nc_ht=scontent.fkhh1-2.fna&oh=8592fbad55c4a08e7340967498061326&oe=5E715B0A',
                title='祀典武廟',
                text='你適合的是祀典武廟，它是國家一級古蹟，起源於明鄭時期，主要奉祀關聖帝君。',
                actions=[
                    PostbackAction(
                        label='位置',
                        data='war_location'
                    ),
                    PostbackAction(
                        label='開放時間',
                        data='war_time'
                    ),
                    PostbackAction(
                        label='聯絡方式',
                        data='war_phone'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://blog.accupass.com/wp-content/uploads/2017/08/e14db151308ad410ad859e6545a8d0f5.jpg',
                title='祀典武廟',
                text='這裡的「拐杖月老」擅長斬爛桃花，或者遇到糾纏不清的舊情人也可以來拜。',
                actions=[
                    PostbackAction(
                        label='抽籤流程',
                        data='war_draw'
                    ),
                    PostbackAction(
                        label='注意事項',
                        data='war_notice'
                    ),
                    PostbackAction(
                        label='返回首頁',
                        data='return'
                    )
                ]
            )
        ]
    )
    )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, Carousel)

    def on_enter_guanyin(self, event):
        print("I'm entering guanyin")
        Carousel= TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=CarouselTemplate(
            image_size="contain",
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://www.taiwan66.com.tw/uploads/panoramas/434/photos/201102111055123.jpg',
                title='大觀音亭',
                text='你適合的是大觀音亭，它屬於市定古蹟，起於荷治明鄭時期，主祀觀世菩薩。',
                actions=[
                    PostbackAction(
                        label='位置',
                        data='guanyin_location'
                    ),
                    PostbackAction(
                        label='開放時間',
                        data='guanyin_time'
                    ),
                    PostbackAction(
                        label='聯絡方式',
                        data='guanyin_phone'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://www.taiwan66.com.tw/uploads/panoramas/434/photos/201102111053224.jpg',
                title='大觀音亭',
                text='大觀音亭的說媒月老耳厚、嘴闊，專長是說媒牽紅線。',
                actions=[
                    PostbackAction(
                        label='求紅線、緣粉流程',
                        data='guanyin_draw'
                    ),
                    PostbackAction(
                        label='注意事項',
                        data='guanyin_notice'
                    ),
                    PostbackAction(
                        label='返回首頁',
                        data='return'
                    )
                ]
            )
        ]
    )
    )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, Carousel)

    def on_enter_cing(self, event):
        print("I'm entering cing")
        Carousel= TemplateSendMessage(
        alt_text='不支援顯示樣板，請使用手機裝置',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://icrvb3jy.xinmedia.com/solomo/article/170289/FBBE31B3-8458-B120-BABB-DC637E48047F.jpeg',
                title='重慶寺',
                text='你適合的是重慶寺，是七寺八廟之一、歷史建築，起源於清朝，主祀觀音，結合了佛教、道教、白教。',
                actions=[
                    PostbackAction(
                        label='位置',
                        data='cing_location'
                    ),
                    PostbackAction(
                        label='開放時間',
                        data='cing_time'
                    ),
                    PostbackAction(
                        label='聯絡方式',
                        data='cing_phone'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://blog.accupass.com/wp-content/uploads/2017/08/3795011809_a8342a744b_z.jpg',
                title='重慶寺',
                text='寺內的「醋矸」乃一大特色，該寺月老也以此聞名，這裡的月老擅長挽回變調的感情。',
                actions=[
                    PostbackAction(
                        label='攪醋矸流程',
                        data='cing_draw'
                    ),
                    PostbackAction(
                        label='注意事項',
                        data='cing_notice'
                    ),
                    PostbackAction(
                        label='返回首頁',
                        data='return'
                    )
                ]
            )
        ]
    )
    )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, Carousel)

    def on_enter_location(self, event):
        print("I'm entering location")
        if event.postback.data == "queen_location":
            location = LocationSendMessage(
                title='大天后宮地址',
                address='台南市中西區永福路二段227巷18號',
                latitude=22.996434,
                longitude=120.201710
            )
            #message = TextSendMessage(text = '返回大天后宮')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大天后宮主選單',
                    actions=[
                        PostbackAction(
                            label='返回大天后宮主選單',
                            data='queen_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "war_location":
            location = LocationSendMessage(
                title='祀典武廟地址',
                address='台南市中西區永福路二段229號',
                latitude=22.996429,
                longitude=120.202153 
            )
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看祀典武廟主選單',
                    actions=[
                        PostbackAction(
                            label='返回祀典武廟主選單',
                            data='war_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "guanyin_location":
            location = LocationSendMessage(
                title='大觀音亭地址',
                address='台南市北區成功路86號',
                latitude=22.9984954,
                longitude=120.206129
            )
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大觀音亭主選單',
                    actions=[
                        PostbackAction(
                            label='返回大觀音亭主選單',
                            data='guanyin_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "cing_location":
            location = LocationSendMessage(
                title='重慶寺地址',
                address='台南市中西區中正路5巷2號',
                latitude=22.991599,
                longitude=120.203526
            )
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看重慶寺主選單',
                    actions=[
                        PostbackAction(
                            label='返回重慶寺主選單',
                            data='cing_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        
        """line_bot_api.push_message('U06538a5ba60fdf5d470b458296993e3d', location)
        line_bot_api.reply_message(reply_token, button)"""
        line_bot_api.reply_message(reply_token, [location,button])
        #line_bot_api.push_message('U06538a5ba60fdf5d470b458296993e3d', message, notification_disabled=True)
    def on_enter_time(self, event):
        print("I'm entering time")
        if event.postback.data == "queen_time":
            message = TextSendMessage(text = '大天后宮開放時間：\n早上六點到晚上九點')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大天后宮主選單',
                    actions=[
                        PostbackAction(
                            label='返回大天后宮主選單',
                            data='queen_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "war_time":
            message = TextSendMessage(text = '祀典武廟開放時間：\n早上五點到晚上九點(初一、十五至晚上十點)')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看祀典武廟主選單',
                    actions=[
                        PostbackAction(
                            label='返回祀典武廟主選單',
                            data='war_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "guanyin_time":
            message = TextSendMessage(text = '大觀音亭開放時間：\n早上七點到晚上九點')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大觀音亭主選單',
                    actions=[
                        PostbackAction(
                            label='返回大觀音亭主選單',
                            data='guanyin_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "cing_time":
            message = TextSendMessage(text = '重慶寺開放時間：\n早上九點到下午五點')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看重慶寺主選單',
                    actions=[
                        PostbackAction(
                            label='返回重慶寺主選單',
                            data='cing_return'
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
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大天后宮主選單',
                    actions=[
                        PostbackAction(
                            label='返回大天后宮主選單',
                            data='queen_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "war_phone":
            message = TextSendMessage(text = '祀典武廟聯絡方式：\n電話：06-2202390')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看祀典武廟主選單',
                    actions=[
                        PostbackAction(
                            label='返回祀典武廟主選單',
                            data='war_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "guanyin_phone":
            message = TextSendMessage(text = '大觀音亭聯絡方式：\n電話：06-2286720、06-2250326')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大觀音亭主選單',
                    actions=[
                        PostbackAction(
                            label='返回大觀音亭主選單',
                            data='guanyin_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "cing_phone":
            message = TextSendMessage(text = '重慶寺聯絡方式：\n電話：06-2232628')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看重慶寺主選單',
                    actions=[
                        PostbackAction(
                            label='返回重慶寺主選單',
                            data='cing_return'
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
            message = TextSendMessage(text = '求籤流程：(只適合有另一半的人)\n1、先向月老上香，並稟明個人資料以及想請示的感情問題。\n2、祈畢插香，持筊過爐三圈淨化，懇請月老賜籤，接著擲筊；若得聖筊，才可繼續求籤。\n3、接著連續擲筊三次，由其顯示的筊型，可得相對應的籤詩。\n4、取籤之後，可自行翻閱籤詩本解籤或請廟方人員解籤。\n\n提醒：此為簡單概述，詳細情形請依廟內規定或洽詢廟方人員。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大天后宮主選單',
                    actions=[
                        PostbackAction(
                            label='返回大天后宮主選單',
                            data='queen_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "war_draw":
            message = TextSendMessage(text = '抽籤流程：\n月老祠沒有籤，需要求籤的信眾，在參拜主神關聖帝君時記得先說，之後抽籤也是跟關聖帝君抽。\n1、購買一份金紙，拜過所有神明。\n2、等20-30分鐘後，詢問關公是否要出籤詩（三個聖筊）\n3、確認完後開始抽籤。\n4、求到後，再度詢問有無要出籤詩（一個聖筊），如果有則會到步驟3繼續；沒有的話即結束。\n\n提醒：此為簡單概述，詳細情形請依廟內規定或洽詢廟方人員。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看祀典武廟主選單',
                    actions=[
                        PostbackAction(
                            label='返回祀典武廟主選單',
                            data='war_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "guanyin_draw":
            message = TextSendMessage(text = '求紅線、緣粉流程：\n1.先向月老上香，並稟明自己的個人資料(包含姓名、生辰、地址)以及理想對象。\n2.接著擲筊，若得聖筊，則可拿取紅線及緣粉。\n3.求得的紅線放在皮包內，等到紅線自然掉落不見，就代表月老去幫你牽姻緣了。\n4.求得的緣粉需擦三天(男生擦脖子、女生擦臉頰)，若有剩下則加進水裡洗臉。\n\n提醒：此為簡單概述，詳細情形請依廟內規定或洽詢廟方人員。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大觀音亭主選單',
                    actions=[
                        PostbackAction(
                            label='返回大觀音亭主選單',
                            data='guanyin_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "cing_draw":
            message = TextSendMessage(text = '攪醋矸流程：\n1. 早期需將自己的頭髮繞於竹棍上再攪動「醋矸」，並拿一些神桌上的燈油塗在另一半的額頭上。\n2. 現在只需用竹棍逆時針攪動「醋矸」三圈即可。\n\n提醒：此為簡單概述，詳細情形請依廟內規定或洽詢廟方人員。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看重慶寺主選單',
                    actions=[
                        PostbackAction(
                            label='返回重慶寺主選單',
                            data='cing_return'
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
            message = TextSendMessage(text = '注意事項：\n1、在寺廟中要先拜主神再拜月老。\n2、多處廟方人員表示，拜月老都可以拜，但求月老只能求一家，請自行斟酌。\n3、月老只是協助，重點還是在個人造化。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大天后宮主選單',
                    actions=[
                        PostbackAction(
                            label='返回大天后宮主選單',
                            data='queen_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "war_notice":
            message = TextSendMessage(text = '注意事項：\n1、在寺廟中要先拜主神再拜月老。\n2、多處廟方人員表示，拜月老都可以拜，但求月老只能求一家，請自行斟酌。\n3、月老只是協助，重點還是在個人造化。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看祀典武廟主選單',
                    actions=[
                        PostbackAction(
                            label='返回祀典武廟主選單',
                            data='war_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "guanyin_notice":
            message = TextSendMessage(text = '注意事項：\n1、在寺廟中要先拜主神再拜月老。\n2、多處廟方人員表示，拜月老都可以拜，但求月老只能求一家，請自行斟酌。\n3、月老只是協助，重點還是在個人造化。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看大觀音亭主選單',
                    actions=[
                        PostbackAction(
                            label='返回大觀音亭主選單',
                            data='guanyin_return'
                        )
                    ]
                )
            )
        elif event.postback.data == "cing_notice":
            message = TextSendMessage(text = '注意事項：\n1、在寺廟中要先拜主神再拜月老。\n2、攪動醋矸時，順時鐘三圈表示永結同心，逆時鐘三圈表示回心轉意。\n3、多處廟方人員表示，拜月老都可以拜，但求月老只能求一家，請自行斟酌。\n4、月老只是協助，重點還是在個人造化。')
            button = TemplateSendMessage(
                alt_text='不支援顯示樣板，請使用手機裝置',
                template=ButtonsTemplate(
                    title='點擊下方按鈕',
                    text='點擊按鈕可查看重慶寺主選單',
                    actions=[
                        PostbackAction(
                            label='返回重慶寺主選單',
                            data='cing_return'
                        )
                    ]
                )
            )
        reply_token = event.reply_token
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, [message, button]) 
    
# exit #
    def on_exit_user(self, event):
        print("Leaving user")

    def on_exit_menu(self, event):
        print("Leaving menu")

    def on_exit_single(self, event):
        print("Leaving single")

    def on_exit_notsingle(self, event):
        print("Leaving notsingle")

    def on_exit_queen(self, event):
        print("Leaving queen")

    def on_exit_war(self, event):
        print("Leaving war")
    
    def on_exit_guanyin(self, event):
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
