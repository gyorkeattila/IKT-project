import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


import datetime

import ffmpeg
from discord import FFmpegPCMAudio

from discord import voice_client
from discord.utils import get


intents = discord.Intents.all() 
client = commands.Bot(command_prefix='.', intents = intents)


@client.event
async def on_ready():
  
  global indulas
  print('Fut a bot')
  
#ping
@client.command()
async def ping(ctx):
        embedVar = discord.Embed(title="Bot válaszideje")
        embedVar.add_field(name="Válaszidő", value=f'{round(client.latency * 1000)}ms', inline=False)
        await ctx.channel.send(embed=embedVar)
  
  
#zene
@client.command()
async def zene(ctx):
    user = ctx.author.voice
    if user is not None:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="C:/Users/ati42/Desktop/ffmpeg-2021-09-01-git-c500dc7cca-full_build/bin/ffmpeg.exe", source=r"C:\Users\ati42\Desktop\Wenseron botja\friday.mp3"))
    else:
        await ctx.send("Nem vagy bent egy hangcsatornában sem")

 














client.run('Discord Token')
