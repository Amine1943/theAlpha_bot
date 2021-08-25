import os
import telebot
import yfinance as yf

#API_KEY = os.getenv('API_KEY')
#bot = telebot.TeleBot(API_KEY)

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "ni greet ni chkoupi")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")
#@bot.on('new_chat_members', (ctx) => console.log(ctx.message.new_chat_members))

bot.polling()