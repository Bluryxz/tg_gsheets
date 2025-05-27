import gspread_asyncio
from gspread_formatting import *

from google.oauth2.service_account import Credentials


def get_creds():

    creds = Credentials.from_service_account_file("service_account.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)


async def sheet_write(agcm, name, date, client, employee, responsible):
    agc = await agcm.authorize()

    sh = await agc.open("апи тест")
    sh = await sh.get_worksheet(0) 
    
    number = 1
    i = 1
    cell = await sh.cell(i, 1)

    while cell.value != None:

        try:
            if int(cell.value) > number:
                number = int(cell.value) + 1
        except ValueError:
            pass

        i += 1
        cell = await sh.cell(i, 1)

    await sh.update_cell(i, 1, number)
    await sh.update_cell(i, 2, name)
    await sh.update_cell(i, 7, date)
    await sh.update_cell(i, 9, client)
    await sh.update_cell(i, 10, employee)
    await sh.update_cell(i, 11, responsible)
    
    

