from pyrogram import Client
from pyrogram.types import CallbackQuery

from utils.funcs import download_torrent, delete_file
from utils.texts import selection_text, download_text, successfully_downloaded
from utils.torrent import get_torrent_files, get_file_info, download_torrent_file
from utils.buttons import (
    photo_or_video_buttons,
    generate_media_buttons,
    delete_file_button
)

async def safe_edit(query: CallbackQuery, text: str, **kwargs):
    try:
        await query.message.edit_text(text, **kwargs)
    except Exception:
        pass


def split_data(data: str):
    return data.split(".")

@Client.on_callback_query()
async def callback(client: Client, query: CallbackQuery):
    data = query.data

    # DOWNLOAD TORRENT
    if data == "download":
        msg = query.message.reply_to_message

        await safe_edit(query, "Downloading...")

        try:
            if msg.document:
                file_path, file_name, file_id = await download_torrent(
                    client=client,
                    torrent_file=msg
                )
            else:
                file_path, file_name, file_id = await download_torrent(
                    client=client,
                    torrent_url=msg.text
                )

            photos, videos, total_size = get_torrent_files(file_id)

        except Exception:
            return await safe_edit(query, "⚠️ Failed to download torrent")

        return await safe_edit(
            query,
            selection_text.format(file_id, len(videos), len(photos), total_size),
            reply_markup=photo_or_video_buttons(file_id)
        )

    # PHOTOS / VIDEOS
    if data.startswith("photos") or data.startswith("videos"):
        file_id = split_data(data)[1]

        await safe_edit(query, "Sending...")

        try:
            photos, videos, total_size = get_torrent_files(file_id)
        except Exception:
            return await safe_edit(query, "⚠️ Failed to get torrent files")

        medias = photos if data.startswith("photos") else videos
        label = "🖼️ Images" if data.startswith("photos") else "🎬 Videos"

        return await safe_edit(
            query,
            f"{label}: {len(medias)}\n✅ Click to get direct link.",
            reply_markup=generate_media_buttons(medias=medias, torrent_id=file_id)
        )

    # DOWNLOAD FILE
    if data.startswith("dl"):
        _, file_id, index = split_data(data)

        try:
            file_path, file_name, file_size = get_file_info(file_id, int(index))
        except Exception:
            return await safe_edit(query, "⚠️ Failed to get torrent info")

        await safe_edit(query, download_text.format(file_id, file_name, file_size))

        url, final_filename = download_torrent_file(file_id, int(index))

        await safe_edit(
            query,
            successfully_downloaded.format(url),
            reply_markup=delete_file_button(final_filename)
        )

        # refresh list
        photos, videos, total_size = get_torrent_files(file_id)

        return await query.message.reply_text(
            selection_text.format(file_id, len(videos), len(photos), total_size),
            reply_markup=photo_or_video_buttons(file_id)
        )

    # DELETE FILE
    if data.startswith("delete"):
        parts = split_data(data)
        file_name = f"{parts[1]}.{parts[-1]}"

        try:
            delete_file(file_name)
            return await safe_edit(query, "✅ File deleted")
        except Exception:
            return await safe_edit(query, "⛔ Failed to delete file")

    # BACK
    if data.startswith("back"):
        file_id = split_data(data)[1]

        try:
            photos, videos, total_size = get_torrent_files(file_id)
        except Exception:
            return await safe_edit(query, "⚠️ Failed to get torrent files")

        return await safe_edit(
            query,
            selection_text.format(file_id, len(videos), len(photos), total_size),
            reply_markup=photo_or_video_buttons(file_id)
        )