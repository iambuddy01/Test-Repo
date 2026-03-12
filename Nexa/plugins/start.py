from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Nexa.bot import app

START_IMAGE = "https://files.catbox.moe/u5ry00.jpg"

TEXT = "Welcome To Nexa Bot"

HELP = "https://t.me/yourhelp"
UPDATE = "https://t.me/yourupdates"
MAJDURI = "https://t.me/yourrepo"
SUPPORT = "https://t.me/yoursupport"

@app.on_message(filters.command("start"))
async def start(client, message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help", url=HELP),
                InlineKeyboardButton("Update", url=UPDATE)
            ],
            [
                InlineKeyboardButton("Majduri", url=MAJDURI),
                InlineKeyboardButton("Support", url=SUPPORT)
            ]
        ]
    )

    await message.reply_photo(
        photo=START_IMAGE,
        caption=TEXT,
        reply_markup=buttons
)
