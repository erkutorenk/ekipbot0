import telebot
import time

botToken= "930782923:AAHwJz6AagkErOJvqW6LUOMJHl54J8EkvFQ"

bot = telebot.TeleBot(token=botToken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Kullanım için /help yazınız.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Bir feedback göndermek için /feedback <mesaj>")

@bot.message_handler(commands=['feedback'])
def feedback_message(message):
    ##bot.forward_message(843540306, message.chat.id, message.message_id)
    msg = message.text.split()
    gonder = msg[2:]
    gonder1 = " ".join(gonder)
    id = message.from_user.id
    id = str(id)
    bot.send_message(843540306, "Gönderen kullanıcının ID'si:{}\n{}".format(id, gonder1))
    bot.reply_to(message, 'Başarıyla gönderilmiştir. Cevabınız için bekleyiniz.')

@bot.message_handler(commands=['cevapla'])
def cevapla(message):
    message = message.text.split()
    msg1 = message[2:]
    if message[1]=="@Alpha_TR":
        msg = " ".join(msg1)
        bot.send_message(message[2], msg)


bot.polling()

while True:
    pass



