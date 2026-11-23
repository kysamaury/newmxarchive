import os
import discord
from discord.ext import commands

# 1. Set up intents (permissions your bot needs)
intents = discord.Intents.default()
intents.message_content = (
    True  # Allows the bot to read message content if enabled
)

# 2. Initialize the bot with a command prefix (e.g., !hello)
bot = commands.Bot(command_prefix="!", intents=intents)


# 3. Event: Runs once when the bot successfully logs in and connects
@bot.event
async def on_ready():
  print(f"Logged in as {bot.user} (ID: {bot.user.id})")
  print("------")
  
# 5. Run the bot using your secret token from the environment
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
  print("Error: DISCORD_TOKEN environment variable not found!")
else:
  bot.run(TOKEN)
