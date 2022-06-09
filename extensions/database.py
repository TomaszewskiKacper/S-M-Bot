import discord
from discord.ext import commands
from replit import db


db_name = ["messages","strikes", "kicks", "bans", "commands used", "times mentioned by someone"]

class Database(commands.Cog):
  def __init__(self, client):
    self.client = client

#commands
  @commands.command()  #show database  
  async def db_show(self, ctx):
    for e in db.keys(): 
      await ctx.send(str(e)+":\t\t strikes = "+str(db[e][0])+" | kicks = "+str(db[e][1])+" | bans = "+str(db[e][2]))

      
  @commands.command()  #clear database
  async def db_clear(self, ctx):
    for e in db.keys():
      del db[e]


  @commands.command()  #update database
  async def db_update(self, ctx):
    for e in ctx.guild.members:
      if not (str(e) in db.keys()):
        db[str(e)] = [0,0,0,0,0]


  @commands.command()  #show stats of a user
  async def db_stats(self, ctx, member : discord.Member):
    print(str(member))
    if str(member) in db.keys():
      i=0
      for e in db_name:
        await ctx.send(e+": "+str(db[str(member)][i]))
        i=i+1


#adding to database
  @commands.Cog.listener()  #add member to database when user joins
  async def on_member_join(self, member):
    if not (str(member) in db.keys()):
        db[str(member)] = [0,0,0,0,0]

  
  @commands.Cog.listener()  #number of messages sent
  async def on_message(self, message : discord.Message):
    db[str(message.author)][0] = db[str(message.author)][0] + 1  #add message count
    if str(message.content).startswith("!"):
      db[str(message.author)][4] = db[str(message.author)][4] + 1
    

  @commands.Cog.listener()  #number of messages sent
  async def on_member_ban(self, guild, user):
    db[str(user)][3]=db[str(user)][3]+1
    
  













def setup(client):
    client.add_cog(Database(client))
