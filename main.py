import  telebot
from  telebot import  types

bot = telebot.TeleBot("7017326687:AAEC8O6BS3YrvQbOnOcdFo6IpSLocMKG7DY")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Магазин")
    btn2 = types.KeyboardButton("Информация")
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, "Наше меню:", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, "information")
    elif message.text == "Магазин":
        bot.send_message(message.chat.id, "store: ")

@bot.message_handler(commands=["help"])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url="https://www.youtube.com")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалиить сообщение", callback_data="delete")
    btn3 = types.InlineKeyboardButton("Bpvtybnm сообщение", callback_data="edit")
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, "Крутой сайт!", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == "edit":
        bot.edit_message_text("eding text", callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)