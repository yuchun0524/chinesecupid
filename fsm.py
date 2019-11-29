"""from transitions.extensions import GraphMachine
from linebot.models import *
from utils import send_text_message, send_button_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
# is going to #

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "開始"
        #return text.lower() == "go to state1"

    def is_going_to_queen(self, event):
        text = event.message.text
        return text.lower() == "單戀中，求紅線" or text.lower() == "有對象，希望感情加溫"
        
        return text.lower() == "go to state2"
    def is_going_to_war(self, event):
        text = event.message.text
        return text.lower() == '想砍掉爛桃花'

    def is_going_to_guanyin(self, event):
        text = event.message.text 
        return text.lower() == '單身，求姻緣'
       
    def is_going_to_cing(self, event):
        text = event.message.text
        return text.lower() == '求感情復合'
        
# enter #

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        button = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='為什麼想拜月老？',
            text='不同廟的月老有不同的專長，選擇適合你的或許能更快完成心願喔！',
            thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuz6VkzNxBKNK8QcHZspwJP_sQOcYReWEjh603OESaHkG0mN2wEQ&s',
            actions=[
                MessageTemplateAction(
                label='單身，求姻緣',
                text='單身，求姻緣'
                ),
                MessageTemplateAction(
                label='單戀中，求紅線',
                text='單戀中，求紅線'
                ),
                MessageTemplateAction(
                label='有對象，希望感情加溫',
                text='有對象，希望感情加溫'
                ),
                MessageTemplateAction(
                label='想砍掉爛桃花',
                text='想砍掉爛桃花'
                ),
                MessageTemplateAction(
                label='求感情復合',
                text='求感情復合'
                )
            ]
        )
    )
    send_button_message(reply_token, button)
        #send_text_message(reply_token, "Trigger state1")
        #self.go_back()
    def on_enter_queen(self, event):
        print("I'm entering queen")
        reply_token = event.reply_token
        send_text_message(reply_token, "queen")
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
        """
from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")