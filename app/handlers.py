from aiogram import Router, F
from aiogram.types import Message


rt = Router()


@rt.message(F.text.startswith('Записать') | F.text.startswith('записать'))
async def write(message: Message):
    text = message.text[9:]
    print(f'Текст для записи: {text}')