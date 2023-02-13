from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6241785740:AAGB9I4cVEiJz5mHLGPxk7jjxf8N_v0O27Y'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello_command(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Здравствуй, {name}! Если ты хочешь изучить возможности (скромные) данного бота введи /help")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(f"Все, что умеет данный бот - это здороваться и возвращать квадраты чисел (если ввести число)")

@dp.message_handler()
async def raise_to_second_power(message: types.Message):
    number = message.text
    await message.reply(f"Квадрат числа: {int(number)**2}!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
