from pyrogram import Client, filters
from pyrogram.types import Message

async def eor(_, m, t):
    try:
        await m.edit(t)
    except:
        await m.reply(t)
        await m.delete()
