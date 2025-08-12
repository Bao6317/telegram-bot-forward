import os
import telebot

# 從環境變數讀取 Token（Render → Environment 裡加 BOT_TOKEN）
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing (set it in Render → Environment)")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# 這裡換成你的實際 chat id（負數是頻道/群組）
SOURCE_CHAT_ID = -1001234567890
TARGET_CHAT_ID = -1009876543210

# 確保沒有 webhook（避免 409）
bot.delete_webhook(drop_pending_updates=True)

@bot.message_handler(func=lambda m: m.chat.id == SOURCE_CHAT_ID)
def forward(m):
    try:
        bot.forward_message(TARGET_CHAT_ID, m.chat.id, m.message_id)
    except Exception as e:
        print("forward error:", e)

if __name__ == "__main__":
    print("Bot 正在運行中...")
    # 用 infinity_polling 更穩定
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
