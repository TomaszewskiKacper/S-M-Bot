import discord
from discord.ext import commands
from replit import db


class Management(commands.Cog):
  def __init__(self, client):
      self.client = client
    
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    db[str(member)][1] = int(db[str(member)][1])+1
    await self.client.get_channel(971637156030337024).send(str(member)+" has been kicked")


  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    db[str(member)][2] = int(db[str(member)][2])+1
    await self.client.get_channel(971637156030337024).send(str(member)+" has been banned")
    f = open("txt/banned-users.txt", "w")
    f.write(str(member)+"="+reason)
    f.close()


  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    member_name, member_discriminator = member.split('#')

    for ban_entry in await ctx.guild.bans():
      user = ban_entry.user
      if (member_name == user.name) & (member_discriminator == user.discriminator):
        await ctx.guild.unban(user)
        await self.client.get_channel(971637156030337024).send(str(user)+" has been unbanned")

  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, *, amount=None):
      if amount == "all":
        await ctx.channel.purge()
      elif amount == None:
        await ctx.channel.purge(limit=10)
      else:
        await ctx.channel.purge(limit=int(amount)+1)


































def setup(client):
    client.add_cog(Management(client))
