from bottery.message import render
from bottery.platform import telegram

from hashid import HashID

async def start(message):
    return render(message, "start.md")

@telegram.reply(lambda message: message.id - 1)
async def hashid(message):
    hash = message.text.replace("hashid ", "")
    hashid = HashID()
    hash_id = list(hashid.identifyHash(hash))
    if len(hash_id) == 0:
        return "No match!"
    else:
        hash_id = [" - " + hash.name for hash in hash_id]
        message = "We found these possible matches:\n"
        if len(hash_id) > 5:
            return message + "\n".join(hash_id[:5])
        else:
            return message + "\n".join(hash_id)
