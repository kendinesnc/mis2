from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""πΌπππππππ π±ππ ππππππππ πΆππππππΔ±πππ π±ππ πππππππ πΎππππππ πΌΓΌπ£ππ Γππππππππ’ππππ. πΆπππππππ£ππ πππππ ππππππππππ πΓΌπ£ππ Γ§πππππππππ πΓ§ππ π°ππππππΔ±π ππππππππ£ππ πππππΔ± πππππππ. π°πΔ°πππ°π½; @MissMuzikAsistan... """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π KullanΔ±m KΔ±lavuzu π", url="https://t.me/MissMusicSupport")
                  ],[
                    InlineKeyboardButton(
                        "π₯³ Asistan π₯³", url="https://t.me/MissMuzikAsistan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grubumuz ποΈ", url="https://t.me/intikamailesi"
                    )],
                [
                    InlineKeyboardButton(text= "DC BOTU", url = "https://t.me/Missdcbot")
                ],[
                    InlineKeyboardButton(text= "π₯Sahipπ₯", url = "https://t.me/intikamsahibi")
            ],]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("botcum") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** β BurdayΔ±m Sahibim @intikamsahibi β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Support Ve Komutlar", url="https://t.me/MissMusicSupport")
                ]
            ]
        )
   )
