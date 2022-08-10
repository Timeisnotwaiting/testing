from pyrogram import Client as Alpha, filters
from pyrogram.types import Message
from config import *
import time

Alf = Alpha("yashu-alpha", api_id = API_ID, api_hash = API_HASH, session_string = STRING_SESSION)

level = None

@Alf.on_message(filters.command("spam", "!"))
async def spammer(_, m):
    try:
        SUDO.append(str(level))
    except:
        pass
    if not str(m.from_user.id) in SUDO:
        return
    if len(m.command) == 1:
        return await m.reply("Usage: !spam < count > < delay > < text >")
    hehe = m.text.split(None, 3)
    counter = hehe[1]
    txt = hehe[3]
    delay = hehe[2]
    for alpha in range(0, int(counter)):
        await _.send_message(m.chat.id, txt)
        time.sleep(int(delay))

@Alf.on_message(filters.command("endspam", "!"))
async def spamend(_, m):
    try:
        SUDO.append(str(level))
    except:
        pass
    if not str(m.from_user.id) in SUDO:
        return


if not YA == "YashuAlpha":
    print("Password wrong !")
else:
    Alf.start()
    me = Alf.get_me()
    level = me.id
    uname = me.username
    print(f"@{uname if uname else None} started successfully... ")

