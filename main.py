import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def send_message(ctx):
    await ctx.send(f"what's good globe")

bot.run(TOKEN)