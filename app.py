import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


bot = commands.Bot(command_prefix="$sheet ")
load_dotenv(".env.local")
token = os.getenv("DISCORD_TOKEN")

bot.load_extension("commands")

bot.run(token)