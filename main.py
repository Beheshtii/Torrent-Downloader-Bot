from pyrogram import Client
from config import *

plugins = dict(root="plugins")

app = Client(
    name="TDBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=plugins
)

app.run()
