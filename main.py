import telebot
from telebot import types

# 你的 Telegram Bot Token（去 BotFather 拿）
TOKEN = 8343172946:AAEmtmqgxODIMcaC75O7PmdmRa-tDVKWGVM
bot = telebot.TeleBot(TOKEN)

# 來源群組 ID
SOURCE_CHAT_ID = -1001234567890  # 替換成來源群組 ID
# 目標群組 ID
TARGET_CHAT_ID = -1009876543210  # 替換成目標群組 ID

# 收到訊息時觸發
@bot.message_handler(func=lambda message: True)
def forward_message(message):
    if message.chat.id == SOURCE_CHAT_ID:
        bot.forward_message(TARGET_CHAT_ID, message.chat.id, message.message_id)

print("Bot 正在運行中...")
bot.polling()
