from pyrogram import Client as Alpha, filters
from pyrogram.types import Message
from config import *
import time
import datetime 

Alf = Alpha("yashu-alpha", api_id = API_ID, api_hash = API_HASH, session_string = STRING_SESSION)



@Alf.on_message(filters.command("addall", "!"))
async def add(_, m):
    l = m.chat.id
    try:
        myid = await Alf.get_me().id
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
        return await _.send_message(m.chat.id, "provide only group id !")
    if str(id)[0] != "-":
        return await _.send_message(l, "⚠️ provide valid group id !")
    ok = await _.send_message(l, "➕ adding users from given group id !")
    if m.chat.type == "private":
        await ok.edit("try this command in groups !")
    MEM = []
    async for mem in _.get_chat_members(id):
        if (not mem.user.is_bot and not mem.user.is_deleted):
            MEM.append(mem.user.id)
            if len(MEM) == 30:
                break
    startica = datetime.datetime.now()
    a = 0
    for lnk in MEM:
        try:
            await _.add_chat_members(l, lnk)
            a += 1
            time.sleep(2)
        except:
            pass
        endica = datetime.datetime.now()
        diffica = (endica - startica).microseconds / 1000
        if diffica >= 120:
            break

    a = str(a)
    await ok.edit(f"successfully added {a} users ! 🎉")
    time.sleep(10)
    await ok.delete()

@Alf.on_message(filters.command("reboot", "!"))
async def rboot(_, m):
    await m.delete()
    ok = await m.reply("Reloading Dev-Op 🇮🇳🎊🎉 Scrapper !")
    reboot()
    await ok.delete()
    if reboot:
        await _.send_message(l, "Successfully Reloaded in <code>{diff}</code> sec ! ✨💫")
    else:
        await _.send_message(l, "Reload failed, report @Timeisnotwaiting")

def reboot():
    start = datetime.datetime.now()
    try:
        Alf.stop()
        Alf.run()
        end = datetime.datetime.now()
        diff = (end-start).microseconds / 1000
        return diff, True
    except:
        diff = 0
        return diff, False
    

if YA == "YashuAlpha":
    Alf.run()
    print("Pyro adder started successfully 🇮🇳🎊🎉")
else:
    print("password you entered is wrong")
