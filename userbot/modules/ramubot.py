from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu Burik`")
    sleep(1)
    await typew.edit("`Dan yang terakhir kamu kaya anjing`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**permisi kak boleh minta pap tt gak..**")


@register(outgoing=True, pattern='^.berak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Vicky Peler☑️**")
    await typew.edit("**Vicky Peler✅**")
    sleep(1)
    await typew.edit("**Toni Gilaa☑️**")
    await typew.edit("**Toni Gilaa✅**")
    sleep(2)
    await typew.edit("**Karina Depresi☑️**")
    await typew.edit("**Karina Depresi✅**")
    sleep(2)
    await typew.edit("**Yunus Gajelas☑️**")
    await typew.edit("**Yunus Gajelas✅**")
    sleep(2)
    await typew.edit("**Adel GJM!☑️**")
    await typew.edit("**Adel GJM!✅**")
    sleep(2)
    await typew.edit("**Jia GJB!☑️**")
    await typew.edit("**Jia GJB!✅**")
    sleep(2)
    await typew.edit("**Imeh,MengRibet☑️**")
    await typew.edit("**Imeh,MengRibet✅**")
    sleep(2)
    await typew.edit("**Jeje,Mengintil☑️**")
    await typew.edit("**Jeje,Mengintil✅**")
    sleep(2)
    await typew.edit("**rama jelek☑️**")
    await typew.edit("**rama jelek✅**")
    sleep(3)
    await typew.edits("**CUMA DEWALA YANG GANTENG✔︎**")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")

CMD_HELP.update({
    "rambot":
    "`.debot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.berak`\
    \nUsage: misi."
})
