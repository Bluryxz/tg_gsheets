from aiogram import Router
from aiogram.types import Message

from app.gsheets import sheet_write, agcm
from app.funcs import find_word, remove_prespace, remove_afterorphofraphy

rt = Router()


@rt.message()
async def write(message: Message):
    text = message.text

    date = str(message.date)[:10]
    date = date[8:10] + '.' + date[5:7] + '.' + date[:4]

    client_pos = await find_word(text, 'контрагент')
    employee_pos = await find_word(text, 'сотрудник')
    responsible_pos = await find_word(text, 'исполнитель')
    
    name = text[:client_pos]
    client = text[client_pos + 13:employee_pos]
    employee = text[employee_pos + 12:responsible_pos]
    responsible = text[responsible_pos + 14:]

    client = await remove_prespace(client)
    employee = await remove_prespace(employee)
    responsible = await remove_prespace(responsible)
    responsible = await remove_afterorphofraphy(responsible)

    await sheet_write(agcm, name, date, client, employee, responsible)

    await message.react(
        reaction=[{'type': 'emoji', 'emoji': '👌'}]
    )