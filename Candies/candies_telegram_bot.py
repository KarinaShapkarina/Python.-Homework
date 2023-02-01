import telebot
import random



bot = telebot.TeleBot("6038206484:AAGFkoc6yGDIDg20sqYInkpqG1WgRLOvXP8")

candies = 221
max_candies = 28
flag = None

# def restart():
#     global candies
#     candies = 221

@bot.message_handler(commands = ["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, привет!")
    flag = random.choice(["user", "bot"])
    bot.send_message(message.chat.id, f"В игре {candies} конфет")
    if flag == "user":
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, твой ход.")
    else:
        bot.send_message(message.chat.id, f"Первым ходит бот!")
    controller(message)
    


def controller(message):
    global flag
    if candies > 0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Введи количетво конфет от 0 до {max_candies}.")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)   
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")

def bot_input(message):
    global candies
    global flag
    if candies <= max_candies:
        bot_turn = candies
    elif candies % max_candies == 0:
        bot_turn = max_candies
    else:
        bot_turn = candies % max_candies - 1
    candies -= bot_turn 
    bot.send_message(message.chat.id, f"Бот взял {bot_turn } конфет.")
    bot.send_message(message.chat.id, f"Осталось {candies} конфет")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global candies
    global flag
    user_turn = int(message.text)
    candies -= user_turn
    bot.send_message(message.chat.id, f"Осталось {candies} конфет")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

    
bot.infinity_polling()

