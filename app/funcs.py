async def find_word(text, word):
    pos = text.lower().find(word)
    return pos


async def remove_space(text):
    if text[0] == ' ':
        text = text[1:]

    if text[len(text) - 1] == ' ':
        text = text[:len(text) - 1]

    return text
    
        
async def remove_orphofraphy(text):
    text = await remove_space(text)
    
    length = len(text)
    if text[length - 1] == '.' or text[length - 1] == ',' or text[length - 1] == ':':
        text = text[:length - 1]

    if text[0] == '.' or text[0] == ',' or text[0] == ':':
        text = text[1:]

    text = await remove_space(text)

    return text


async def get_key(dictionary, value):
    list = []
    for k, v in dictionary.items():
        if v == value:
            list.append(k)
    
    return list
    