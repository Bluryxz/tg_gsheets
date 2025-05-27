from aiogram import Router, F
from aiogram.types import Message

from app.gsheets import sheet_write, agcm


rt = Router()


@rt.message()
async def write(message: Message):
    text = message.text

    date = str(message.date)[:10]
    date = date[8:10] + '.' + date[5:7] + '.' + date[:4]

    client_pos = message.text.lower().find('контрагент')
    employee_pos = message.text.lower().find('сотрудник')
    responsible_pos = message.text.lower().find('исполнитель')

    name = text[:client_pos]
    client = text[client_pos + 11:employee_pos - 1]
    employee = text[employee_pos + 10:responsible_pos - 1]
    responsible = text[responsible_pos + 12:]

    print(name + '\n', date, client + '\n', employee + '\n', responsible)
    await sheet_write(agcm, name, date, client, employee, responsible)

    await message.react(
        reaction=[{'type': 'emoji', 'emoji': '👌'}]
    )