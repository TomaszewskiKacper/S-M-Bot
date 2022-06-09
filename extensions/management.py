import discord
from discord.ext import commands
from replit import db
import datetime


class Management(commands.Cog):
  def __init__(self, client):
      self.client = client
    
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    db[str(member)][2] = int(db[str(member)][2])+1
    await self.client.get_channel(971637156030337024).send(str(member)+" has been kicked")


  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
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


  @commands.command()
  @commands.has_role("Admin")
  async def add_role(self, ctx, member: discord.Member, r_name = "Test"):
    roles = ctx.message.guild.roles
    role = discord.utils.get(roles, name = r_name)
    print(role)
    await member.add_roles(role)



  @commands.command()
  @commands.has_role("Admin")
  async def create_role(self, ctx, r_name = "Test"):
    guild = ctx.message.guild
    await guild.create_role(name=r_name)

  @commands.command()
  @commands.has_role("Admin")
  async def remove_role(self, ctx, member: discord.Member, r_name = "Test"):
    roles = ctx.message.guild.roles
    role = discord.utils.get(roles, name = r_name)
    print(role)
    await member.remove_roles(role)


  @commands.command()
  @commands.has_role("Admin")
  async def delete_role(self, ctx, r_name = "Test"):
    guild = ctx.message.guild
    roles = guild.roles
    role = discord.utils.get(roles, name = r_name)
    await role.delete()


  @commands.command()
  @commands.has_role("Admin")
  async def create_text_channel(self, ctx, name):
    guild = ctx.message.guild
    await guild.create_text_channel(name)
  

  @commands.command()
  @commands.has_role("Admin")
  async def delete_channel(self, ctx, r_name = "Test"):
    guild = ctx.message.guild
    channels = guild.channels
    channel = discord.utils.get(channels, name = r_name)
    await channel.delete()


  @commands.command()
  @commands.has_role("Admin")
  async def create_voice_channel(self, ctx, name):
    guild = ctx.message.guild
    await guild.create_voice_channel(name)
  






def setup(client):
    client.add_cog(Management(client))
