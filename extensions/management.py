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

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(ctx, amount=None):
      if amount == "all":
        await ctx.channel.purge()
      elif amount == None:
        await ctx.channel.purge(limit=10)
      elif isinstance(amount, int):
        await ctx.channel.purge(limit=amount+1)


































def setup(client):
    client.add_cog(Management(client))
