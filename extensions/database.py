import discord
from discord.ext import commands
from replit import db


db_name = ["messages","strikes", "kicks", "bans"]

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
        db[str(e)] = [0,0,0]
      


#adding to database
  @commands.Cog.listener()  #add member to database when user joins
  async def on_member_join(self, member):
    if not (str(member) in db.keys()):
        db[str(member)] = [0,0,0]


  @commands.Cog.listener()  #number of messages sent
  async def on_member_ban(self, guild, user):
    db[str(user)][0]=db[str(user)][0]+1



















def setup(client):
    client.add_cog(Database(client))
