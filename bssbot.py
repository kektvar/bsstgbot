import os
import telebot as tb
from dotenv import load_dotenv

def shutdown_pc():
    os.system("shutdown /s /t 0")

def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def reboot_pc():
    os.system("shutdown /r /t 0")

load_dotenv()
bot = tb.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.reply_to(message, "Bot has been started\nAll comands:\n/offpc - shutdown your pc\n/rebootpc - reboot your pc")

@bot.message_handler(commands=['offpc'])
def offpc(message):
    bot.reply_to(message, "Your pc was turned off")
    shutdown_pc()

@bot.message_handler(commands=['rebootpc'])
def rebootpc(message):
    bot.reply_to(message, "Your pc has been rebooted")
    reboot_pc()

bot.infinity_polling()