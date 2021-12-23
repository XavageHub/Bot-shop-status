import os
from aiohttp.helpers import TOKEN 
import dotenv
from discord.ext import commands
import discord

dotenv.load_dotenv()

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print(f'Success log in as {client.user}')


@client.event
async def on_message(message):
    await client.process_commands(message)


# commands

@client.command()
async def open(cxt):
    await cxt.channel.send(f'@everyone')
    emBed = discord.Embed(title="สถานะร้าน🟢เปิด", description="กดticket เพื่อติดต่อการซื้อ ", color=0x32CD32, inline=True)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/906770280683307039/923653954171179098/aLpNLwz_700b.png')
    await cxt.channel.send(embed=emBed)



@client.command()
async def close(cxt):
    await cxt.channel.send(f'@everyone')
    emBed = discord.Embed(title="สถานะร้าน🔴ปิด", description="เจอกันเช้าครับฝรรดี", color=0x960F00, inline=False)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/906770280683307039/923654153417424956/2010_CN_bigstock-gray-striped-kitten-beautiful-376439455.png')
    await cxt.channel.send(embed=emBed)



TOKEN = 'OTIzNjQ1Nzk4MjY3MzU1MjM3.YcTCLg.Py-FQj5oS2ZO6mRlpGr-rX9_I58'

client.run(TOKEN)

