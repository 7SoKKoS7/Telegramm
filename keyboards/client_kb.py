from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# , ReplyKeyboardRemove


b1 = KeyboardButton('/Режим_роботи')
b2 = KeyboardButton('/Ваш_ID')
b3 = KeyboardButton('/Отримати_тест')
b4 = KeyboardButton('Поділитися номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)
b5 = KeyboardButton('/Оновити')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).row(b2, b3).row(b4, b5)
