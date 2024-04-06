import os, discord, urllib.request
from discord.ext import commands


# Set the token.
f = open('config.txt', 'r')
token = f.read()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.hybrid_command()
async def active_developer_badge(ctx: commands.Context):
    embed = discord.Embed(title="Program Ran Successfully",
                          description="**+** You have ran the bot correctly and have claimed your Discord Developer Badge. \n\n**+** It may take up to 24 hours or a tiny bit more for your badge to shop up here (https://discord.com/developers/active-developer)\n\n**+** Please don't forget to star the repository on github! (https://github.com/oxy-szn/Active-Discord-Developer-Badge)",
                          colour=0x00f53d)

    embed.set_footer(text="This bot has been made by oxy.szn")

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("im ready")
    await bot.tree.sync()

bot.run(token)
