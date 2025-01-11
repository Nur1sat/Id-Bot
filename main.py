import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties

import asyncio

from aiogram.types import FSInputFile, URLInputFile
from aiogram.utils.media_group import MediaGroupBuilder

API_TOKEN = 'API'

logging.basicConfig(level=logging.INFO)
bot_properties = DefaultBotProperties(parse_mode="HTML")
bot = Bot(token=API_TOKEN, default=bot_properties)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello it is id_bot!")



@dp.message(F.photo)
async def handle_photo(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.reply(f"Photo ID: {file_id}")


@dp.message(F.video_note)
async def handle_video_note(message: types.Message):
    file_id = message.video_note.file_id
    await message.reply(f"VideoNote ID: {file_id}")


@dp.message(F.video)
async def handle_video(message: types.Message):
    file_id = message.video.file_id
    await message.reply(f"Video ID: {file_id}")


@dp.message(F.file)
async def handle_document(message: types.Message):
    file_id = message.document.file_id
    await message.reply(f"Document ID: {file_id}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
