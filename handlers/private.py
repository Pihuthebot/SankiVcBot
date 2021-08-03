from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
HεΥ 🙋‍♀, {} Ι Cαη Plαγ Μυsιc Iη Τhε Vσιcε Chατs Of TεlεGrαm Grσυρs & Chαηηεls Iη Frεε.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("➕ Add Με Τσ Υσυr Grσυρ 🙋‍♀️", url="https://t.me/SankiRobot?startgroup=true")],
                [InlineKeyboardButton("🔥 Οωηεr 🔥", url="https://t.me/Em_Nitric")]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ΗεΥ, 🕹 ‣ 𝙎𝙖𝙣𝙠𝙞 𝙍𝙤𝙗𝙤𝙩 [🇮🇳] Ιs Οηlιηε Ηεrε.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Uρdατεs", url="https://t.me/BrandSanki")
                ]
            ]
        )
   )
