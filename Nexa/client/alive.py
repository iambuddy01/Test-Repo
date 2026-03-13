from pyrogram import filters

def load(client):

    @client.on_message(filters.command("alive", ".") & filters.me)
    async def alive_handler(client, message):
        await message.reply_text("Nexa Client Alive")
