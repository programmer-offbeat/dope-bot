import discord,os
from dotenv import load_dotenv
from jishaku.cog import jishaku
from discord.ext import commands

client = commands.Bot(command_prefix='e!')

@bot.event()
async def on_ready():
  print(f"imded")

client.load_extension('jishaku')
client.run(os.getenv('TOKEN'))
