import asyncio
import os
from pyrogram import Client, filters

# بيانات API و توكن البوت من البيئة
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# الاستماع إلى الرسائل في القروب
@app.on_message(filters.group & filters.text)
async def on_message(client, message):
    if 'سبيسيبسيبثفهيس' in message.text:
        await message.reply("مرحبا!")

async def main():
    await app.start()
    print("✅ البوت يعمل الآن!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
