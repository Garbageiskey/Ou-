import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!!!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with 1 Server"))                               
    print('Ready, Freddy')

node_modules/ :

package-lock.json
.idea/

@client.event
async def on_message(message):
      if message.content == 'ouo.test':
        await client.send_message(message.channel,'TEST')
      if message.content == 'ouo.globalemotetest':                           
        await client.send_message(message.channel,':Clyde:')
        

client.run('NTM4MTMxNzcyNTI1NzcyODAx.DyvXfA.t4B6oSElwAg-q9jjB23Jtb90-_g')



