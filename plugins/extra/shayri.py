from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time

from Bikash import app
from Bikash.utils.bgtmusic.bk import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

shayri = [ "हौसले के तरकश में कोशिश का तीर 🏹 जिंदा रखो, हार जाओ चाहे जिंदगी में सब कुछ मगर जीतने की उम्मीद जिंदा रखो।",
"रख हौसला वो मंजर भी आयेगा, प्यासे के पास चल के समन्दर भी आयेगा, थक कर न बैठ ऐ मंज़िल के मुसाफिर, मंज़िल भी मिलेगी और मिलने का मज़ा भी आयेगा ।",
"तू हँस, तू मुस्कुरा और रोना कम कर दे जिन्दा है तू, जिंदगी की नाक में दम कर दे...!!",
"ना संघर्ष ना तकलीफ, खाक मजा है जीने में बङे बङे तुफान थम जाते है,, जब आग लगीं हो सीने में...!!",
"जब आंखों में अरमान लिया, मंजिल को अपना मान लिया तो मुश्किल क्या, आसान क्या, जब ठान लिया तो ठान लिया..!!" ]

@app.on_message(
    filters.command("shayri")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_text(text = random.choice(shayri),
        reply_markup=InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton(
                        "💝 𝐆ɾσυ𝐏 💝", url=f"https://t.me/mission_successs"
                    ),
                    InlineKeyboardButton(
                        "💝 𝐂ԋαɳɳҽ𝐋 💝", url=f"https://t.me/About_Info_Devil")
                ]
            ]
        ),
    )
