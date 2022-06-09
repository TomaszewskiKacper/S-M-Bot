import discord
from discord.ext import commands
from replit import db
from serpapi import GoogleSearch
import os
import random

class Images(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.last_query = "base"
  
  def gsearch(self, q = "base"):
    params = {
      "engine": "google",
      "q": q,
      "location": "Austin, Texas, United States",
      "google_domain": "google.com",
      "gl": "us",
      "hl": "en",
      "num": "10",
      "tbm": "isch",
      "nfpr": "1",
      "ijn": 0,
      "api_key": os.environ['SEPAPI_TOKEN']
          }
    file = open("./extensions/img/"+str(q)+".txt","a")
    
    search = GoogleSearch(params)
    image_results = []
    image_exists = True
    while image_exists:
      results = search.get_dict()

      if "error" not in results:
        for image in results["images_results"]:
          if image["original"] not in image_results:
            image_results.append(image["original"])
        params["ijn"] += 1  #next page
        
      else:
        image_exists = False

    for e in image_results:
      file.write(e+"\n")
    
    file.close()

  
  
  @commands.command()
  async def r(self, ctx, *, q="nnn"):
    if q == "nnn":
      q = self.last_query
    if str(q)+".txt" not in os.listdir("./extensions/img"):
      self.gsearch(q)
      print("true")
    self.last_query = str(q)
    file = open("./extensions/img/"+str(q)+".txt", "r")
    images = file.readlines()
    file.close()
    image = images[random.randint(0,len(images)-1)]
    await ctx.send(image.strip())

        


















def setup(client):
    client.add_cog(Images(client))
