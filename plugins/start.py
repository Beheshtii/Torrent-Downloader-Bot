from pyrogram import Client, filters
from pyrogram.types import Message
from utils.buttons import confirm_button

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply_text(text="""
Welcome to the Torrent Downloader Bot
Send a torrent file or link to use
.""")

@Client.on_message(filters.private)
async def message_handler(client: Client, message: Message):
    msg = message.text

    if msg and msg.startswith("http"):
        await message.reply_text(text="Are you sure the link you sent is correct?", reply_markup=confirm_button)

    elif message.document:
        file_name = message.document.file_name.lower()
        if file_name.endswith(".torrent"):
            await message.reply_text(text="Are you sure the file you sent is correct?", reply_markup=confirm_button)
        else:
            await message.reply_text(text="The torrent sent is not valid.")
    else:
        await message.reply_text(text="The torrent sent is not valid.")
