import  telebot
import  webbrowser

bot = telebot.TeleBot("7017326687:AAEC8O6BS3YrvQbOnOcdFo6IpSLocMKG7DY")

@bot.message_handler(commands=["site"])
def site(massage):
    webbrowser.open("https://pypi.org/project/pyTelegramBotAPI/")

@bot.message_handler(commands=["start", "hello"])
def main(massage):
    if(massage.from_user.id == 860936779):
        bot.send_message(massage.chat.id, "Вы админ этого бота!")
    else:
        bot.send_message(massage.chat.id,
                         f"К <b>сожалению</b> {massage.from_user.first_name} вы не админ",
                         parse_mode="html"
                         )
@bot.message_handler()
def info(massage):
    if (massage.text.lower() == "привет"):
        bot.send_message(massage.chat.id, f"Првиет {massage.from_user.first_name}!")
    elif(massage.text.lower() == "id"):
        bot.reply_to(massage, f"Ваш ID: {massage.from_user.id}")

bot.polling(non_stop=True)