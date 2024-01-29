import discord
from botmantik import gen_pass
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('naber lan'):
        await message.channel.send("iyiyim senden naber")
    elif message.content.startswith('alla emanet bro'):
        await message.channel.send("yine bekleriz ;D")
    elif message.content.startswith("/pass"):
        await message.channel.send(gen_pass(15))
    else:
        await message.channel.send(message.content)

client.run("token")
