from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
import datetime



async def echo_chat_in_base(message: types.message):
    await bot.send_message(message.from_user.id, 'Повідомлення отримано, очикуйте контакту - це тест')
    str_client = (message.from_user.id, message.text, datetime.datetime.now())
    sqlite_db.cur.execute('INSERT INTO client_base VALUES (NULL, ?, ?, ?)', str_client)
    sqlite_db.base.commit()




# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Привіт', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з ботом через повідомлення, напишіть йому:\nhttps://t.me/TVPK_bot')

# @dp.message_handler(commands=['Режим_роботи'])
async def open_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Пн-ВС с 9:00 до 20:00')

# @dp.message_handler(commands=['Ваш ID'])
async def place_command(message : types.Message):
	await bot.send_message(message.from_user.id, f"Ваш ID: {message.from_user.id}")#, reply_markup=ReplyKeyboardRemove())
    # await bot.send_message(5278056295,f"Id відправника: {message.from_user.id}")


# @dp.message_handler(commands=['Меню'])
async def menu_command(message : types.Message):
    await bot.send_message(message.from_user.id, f"Ваш test")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', 'Оновити'])
    dp.register_message_handler(open_command, commands=['Режим_роботи'])
    dp.register_message_handler(place_command, commands=['Ваш_ID'])
    dp.register_message_handler(menu_command, commands=['Отримати_тест'])
    dp.register_message_handler(echo_chat_in_base)
