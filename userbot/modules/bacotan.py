from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.gk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BHAKSSSSS!**")
    sleep(1)
    await typew.edit("**ANAKK GOBLOKKKK!**")


@register(outgoing=True, pattern='^.ps(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIH!**")
    sleep(1)
    await typew.edit("**APAANSI NGENTOTT**")

@register(outgoing=True, pattern='^.cpr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSA CAPER NGENTOT GA KEREN LU BEGITU**")
    sleep(3)
    await typew.edit("**CUIHHH**")


@register(outgoing=True, pattern='^.pp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Dua tiga tutup botol**")
    sleep(1)
    await typew.edit("**Assalamualaikum kontol**")


@register(outgoing=True, pattern='^.ga(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GADA-GADA**")
    sleep(1)
    await typew.edit("**POKONYA KAGA KONTOL**")


@register(outgoing=True, pattern='^.skb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU SIAPA KONTOL**")
    sleep(1)
    await typew.edit("**SOKAB BANGET NGENTOTTT!**")


@register(outgoing=True, pattern='^.nimb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOI GOBLOK**")
    sleep(1)
    await typew.edit("**BUAT APA MASUK GC GA NIMBRUNG KONTOL!**")
    sleep(2)
    await typew.edit("**CUIH MENDING OUT AJA KONTOLL!**")


@register(outgoing=True, pattern='^.baptis(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Aku membaptis engkau dalam nama Bapa, Anak dan Roh kudus, yaitu Tuhan Yesus Kristus**")
    sleep(3)
    await typew.edit("**Aminn**")


register(outgoing=True, pattern='^.ig(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**dua tiga tutup botol, muka lu kek kontol**")
    sleep(3)
    await typew.edit("** [Si ganteng](https://t.me/mentalbrikden) | [Instagram](https://Instagram.com/xrrmli)")


CMD_HELP.update({
    "bacotan":
    "`.gk`\
\nUsage: buat goblokin.\
\n\n`.ga`\
\nUsage: buat nolak.\
\n\n`.cpr`\
\nUsage: buat ngtain cpr.\
\n\n`.baptis`\
\nUsage: buat ngebaptis.\
\n\n`.ps`\
\nUsage: paansi.\
\n\n`.nimb`\
\nUsage: Liat aja."
})
