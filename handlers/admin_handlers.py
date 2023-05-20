import datetime

from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

from system.dispatcher import dp

date_now = datetime.datetime.now()


class AddUserStates(StatesGroup):
    WAITING_FOR_USER_ID = State()  # ожидание ввода ID пользователя;
    USER_ADDED = State()  # состояние, когда пользователь успешно добавлен в базу данных.


# Игнорирование сообщений, когда состояние FSM = USER_ADDED
@dp.message_handler(state=AddUserStates.USER_ADDED)
async def ignore_messages(message: types.Message):
    pass


info = '''
<b>✅ Основные команды бота:</b>
<u>/start</u>     – 🤖 запустить бота,
<u>/help</u>      – 🤖 информация по работе с ботом,
<u>/id</u>        – 🧾 узнать ID участника чата (использование в виде ответа на сообщение),
<u>/user_add</u>  – 🧾 дать пользователю определенные права в группе (нужен ID участника),
<u>/pin</u>       – 📌 закрепить сообщение (использование в виде ответа на сообщение, которое хотите закрепить),
<u>/unpin</u>     – 📌 открепить сообщение (использование в виде ответа на сообщение, которое хотите открепить),
<u>/unpin_all</u> – 📌 открепить все закрепленные сообщения,
<u>@PyAdminRUS</u>– 🔗 связь с администратором (разработчиком).
'''


# обработчик команды /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message) -> None:
    """Отвечаем на команду start"""
    await message.reply(info, parse_mode="HTML")


# обработчик команды /help
@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message) -> None:
    """Отвечаем на команду help"""
    await message.reply(info, parse_mode="HTML")


def admin_handlers():
    """Регистрируем handlers для всех пользователей"""
    dp.register_message_handler(send_welcome)
    dp.register_message_handler(help_handler)
