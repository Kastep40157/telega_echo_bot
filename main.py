from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '7085892602:AAHIy0575CZ2FU79DtqU1ABWUxAh994BN5s'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

#  хендлер обработки команды Start
@dp.message(Command(commands=['start']))
async def start_process_command(message: Message):
    await message.answer('Привет! я Эхо- Бот.\n Напиши мне что-нибудь')


#Хэндлер обработки команды Help
@dp.message(Command(commands=['help']))
async def help_process_command(message: Message):
    await message.answer(('Отправь сообщение и бот пришлет тебе его обратно'))

#хэндлер для обработки изображений
#@dp.message(F.photo)
#async def send_photo(message: Message):
 #   await message.reply_photo(message.photo[0].file_id)
  #  print(message)

  #Хендлер обработки текстовых сообщений
#@dp.message()
#async def send_text(message: Message):
#    await message.answer(text=message.text)

# Хэндлер обработки входящих всех видов сообщений
@dp.message()
async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)


if __name__ == '__main__':
    dp.run_polling(bot)