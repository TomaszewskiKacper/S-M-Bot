import discord
from discord.ext import commands


class Debug(commands.Cog):
  def __init__(self, client):
      self.client = client


  @commands.command()
  async def whereAmI(self, ctx):
    await ctx.send(str(ctx.channel)+": "+str(ctx.channel.id))

  @commands.command()
  async def whoAmI(self, ctx):
    await ctx.send(str(ctx.author)+": "+str(ctx.author.id))































def setup(client):
    client.add_cog(Debug(client))
