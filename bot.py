
from aiogram import Bot, Dispatcher, executor, types
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")
SUPPORT_LINK = os.getenv("SUPPORT_LINK", "https://t.me/hamonasa")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📋 Записаться", "🛠 Я мастер", "📞 Служба поддержки")
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

# Запись клиента
@dp.message_handler(lambda message: message.text == "📋 Записаться")
async def handle_booking(message: types.Message):
    await message.answer("Введите ваше имя и фамилию:")

    @dp.message_handler()
    async def get_name(message: types.Message):
        full_name = message.text
        await message.answer("Введите номер телефона:")

        @dp.message_handler()
        async def get_phone(message: types.Message):
            phone = message.text
            await message.answer("Введите желаемую дату и время:")

            @dp.message_handler()
            async def get_datetime(message: types.Message):
                dt = message.text
                await message.answer(f"Спасибо за запись, {full_name}!
Телефон: {phone}
Дата и время: {dt}")

# Мастерская страница
@dp.message_handler(lambda message: message.text == "🛠 Я мастер")
async def master_setup(message: types.Message):
    await message.answer("Вы можете настроить вашу страницу с услугами.
(Функционал пока в разработке — доступ свободен).")

# Служба поддержки
@dp.message_handler(lambda message: message.text == "📞 Служба поддержки")
async def support(message: types.Message):
    await message.answer(f"Связаться с поддержкой: {SUPPORT_LINK}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
