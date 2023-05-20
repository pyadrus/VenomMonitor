import datetime
import asyncio
from aiogram import types

from system.dispatcher import dp, bot
from system.sqlite import reading_data_from_the_database, writing_to_the_database_about_a_new_user

"""
Стиль текста для parse_mode="HTML", <code> - моноширинный, <b> - жирный, <i> - наклонный
"""

time_del = 60


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def deleting_message_about_adding_new_group_member(message: types.Message):
    """Удаляем сообщение о новом участнике группы и записываем данные в базу данных"""
    chat_id = message.chat.id  # Получаем ID чата
    chat_title = message.chat.title  # Получаем название чата
    user_id = message.new_chat_members[0].id  # Получаем ID пользователя, который зашел в группу
    username = message.new_chat_members[0].username  # Получаем username пользователя, который вступил в группу
    first_name = message.new_chat_members[0].first_name  # Получаем имя пользователя который вступил в группу
    last_name = message.new_chat_members[0].last_name  # Получаем фамилию пользователя который вступил в группу
    date_now = datetime.datetime.now()  # Дата вступления участника в группу
    await bot.delete_message(chat_id, message.message_id)  # Удаляем сообщение о новом участнике группы
    name_table = "group_members_add"  # Имя таблицы в которую записываем данные
    writing_to_the_database_about_a_new_user(name_table, chat_id, chat_title, user_id, username, first_name, last_name,
                                             date_now)
    # Отправляем сообщение в группу
    await message.answer(f"<code>✅ Привет, {str(message.from_user.full_name)}</code>\n"
                         "<code>Добро пожаловать в чат подружки.</code>\n"
                         "<code>Чат создан для общения и встреч.</code>\n"
                         "<code>Ознакомься, пожалуйста, с правилами чата.</code>\n"
                         "<code>Если заскучала, предлагай встречу.</code>\n"
                         "<code>Или приходи на те, которые предлагают девчонки в чате.</code>", parse_mode="HTML")


@dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def deleting_a_message_about_a_member_has_left_the_group(message: types.Message):
    """Удаляем сообщение о покинувшем участнике группы и записываем данные в базу данных"""
    chat_id = message.chat.id  # Получаем ID чата с которого пользователь вышел
    chat_title = message.chat.title  # Получаем название с которого пользователь вышел
    user_id = message.left_chat_member.id  # Получаем ID пользователя, который вышел с чата
    username = message.left_chat_member.username  # Получаем username пользователя с которого пользователь вышел
    first_name = message.left_chat_member.first_name  # Получаем имя пользователя, того что вышел с группы
    last_name = message.left_chat_member.last_name  # Получаем фамилию пользователя, того что вышел с группы
    date_left = datetime.datetime.now()  # Дата выхода пользователя с группы
    await bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение о покинувшем участнике группы
    name_table = "group_members_left"  # Имя таблицы в которую записываем данные
    writing_to_the_database_about_a_new_user(name_table, chat_id, chat_title, user_id, username, first_name, last_name,
                                             date_left)


@dp.message_handler(content_types=['text'])
async def del_link(message: types.Message) -> None:
    """Запрещенных слов"""

    for entity in message.entities:
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if entity.type in ["url", "text_link"]:
            # Если записанный id пользователя в боте записан, то сообщения пропускаются
            data_dict = reading_data_from_the_database()
            chat_id = message.chat.id
            user_id = message.from_user.id
            print(f"message.from_user.id: {user_id}")
            print(f"chat_id: {chat_id}, user_id: {user_id}")
            if (message.chat.id, message.from_user.id) in data_dict:
                print(f"{str(message.from_user.full_name)} написал сообщение со ссылкой")
                pass
            else:
                await bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение
                # Отправляем сообщение в группу
                warning = await message.answer(f"<code>✅ {str(message.from_user.full_name)}</code>\n"
                                               "<code>В чате запрещена публикация сообщений со ссылками, при повторном "
                                               "нарушении вы будете заблокированные на 24 часа</code>",
                                               parse_mode="HTML")
                await asyncio.sleep(int(time_del))  # Спим 20 секунд
                await warning.delete()  # Удаляем предупреждение от бота
                pass

    for cap in message.caption_entities:
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if cap.type in ["mention"]:
            # Если записанный id пользователя в боте записан, то сообщения пропускаются
            data_dict = reading_data_from_the_database()
            chat_id = message.chat.id
            user_id = message.from_user.id
            print(f"message.from_user.id: {user_id}")
            print(f"chat_id: {chat_id}, user_id: {user_id}")
            if (message.chat.id, message.from_user.id) in data_dict:
                print(f"{str(message.from_user.full_name)} написал сообщение со ссылкой")
                pass
            else:
                await bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение
                # Отправляем сообщение в группу
                warning = await message.answer(f"<code>✅ {str(message.from_user.full_name)}</code>\n"
                                               "<code>В чате запрещена публикация сообщений со ссылками, при повторном "
                                               "нарушении вы будете заблокированные на 24 часа</code>",
                                               parse_mode="HTML")
                await asyncio.sleep(int(time_del))  # Спим 20 секунд
                await warning.delete()  # Удаляем предупреждение от бота
                pass


def bot_handlers():
    """Регистрируем handlers для всех пользователей"""
    dp.register_message_handler(deleting_message_about_adding_new_group_member)
    dp.register_message_handler(deleting_a_message_about_a_member_has_left_the_group)
    dp.register_message_handler(del_link)
