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
<b>✅ Основные функции бота:</b>

- Приветствие новых пользователей.
- Удаление системных сообщений.
- Предупреждение и удаление сообщений с ссылками в группе.
- Бан пользователей, которые игнорируют правила.

<u>@PyAdminRUS</u> – связь с разработчиком бота.
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
