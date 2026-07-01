from pyrogram import Client
from pyrogram.types import Message
import os
import random
import asyncio
import requests
from config import PATH

async def download_torrent(
        client: Client,
        torrent_url: str | None = None,
        torrent_file: Message | None = None,
):
    os.makedirs("torrents", exist_ok=True)

    file_id = random.randint(100000, 999999)
    file_name = f"{file_id}.torrent"
    file_path = os.path.join("torrents", file_name)

    if torrent_url:
        def _download():
            response = requests.get(torrent_url, timeout=30)
            response.raise_for_status()

            with open(file_path, "wb") as f:
                f.write(response.content)

        await asyncio.to_thread(_download)

    elif torrent_file:
        await client.download_media(message=torrent_file, file_name=file_path)

    else:
        raise ValueError("torrent_url or torrent_file is required.")

    return file_path, file_name, file_id

def delete_file(file_name):
    file_path = os.path.join(PATH, file_name)
    os.remove(file_path)
