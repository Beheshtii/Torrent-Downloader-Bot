import os
import time
import libtorrent as lt
import shutil
import math
from config import PATH, DOMAIN

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_torrent_files(torrent_id):
    info = lt.torrent_info(f"torrents/{torrent_id}.torrent")

    ses = lt.session()
    ses.listen_on(6881, 6891)

    files = info.files()

    photos = {}
    videos = {}

    total_size = convert_size(files.total_size())

    for index in range(files.num_files()):
        file_path = files.file_path(index)

        file_name = files.file_name(index)
        file_size = convert_size(files.file_size(index))

        if file_path.endswith(".mp4") or file_path.endswith(".mkv"):
            videos[index] = [file_name, file_size]
        elif file_path.endswith(".webm") or file_path.endswith(".jpg") or file_path.endswith(".jpeg") or file_path.endswith(".png"):
            photos[index] = [file_name, file_size]

    return photos, videos, total_size

def get_file_info(torrent_id, index):
    info = lt.torrent_info(f"torrents/{torrent_id}.torrent")

    ses = lt.session()
    ses.listen_on(6881, 6891)

    files = info.files()

    file_path = files.file_path(index)
    file_name = files.file_name(index)
    file_size = convert_size(files.file_size(index))

    return file_path, file_name, file_size

def download_torrent_file(torrent_id, index):
    torrent_path = f"torrents/{torrent_id}.torrent"

    info = lt.torrent_info(torrent_path)
    files = info.files()

    file_path = files.file_path(index)
    file_name = os.path.basename(file_path)
    ext = os.path.splitext(file_name)[1]

    download_root = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_root, exist_ok=True)

    ses = lt.session()
    ses.listen_on(6881, 6891)

    handle = ses.add_torrent({
        "ti": info,
        "save_path": download_root
    })

    priorities = [0] * files.num_files()
    priorities[index] = 1
    handle.prioritize_files(priorities)

    while handle.status().progress < 1.0:
        time.sleep(1)

    downloaded_full_path = os.path.join(download_root, file_path)

    if not os.path.exists(downloaded_full_path):
        raise FileNotFoundError(f"Downloaded file not found: {downloaded_full_path}")

    os.makedirs(PATH, exist_ok=True)

    final_filename = f"{torrent_id}_{index}{ext}"
    final_path = os.path.join(PATH, final_filename)

    shutil.move(downloaded_full_path, final_path)

    url = f"https://{DOMAIN}/{final_filename}"

    return url, final_filename