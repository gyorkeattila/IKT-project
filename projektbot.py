import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


import datetime



intents = discord.Intents.all() 
client = commands.Bot(command_prefix='.', intents = intents)


@client.event
async def on_ready():
  
  global indulas
  print('Fut a bot')
  
 













client.run('Discord Token')
