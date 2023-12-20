import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","12227067"))
API_HASH = getenv("API_HASH","b463bedd791aa733ae2297e6520302fe")
BOT_TOKEN = getenv("BOT_TOKEN","6605147503:AAHoi6D8B0J19CP5wzDe_DKG8APouMsKBXo")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AMBOT:AMBOT@ambot.uecutzy.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001840241140"))
OWNER_ID = int(getenv("OWNER_ID", "5097836954"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiMod/satyammusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/satyamnetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+eSTzpugepEMwNDBl")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/c2a3f692748ef4fecc18c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/86eb759b32ead328e198a.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/4eee6d4a7a1de179ff26d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
