from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from pythonbot.keyboards.for_navigate import keyboard

private_router = Router()


@private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.reply('Hello', reply_markup=keyboard)


@private_router.message(Command('about'))
async def about(message: Message):
    await message.answer('This bot about computer games')


@private_router.message((F.text.lower() == 'hello') | (F.text.lower() == 'hi'))
async def options(message: Message):
    await message.answer('Hello, nice to meet you')





