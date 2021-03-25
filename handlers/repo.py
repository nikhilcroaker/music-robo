from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("repo")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**MʋsɩcRoɓo𝓽:** ɩʆ ƴoʋ wʌŋt ɱʋsɩcɓot ɭɩĸɘ ɱɘ tʜɘŋ cɭɩcĸ oŋ ʀɘpo ɓʋttoŋ to ʛɘt ɱƴ ʀɘpo ʌŋɗ cɭɩcĸ oŋ SESSION ɓʋttoŋ ʆoʀ ʛɘʀŋʌtɩŋʛ sɘssɩoŋ ʌŋɗ cɭɩcĸ oŋ ʜɘʀoĸʋ ɓottoŋ to ɗɘpɭoƴ ɱɘ🤍  \n**Go Aŋɗ Dɘpɭoƴ It Now ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/nikhilcroaker/music-robo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://replit.com/@nikhilcroaker/music-robo"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot&template=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot"
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
    filters.command("repo")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        "**MʋsɩcRoɓo𝓽:** ɩʆ ƴoʋ wʌŋt ɱʋsɩcɓot ɭɩĸɘ ɱɘ tʜɘŋ cɭɩcĸ oŋ ʀɘpo ɓʋttoŋ to ʛɘt ɱƴ ʀɘpo ʌŋɗ cɭɩcĸ oŋ SESSION ɓʋttoŋ ʆoʀ ʛɘʀŋʌtɩŋʛ sɘssɩoŋ ʌŋɗ cɭɩcĸ oŋ ʜɘʀoĸʋ ɓottoŋ to ɗɘpɭoƴ ɱɘ🤍  \n**Go Aŋɗ Dɘpɭoƴ It Now ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/nikhilcroaker/music-robo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://replit.com/@nikhilcroaker/music-robo"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot&template=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot"
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
