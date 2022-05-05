import discord
from discord.ext import commands
from replit import db

class WordFilter(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.n_list = open("n-word-list.txt", "r")
    self.list = self.n_list.readlines()

  @commands.Cog.listener()
  async def on_message(self, message):
    print("working")
    if not message.author.bot: #check if the message is from the bot
      for e in self.list:     #look for bad words
        if e.strip() in message.content:    #found a bad word
          await message.channel.send("mind your language!")
          if str(message.author) in db.keys():
            db[str(message.author)] = db[str(message.author)] + 1
          else:
            db[str(message.author)] = 0
          await message.channel.send("you have now "+str(db[str(message.author)])+"strikes")




































def setup(client):
    client.add_cog(WordFilter(client))
