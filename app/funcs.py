async def remove_orphography(text, pos):
    if text[pos - 2] == '.' or text[pos - 2] == ',' or text[pos - 2] == ':':
        return pos - 2
    else:
        return pos - 1
    

async def find_word(text, word):
    pos = text.lower().find(word)
    pos = await remove_orphography(text, pos)
    return pos


async def remove_prespace(text):
    if text[0] == ' ':
        return text[1:]
    else:
        return text
    

async def remove_afterorphofraphy(text):
    length = len(text)
    if text[length - 1] == '.' or text[length - 1] == ',' or text[length - 1] == ':':
        return text[:length - 2]
    else:
        return text