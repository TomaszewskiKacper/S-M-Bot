import discord
from discord.ext import commands
from replit import db

class WordFilter(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.n_list = open("txt/n-word-list.txt", "r")
    self.list = self.n_list.readlines()
    self.n_list.close()

  
  @commands.Cog.listener()
  async def on_message(self, message):
    if not message.author.bot: #check if the message is from the bot
      for e in self.list:     #look for bad words
        if e.strip() in message.content:    #found a bad word
          await message.channel.send("mind your language!")
          db[str(message.author)][0] = int(db[str(message.author)][0]) + 1
          await message.channel.send("you have now "+str(db[str(message.author)][0])+" strikes")


  @commands.command()
  async def n_add(self, ctx, *, word):
    if word not in self.list:
      self.list.append(word+"\n")
      f = open("txt/n-word-list.txt", "a")
      f.write(word+"\n")
      f.close()
      print("test")

      
    
  @commands.command()
  async def n_list(self, ctx):
    s = ""
    for e in self.list:
      s = s + ", "  + e.strip()
    await ctx.send(s)

































def setup(client):
    client.add_cog(WordFilter(client))
