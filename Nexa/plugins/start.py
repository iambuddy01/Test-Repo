from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Nexa.bot import app, CLONED
from Nexa.client import load_plugins
from config import API_ID, API_HASH

START_IMAGE = "https://graph.org/file/6e7c1a1f5c21d5b9a9c3e.jpg"

TEXT = "Welcome To Nexa Cloner Bot"

@app.on_message(filters.command("start"))
async def start(client, message):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help", callback_data="help"),
                InlineKeyboardButton("Update", url="https://t.me/telegram")
            ],
            [
                InlineKeyboardButton("Majduri", url="https://t.me/telegram"),
                InlineKeyboardButton("Support", url="https://t.me/telegram")
            ]
        ]
    )

    await message.reply_photo(
        photo=START_IMAGE,
        caption=TEXT,
        reply_markup=buttons
    )


@app.on_message(filters.command("clone"))
async def clone(client, message):

    if len(message.command) < 2:
        await message.reply_text("Use /clone <session_string>")
        return

    session = message.command[1]

    try:

        user_client = Client(
            name=f"clone_{message.from_user.id}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session
        )

        await user_client.start()

        load_plugins(user_client)

        CLONED[message.from_user.id] = user_client

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Fetch Groups", callback_data="fetch")
                ]
            ]
        )

        await message.reply_text(
            "Clone Successful\n\nAvailable Commands:\n/fetch\n/status",
            reply_markup=buttons
        )

    except Exception as e:
        await message.reply_text(str(e))
