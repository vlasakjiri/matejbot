# Work with Python 3.6
import discord
import random
import time

TOKEN = 'NTI2ODQzMDU5NjkxMDYxMjU4.DwLEng.drot4n9xSR-ZC1SfTT41diCAJp8'

client = discord.Client()

hovna = ["Kotoun dostane pěstí.",
         "Tak fakt díky no.",
         "Já vím, já jsem blbej.",
         "Mně tohle nejde.",
         "Horácká Slavia.",
         "Hokej.",
         "BTW Leoš mi vyhrožuje.",
         "Já mlíčko nemůžu, jsem tlustej.",
         "Jako ten mid jsi fakt posral.",
         "Jako nechci nic říkat, ale kdybys měl voida, tak bys odskočil."
         ]


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    msg = message.content.lower()
    if "matěj" in msg:
        if "mlíčko" in msg:
            await message.channel.send("Já mlíčko nemůžu, jsem tlustej.")
        elif "dota" in msg or "dotu" in msg:
            await message.channel.send("S Vlasákem hrát nebudu, nestojím o nějaký narážky.")
        elif "čůrák" in msg or "kokot" in msg or "píč" in msg:
            await message.channel.send("Tak si to fakt užijte čůráci.")
            await client.logout()
            time.sleep(5)
            client.run(TOKEN)
        else:
            await message.channel.send(random.choice(hovna))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
