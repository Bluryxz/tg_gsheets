from aiogram import Router, F
from aiogram.types import Message

from app.gsheets import sheet_write, agcm


rt = Router()


@rt.message()
async def write(message: Message):
    text = message.text

    date = message.date
    client_pos = message.text.lower().find('контрагент')
    employee_pos = message.text.lower().find('сотрудник')
    responsible_pos = message.text.lower().find('исполнитель')

    name = text[:client_pos - 1]
    client = text[client_pos : employee_pos - 1]
    employee = text[employee_pos : responsible_pos - 1]
    responsible = text[responsible_pos:]

    print(name, date, client, employee, responsible)
    await sheet_write(agcm, name, date, client, employee, responsible)

    await message.react(
        reaction=[{'type': 'emoji', 'emoji': '👌'}]
    )