import discord,os
from dotenv import load_dotenv
from jishaku.cog import Jishaku
from discord.ext import commands

client = commands.Bot(command_prefix='e!')

@client.event
async def on_ready():
  print("imded")

client.load_extension('jishaku')
client.run(os.getenv('TOKEN'))
