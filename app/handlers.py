from aiogram import Router, F
from aiogram.types import Message

from app.gsheets import sheet_write, agcm


rt = Router()


@rt.message(F.text.startswith('Записать') | F.text.startswith('записать'))
async def write(message: Message):
    text = message.text[9:]

    await sheet_write(agcm, text)

    await message.react(
        reaction=[{'type': 'emoji', 'emoji': '👌'}]
    )