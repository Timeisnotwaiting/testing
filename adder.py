from pyrogram import Client as Alpha, filters
from pyrogram.types import Message
import config

Alf = Alpha(STRING_SESSION, API_ID, API_HASH)

@Alf.on_message(filters.command("addall", "."))
async def add(_, m):
    l = m.chat.id
    if not m.from_user.id in SUDO:
        return
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
            await _.add_chat_members(l, lnk):
            a += 1
        except:
            pass
        if a == 50:
            break
    a = str(a)
    await ok.edit(f"successfully added {a} users ! 🎉")
        
    
    
