from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""🙃 Hɩ {message.from_user.first_name}!

✨ I ʌɱ MʋsɩcRoɓo Mʋsɩc Pɭʌƴɘʀ

🥳 I cʌŋ pɭʌƴ ɱʋsɩc ɩŋ ƴoʋʀ Tɘɭɘʛʀʌɱ Gʀoʋp's Voɩcɘ Cʜʌt😉

⚜️ Usɘ tʜɘsɘ ɓʋttoŋs ɓɘɭow to ĸŋow ɱoʀɘ. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📔 Soʋʀcɘ Coɗɘ 📔", url="https://github.com/nikhilcroaker/music-robo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Bot Cʀɘʌtoʀ 💬", url="https://t.me/Mr_Nitric"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel 📣", url="https://t.me/Bakchodindia"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**êvilẞø†:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
