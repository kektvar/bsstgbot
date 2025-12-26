import os
import telebot as tb
from dotenv import load_dotenv
import time
import pyautogui as pg

def shutdown_pc():
    os.system("shutdown /s /t 0")

def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def reboot_pc():
    os.system("shutdown /r /t 0")

def status_pc():
    print('ON')

def onmacros():
    pg.press('f1')

def pausemacros():
    pg.press('f2')

def offmacros():
    pg.press('f3')

load_dotenv()
bot = tb.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.reply_to(message, "Bot has been started\n/commands - check commands")

@bot.message_handler(commands=['offpc'])
def offpc(message):
    bot.reply_to(message, "Your pc was turned off")
    shutdown_pc()

@bot.message_handler(commands=['rebootpc'])
def rebootpc(message):
    bot.reply_to(message, "Your pc has been rebooted")
    reboot_pc()

@bot.message_handler(commands=['sleep'])
def sleeppc(message):
    bot.reply_to(message, "Your pc went into sleep mode")
    sleep_pc()

@bot.message_handler(commands=['status'])
def checkstatus(message):
    bot.reply_to(message, status_pc())

@bot.message_handler(commands=['commands'])
def commandscheck(message):
    bot.reply_to(message, 'All comands:\n/status - check status\n/offpc - shutdown your pc\n/rebootpc - reboot your pc\n/sleep - put the pc into sleep mode\n/onmacro - turn on macro\n/offmacro - turn off macro\n/pausemacro - pause macro')

@bot.message_handler(commands=['onmacro'])
def on_macros(message):
    bot.reply_to(message, 'macro enabled')

@bot.message_handler(commands=['offmacro'])
def off_macros(message):
    bot.reply_to(message, 'macro disabled')

@bot.message_handler(commands=['pausemacro'])
def pause_macros(message):
    bot.reply_to(message, 'macro paused')

bot.infinity_polling()