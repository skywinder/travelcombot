import os


BOT_TOKEN = os.getenv('BOT_TOKEN')
DEBUG = False
PROXY = {'https': os.getenv('PROXY_STRING')}
LOGGER_PATH = 'logging.log'
AVARATRS_PATH = 'avatars/'
# ID Telegram админов в боте
ADMINS = [217166737, 263156959]

# MySQL данные для авторизации
db_host = 'mysql'
db_user = 'root'
db_password = ''
db_database = ''
db_charset = 'utf8'

# ID Telegram канала для подтверждение анкет пользователей
admin_channel_id = -1001346987455

main_markup = [
	'📍 Поделиться геолокацией',
	'🗺 Посмотреть геолокации пользователей',
	'⚙️ Настройки',
]

setting_markup = [
	'ℹ️ Рассказать о себе и своих интересах',
	'🎇 Дополнить мероприятия',
	'📱 Добавить ссылку на инстаграм',
]

admin_markup = [
	'📩 Создать рассылку',
]

try:
	from local_config import *
except ImportError:
	pass
