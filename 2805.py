from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from key.keys import get_keyboard_1, get_keyboard_2

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('q, echobot 2 greets u', reply_markup=get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'send image')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/564x/23/ce/dd/23cedd1604e2f90c3ef9caa53702b983.jpg', caption='beautiful image, isnt it?')

@dp.message_handler(lambda message: message.text == 'image 2')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/564x/d7/9f/34/d79f34c1e5407c291578b30eef1e810d.jpg')

@dp.message_handler(lambda message: message.text == 'image 3')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/564x/76/11/eb/7611ebafc135860cbd72726674074c3a.jpg')

@dp.message_handler(lambda message: message.text == 'image 4')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/736x/40/32/c8/4032c884e8808a5e6760d9aef01a7b5f.jpg')

@dp.message_handler(lambda message: message.text == 'send another image')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/564x/13/c0/fa/13c0fae277327d626d90f69e047d34f2.jpg')

@dp.message_handler(lambda message: message.text == 'move to the next keyboard')
async def button_5_click(message: types.Message):
    await message.answer('*Moving*', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'go back to first keyboard')
async def button_8_click(message: types.Message):
    await message.answer('*Done*', reply_markup=get_keyboard_1())

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Просто отправь мне любое сообщение, и я повторю его.')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



