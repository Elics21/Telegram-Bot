import  telebot

import  sqlite3

bot = telebot.TeleBot("7017326687:AAEC8O6BS3YrvQbOnOcdFo6IpSLocMKG7DY")

@bot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("base.sql")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))")
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, "Привет! Ввведите имя")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    name = message.text.strip()

    bot.send_message(message.chat.id, "Ввведите пароль")
    bot.register_next_step_handler(message, user_pass, name)

def  user_pass(message, name):
    password = message.text.strip()

    conn = sqlite3.connect("base.sql")
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("Список пользователей", callback_data="user_list")
    markup.add(btn1)

    bot.send_message(message.chat.id, "Вы зарегистрированы", reply_markup=markup)
    bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "user_list":
        conn = sqlite3.connect("base.sql")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        info = ""
        for el in users:
            info += f"Имя: {el[1]}, Пароль: {el[2]}\n"

        cur.close()
        conn.close()

        bot.send_message(call.message.chat.id, info)

bot.polling(non_stop=True)