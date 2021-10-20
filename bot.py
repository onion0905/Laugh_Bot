import discord
from discord import channel
from discord.ext import commands
import json
import random
import os
import keep_alive
import pandas as pd
invite = False

intents = discord.Intents.default()
intents.members = True

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="-", intents = intents)

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

@bot.event
async def on_ready():
    channel = bot.get_channel(858221992390295553) # 858221992390295553
    print("Bot Ready")
    with open("save.md", "a", encoding="utf8") as mddata:
        async for message in channel.history(limit=1000):   # As an example, I've set the limit to 10000
            mddata.write(message.content)
            if len(message.attachments) > 0:
                attachment = message.attachments[0]
                mddata.write(attachment.url)
            mddata.write("\n")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension} done")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"unloaded {extension} done")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"reloaded {extension} done")





if __name__ == "__main__":
    #keep_alive.keep_alive()
    bot.run(jdata["laugh_TOKEN"])


    