import asyncio
import gspread_asyncio

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


async def sheet_write(agcm, text):
    agc = await agcm.authorize()

    sh = await agc.open("апи тест")
    sh = await sh.get_worksheet(0) 
    
    i = 1
    cell = await sh.cell(i, 1)

    while cell.value != None:
        i += 1
        cell = await sh.cell(i, 1)

    await sh.update_cell(i, 1, text)


