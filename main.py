import os
import discord
from discord.ext import commands, tasks
import web_scraper as ws
import helper
from web_server import keep_alive

token = os.environ["token"]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
  print("We have logged in as {0.user}".format(bot))

  auto_send.start()

@bot.command()
async def check(ctx):
  result = ws.scrape()
  
  await ctx.send(result)

@tasks.loop(minutes = 30)
async def auto_send():
  result = ws.scrape()

  not_posted = helper.check_similar_post(result)

  if not_posted == True:
    channel = await bot.fetch_channel(os.environ["UofT Safety Alert Channel"])
    await channel.send(result)

keep_alive()
bot.run(token)