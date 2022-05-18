import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event  #when bot is Online
async def on_ready():
  await client.get_channel(971637156030337024).send("I'm online!")  


@client.command()  #load commands
@commands.is_owner()
async def load(ctx, item):
  try:
    client.load_extension("extensions."+item)
    await client.get_channel(971637156030337024).send("loaded " + item)
  except:
    await client.get_channel(971637156030337024).send("already loaded")

@client.command()  #unload command
@commands.is_owner()
async def unload(ctx, item):
  try:
    client.unload_extension("extensions."+item)
    await client.get_channel(971637156030337024).send("unloaded " + item)
  except:
    await client.get_channel(971637156030337024).send("already unloaded")


@client.command()  #reload command
@commands.is_owner()
async def reload(ctx, item):
  if item == "all":
    for f in os.listdir("./extensions"):
      if f.endswith(".py"):
        try:
          client.reload_extension(f'extensions.'+f[:-3])
          await client.get_channel(971637156030337024).send("reloaded "+f[:-3])
        except:
          print(str(f)+" is alredy loaded")
  else:
    try:
      client.reload_extension("extensions."+item)
      await client.get_channel(971637156030337024).send("reloaded " + item)
    except:
      try:
        client.load_extension("extensions."+item)
      except:
        await client.get_channel(971637156030337024).send("could not find the module")

  
#load all when the Bot starts
for f in os.listdir("./extensions"):
    if f.endswith(".py"):
        client.load_extension(f'extensions.'+f[:-3])

client.run(os.environ['token'])