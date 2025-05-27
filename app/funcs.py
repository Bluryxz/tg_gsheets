async def remove_orphography(text, pos):
    if text[pos] == '.' or text[pos] == ',' or text[pos] == ':':
        return pos + 1
    else:
        return pos
    

async def find_word(text, word):
    pos = text.lower().find(word)
    pos = await remove_orphography(text, pos)
    return pos