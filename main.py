from aiogram import executor

from api.telegram import telegram_dp

if __name__ == '__main__':
    executor.start_polling(telegram_dp)
