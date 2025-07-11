import re
from os import environ
import os
from Script import script
import pytz
import logging

logger = logging.getLogger(__name__)

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        logger.error(f'{type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '24064660')
if len(API_ID) == 0:
    logger.error('API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', 'd299cb7fbd24ae9848bf5867442c19e7')
if len(API_HASH) == 0:
    logger.error('API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '7820241308:AAFp91zCFfYefzlgapTYr22AYRK2_BvihOA')
if len(BOT_TOKEN) == 0:
    logger.error('BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '80'))

# Upload your images to "postimages.org" and get direct link
PICS = (environ.get('PICS', 'https://www.hdwallpapers.in/download/blue_eyes_naruto_uzumaki_minato_namikaze_rasengan_4k_hd_naruto_jpeg-2560x1440.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '8091916399')
if len(ADMINS) == 0:
    logger.error('ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1002264326677 -1002239734551 -1002189644835 -1002432923495 -1002607953782 -1001685513854').split()]
if len(INDEX_CHANNELS) == 0:
    logger.info('INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002599309626')
if len(LOG_CHANNEL) == 0:
    logger.error('LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
FORCE_SUB_CHANNELS = [int(fsub_channels) for fsub_channels in environ.get('FORCE_SUB_CHANNELS', '-1002537832186 -1002518345349 -1002253684616').split()]
if len(FORCE_SUB_CHANNELS) == 0:
    logger.info('FORCE_SUB_CHANNELS is empty')
REQUEST_FORCE_SUB_CHANNELS = environ.get('REQUEST_FORCE_SUB_CHANNELS', '-1002832766371 -1002828777146 -1002871953777')
if len(REQUEST_FORCE_SUB_CHANNELS) == 0:
    logger.info('REQUEST_FORCE_SUB_CHANNELS is empty')
else:
    REQUEST_FORCE_SUB_CHANNELS = int(REQUEST_FORCE_SUB_CHANNELS)
    
# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1002637004953')
if len(SUPPORT_GROUP) == 0:
    logger.error('SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATA_DATABASE_URL = environ.get('DATA_DATABASE_URL', "mongodb+srv://alanshal9633:alanshal9633@alanshal.5i3l1tp.mongodb.net/?retryWrites=true&w=majority&appName=Alanshal")
if len(DATA_DATABASE_URL) == 0:
    logger.error('DATA_DATABASE_URL is missing, exiting now')
    exit()
FILES_DATABASE_URL = environ.get('FILES_DATABASE_URL', "mongodb+srv://alanshal9633:alanshal9633@alanshal.5i3l1tp.mongodb.net/?retryWrites=true&w=majority&appName=Alanshal")
if len(FILES_DATABASE_URL) == 0:
    logger.error('FILES_DATABASE_URL is missing, exiting now')
    exit()
SECOND_FILES_DATABASE_URL = environ.get('SECOND_FILES_DATABASE_URL', "mongodb+srv://alanshal9633:alanshal9633@alanshal.5i3l1tp.mongodb.net/?retryWrites=true&w=majority&appName=Alanshal")
if len(SECOND_FILES_DATABASE_URL) == 0:
    logger.info('SECOND_FILES_DATABASE_URL is empty')
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+Byx_TR0MPediYWI1')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/+OFblnlif6K5jMDZl')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/+Byx_TR0MPediYWI1')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/NarutoSeriesUpdates")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/NarutoSeriesUpdates/12")

# Bot settings
TIME_ZONE = pytz.timezone(environ.get("TIME_ZONE", 'Asia/Colombo'))
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 8))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'hindi english telugu tamil kannada malayalam marathi punjabi').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', '360p 480p 720p 1080p 2160p').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "shortxlinks.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "794a271f91ab933a04f1c1a015dd64dff0ce23b8")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', '3600'))

# boolean settings
USE_CAPTION_FILTER = is_enabled('USE_CAPTION_FILTER', False)
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', False)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002773777484")
if len(BIN_CHANNEL) == 0:
    logger.error('BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://t.me/+6j_hPRMDQCpkNGFl")
if len(URL) == 0:
    logger.error('URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        logger.error('URL is not valid, exiting now')
        exit()

#start command reactions and sticker
REACTIONS = [reactions for reactions in environ.get('REACTIONS', '🤝 😇 🤗 😍 👍 🎅 😐 🥰 🤩 😱 🤣 😘 👏 😛 😈 🎉 ⚡️ 🫡 🤓 😎 🏆 🔥 🤭 🌚 🆒 👻 😁').split()]  # Multiple reactions can be used separated by space
STICKERS = [sticker for sticker in environ.get('STICKERS', 'CAACAgIAAxkBAAEN4ctnu1NdZUe21tiqF1CjLCZW8rJ28QACmQwAAj9UAUrPkwx5a8EilDYE CAACAgIAAxkBAAEN1pBntL9sz1tuP_qo0bCdLj_xQa28ngACxgEAAhZCawpKI9T0ydt5RzYE').split()]  # Multiple sticker can be used separated by space, use @idstickerbot for get sticker id


# for Premium 
PRE_DAY_AMOUNT = int(environ.get('PRE_DAY_AMOUNT', '10')) # add amount in INR for premium charge pre day 
UPI_ID = environ.get("UPI_ID", "sha194832@okaxis")
if len(UPI_ID) == 0:
    logger.error('UPI_ID is missing, exiting now')
    exit()
UPI_NAME = environ.get("UPI_NAME", "Remya") # add your UPI account name
if len(UPI_NAME) == 0:
    logger.error('UPI_NAME is missing, exiting now')
    exit()
RECEIPT_SEND_USERNAME = environ.get("RECEIPT_SEND_USERNAME", "@Alanshal")
