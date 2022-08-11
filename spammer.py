from pyrogram import Client as Alpha, filters, idle
from pyrogram.types import Message
from config import *
import time
from helper import eor

Alf = Alpha("yashu-alpha", api_id = API_ID, api_hash = API_HASH, session_string = STRING_SESSION)

stop = False

@Alf.on_message(filters.command("spam", "!"))
async def spammer(_, m):
    global stop
    try:
        SUDO.append(str(level))
    except:
        pass
    if not str(m.from_user.id) in SUDO:
        return
    if len(m.command) != 4:
        return await m.reply(f"<code>Usage: !spam < count > < delay > < text ></code>")
    hehe = m.text.split(None, 3)
    counter = hehe[1]
    txt = hehe[3]
    delay = hehe[2]
    for alpha in range(0, int(counter)):
        if stop:
            stop = False
            return
        await _.send_message(m.chat.id, txt)
        time.sleep(int(delay))

@Alf.on_message(filters.command("endspam", "!"))
async def spamend(_, m):
    global stop
    try:
        SUDO.append(str(level))
    except:
        pass
    if not str(m.from_user.id) in SUDO:
        return
    ok = await eor(_, m, "terminating process....")
    stop = True
    time.sleep(5)
    await ok.delete()


if not YA == "YashuAlpha":
    print("Password wrong !")
else:
    Alf.start()
    me = Alf.get_me()
    level = me.id
    uname = me.username
    idle()
    print(f"@{uname if uname else None} started successfully... ")

