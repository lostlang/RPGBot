from aiogram import executor

from api.telegram import telegram_dp
from config.base import database_name
from logic.database_work import Database

game_database = Database(database_name)

if __name__ == '__main__':

    pass
    # executor.start_polling(telegram_dp)
