from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""𝙼𝚎𝚛𝚑𝚊𝚋𝚊👋 𝙱𝚎𝚗 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙶𝚛𝚞𝚙𝚕𝚊𝚛ı𝚗𝚍𝚊 𝙱𝚊𝚗 𝚈𝚎𝚝𝚔𝚒𝚜𝚒 𝙾𝚕𝚖𝚊𝚍𝚊𝚗 𝙼ü𝚣𝚒𝚔 Ç𝚊𝚕𝚊𝚋𝚒𝚕𝚒𝚢𝚘𝚛𝚞𝚖. 𝙶𝚛𝚞𝚋𝚞𝚗𝚞𝚣𝚞𝚗 𝚜𝚎𝚜𝚕𝚒 𝚜𝚘𝚑𝚋𝚎𝚝𝚒𝚗𝚍𝚎 𝚖ü𝚣𝚒𝚔 ç𝚊𝚕𝚊𝚋𝚒𝚕𝚖𝚎𝚔 𝚒ç𝚒𝚗 𝙰𝚜𝚒𝚜𝚝𝚊𝚗ı𝚗 𝚐𝚛𝚞𝚋𝚞𝚗𝚞𝚣𝚍𝚊 𝚘𝚕𝚖𝚊𝚜ı 𝚐𝚎𝚛𝚎𝚔𝚒𝚛. 𝙰𝚂İ𝚂𝚃𝙰𝙽; @MissMuzikAsistan.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://t.me/MissMusicSupport")
                  ],[
                    InlineKeyboardButton(
                        "🥳 Asistan 🥳", url="https://t.me/MissMuzikAsistan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grubumuz 🎙️", url="https://t.me/intikamailesi"
                    )],
                [
                    InlineKeyboardButton(text= "😇Sahibim😇", url = "https://t.me/MissKraL")
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Müzik Botu Sorunsuz Çalışıyor..✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Destek", url="https://t.me/MissMusicSupport")
                ]
            ]
        )
   )
