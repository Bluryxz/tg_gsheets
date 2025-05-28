from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.gsheets import sheet_write, agcm
from app.funcs import find_word, remove_orphofraphy, get_key

rt = Router()


@rt.message(CommandStart())
async def start(message: Message):
    await message.answer('Отправьте сообщение в формате:'
    '\n<заголовок> контрагент <контрагент> сотрудник <сотрудник> исполнитель <исполнитель>')


@rt.message()
async def write(message: Message):
    text = message.text

    date = str(message.date)[:10]
    date = date[8:10] + '.' + date[5:7] + '.' + date[:4]

    client_pos = await find_word(text, 'контрагент')
    employee_pos = await find_word(text, 'сотрудник')
    responsible_pos = await find_word(text, 'исполнитель')

    pos = {'контрагент': client_pos, 'сотрудник': employee_pos, 'исполнитель': responsible_pos}

    missing = await get_key(pos, -1)

    if len(missing) != 0:
        await message.react(
        reaction=[{'type': 'emoji', 'emoji': '👎'}]     
        )

        miss_str = ''
        for i in missing:
            miss_str += f'"{i}"'

            if i != missing[len(missing) - 1]:
                miss_str += ', '

        await message.reply(f'Не заполнено: {miss_str}')

    elif client_pos > employee_pos or employee_pos > responsible_pos:
        await message.react(
        reaction=[{'type': 'emoji', 'emoji': '👎'}]     
        )
        await message.reply('Отправьте сообщение в формате:'
    '\n<заголовок> контрагент <контрагент> сотрудник <сотрудник> исполнитель <исполнитель>')    
    
    else:            
        name = text[:client_pos]
        client = text[client_pos + 11:employee_pos]
        employee = text[employee_pos + 10:responsible_pos]
        responsible = text[responsible_pos + 12:]

        name = await remove_orphofraphy(name)
        client = await remove_orphofraphy(client)
        employee = await remove_orphofraphy(employee)
        responsible = await remove_orphofraphy(responsible)

        await sheet_write(agcm, name, date, client, employee, responsible)

        await message.react(
            reaction=[{'type': 'emoji', 'emoji': '👌'}]
        )