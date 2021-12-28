import discord
from discord.ext import commands

client = commands.Bot(command_prefix='e!')

@bot.event()
async def on_ready():
  print(f"imded")

client.run()
