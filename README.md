<div align="center">

# 🚀 Torrent Downloader Telegram Bot

A lightweight Telegram bot built with **Pyrogram** and **libtorrent** that downloads files from **`.torrent` files** or **direct torrent URLs**, allows users to browse torrent contents, and generates direct HTTP download links.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-success)
![Pyrogram](https://img.shields.io/badge/Pyrogram-Latest-blueviolet)
![Nginx](https://img.shields.io/badge/Nginx-Required-brightgreen)

</div>

---

## ✨ Features

* 📄 Upload `.torrent` files directly to Telegram
* 🔗 Download torrents from direct torrent URLs
* 📂 Browse torrent contents before downloading
* 🖼️ Separate Images and Videos automatically
* 📥 Download only the selected file
* 🌐 Generate direct HTTP download links
* 🗑️ Delete downloaded files from Telegram
* ⚡ Lightweight and easy to deploy
* 🤖 Built with Pyrogram and libtorrent

---

## Requirements

### Server

* Python **3.10+**
* Nginx
* Linux Server (Ubuntu/Debian recommended)
* Public IP address or Domain
* `/var/www/html/` accessible through Nginx

### Python Packages

Install the required packages using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
pyrogram
tgcrypto
requests
libtorrent
```

> **Note:** `tgcrypto` is optional but highly recommended for better Pyrogram performance.

---

## Telegram Requirements

Before using the bot, create:

* A Telegram application at **https://my.telegram.org**
* A Telegram Bot using **@BotFather**

You will need:

* API ID
* API Hash
* Bot Token

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Beheshtii/TorrentDownloader.git
cd TorrentDownloader
```

---

### 2. Create a virtual environment

#### Linux / macOS

```bash
python3 -m venv .venv
```

#### Windows

```powershell
python -m venv .venv
```

---

### 3. Activate the virtual environment

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the bot, edit **`config.py`** and configure all required values.

```python
API_ID =          # https://my.telegram.org
API_HASH = ""     # https://my.telegram.org
TOKEN = ""        # @BotFather

SERVER = "2.2.2.2"      # Your server IP
DOMAIN = "example.com"  # If you don't have a domain, use your server IP
PATH = "/var/www/html/"
```

> **Important:** Make sure every value inside `config.py` is configured correctly before starting the bot.

---

## Running the Bot

```bash
python main.py
```

---

## Nginx

The bot saves downloaded files into:

```python
PATH = "/var/www/html/"
```

Make sure Nginx serves this directory.

Example generated links:

```
https://example.com/movie.mp4
```

or

```
http://YOUR_SERVER_IP/movie.mp4
```

The bot automatically generates download links using the configured `DOMAIN`.

---

## Usage

1. Start the bot.
2. Send a `.torrent` file or a direct torrent download URL.
3. Wait for the torrent metadata to be processed.
4. Choose **Images** or **Videos**.
5. Select the file you want to download.
6. Wait for the download to finish.
7. Receive a direct HTTP download link.
8. Delete the downloaded file whenever you want.

---

## Notes

* Only the selected file is downloaded from the torrent.
* Downloaded files are moved to the directory specified by `PATH`.
* Direct links are generated using the configured `DOMAIN`.
* Nginx must have permission to serve files from the configured directory.
