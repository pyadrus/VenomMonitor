from aiogram.utils import executor
from loguru import logger

from handlers.admin_handlers import admin_handlers, date_now
from handlers.bot_handlers import bot_handlers
from system.dispatcher import dp

logger.add("setting/log/log.log", rotation="1 MB", compression="zip")


def main():
    """Запуск бота"""
    print(f"GreetingSentryBot запущен {date_now}")
    executor.start_polling(dp, skip_updates=True)
    # Handlers - для админа и пользователей
    admin_handlers()
    # Handlers - только для бота
    bot_handlers()


if __name__ == "__main__":
    try:
        # Запуск бота
        main()
    except Exception as e:
        logger.exception(e)
        print("[bold red][!] Произошла ошибка, для подробного изучения проблемы просмотрите файл log.log")
