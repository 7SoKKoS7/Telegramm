from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import mariadb
import sys

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=os.getenv('USER_NAME'),
        password=os.getenv('password_name'),
        host=os.getenv('host_name'),
        port=3306,
        database=os.getenv('database_name')
    )
    print('base connection - OK')
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


# Get Cursor
cur = conn.cursor()


# TEST
# cur.execute("SELECT * FROM AMain WHERE Name = 'Igor'")
#
#
# for Name in cur:
#     print(f"First name: {Name}")








