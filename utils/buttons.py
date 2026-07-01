from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ButtonStyle

confirm_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Yes, I'm sure.", style=ButtonStyle.SUCCESS, callback_data="download"),
        ]
    ]
)


def delete_file_button(file_name):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Delete File ⛔", style=ButtonStyle.DANGER, callback_data=f"delete.{file_name}"),
            ]
        ]
    )


def photo_or_video_buttons(torrent_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Photos 🖼️", callback_data=f"photos.{torrent_id}"),
                InlineKeyboardButton(text="Videos 🎬", callback_data=f"videos.{torrent_id}"),
            ]
        ]
    )


def generate_media_buttons(medias, torrent_id):
    buttons = []

    counter = 1
    for key, value in medias.items():
        file_name, file_size = value
        name = file_name if len(file_name) <= 20 else f"{file_name[:20]}..."
        buttons.append([InlineKeyboardButton(text=f"[{str(counter).zfill(2)}] - {name} | ({file_size})",
                                             callback_data=f"dl.{torrent_id}.{key}")])
        counter += 1

    buttons.append([InlineKeyboardButton(text="🔙", callback_data=f"back.{torrent_id}")])

    return InlineKeyboardMarkup(
        buttons
    )
