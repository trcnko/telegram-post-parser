import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from keywords import is_target_hashtag, format_post
from sheets import SheetsClient

dp = Dispatcher()
sheets_client = SheetsClient()

@dp.channel_post()
async def handle_channel_post(message):
    text = message.text
    if is_target_hashtag(text):
        formatted = format_post(text)
        # print(f'Пост обработан: {formatted}')
        sheets_client.append_to_b1(formatted)

async def run_bot():
    bot = Bot(token=settings.BOT_TOKEN)
    print('Бот запущен')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())
