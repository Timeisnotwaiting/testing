from pyrogram import Client as Alpha, filters
from pyrogram.types import Message
from config import *
import time

Alf = Alpha("yashu-alpha", api_id = API_ID, api_hash = API_HASH, session_string = STRING_SESSION)

Reboot = False

@Alf.on_message(filters.command("addall", "!"))
async def add(_, m):
    l = m.chat.id
    try:
        myid = await _.get_me()["id"]
        SUDO.append(str(myid))
    except:
        pass
    if not str(m.from_user.id) in SUDO:
        return
    try:
        await m.delete()
    except:
        pass
    try:
        id = int(m.text.split(None, 1)[1])
    except:
        return await _.send_message(m.chat.id, "provide only group id")
    if str(id)[0] != "-":
        return await _.send_message(l, "provide valid group id")
    ok = await _.send_message(l, "adding users from given group id")
    if m.chat.type == "private":
        await ok.edit("try this command in groups")
    MEM = []
    async for mem in _.get_chat_members(id):
        if (not mem.user.is_bot and not mem.user.is_deleted):
            MEM.append(mem.user.id)
    a = 0
    for lnk in MEM:
        try:
            await _.add_chat_members(l, lnk)
            a += 1
            time.sleep(2)
        except:
            pass
        if a == 50:
            break
    a = str(a)
    await ok.edit(f"successfully added {a} users ! 🎉")
    time.sleep(10)
    await ok.delete()

@Alf.on_message(filters.command("reboot", "!"))
async def rboot(_, m):
    global Reboot
    await m.delete()
    ok = await m.reply("Reloading Dev-Op 🇮🇳🎊🎉 scrapper !")
    Reboot = True

if Reboot:
    Alf.stop()
    Alf.run()
    

if YA == "YashuAlpha":
    Alf.run()
    print("Pyro adder started successfully 🇮🇳🎊🎉")
else:
    print("password you entered is wrong")
