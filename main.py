import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
# We don't necessarily need message_content for slash commands,
# but it's good to keep if you still want traditional prefix commands like !ping
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 1. Define your allowed list of characters (lowercase to make matching easy)
ALLOWED_CHARACTERS = ["omega", "i hate you luigi", "mr virtual", "ultra m", "mx"]


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user} (ID: {bot.user.id})")
  # Sync slash commands with Discord so they show up in your server
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)
  print("------")


# 2. Create the slash command
@bot.tree.command(
    name="search", description="search for a character or sum [only mm characters] "
)
@app_commands.describe(
    character="The name of the character you want to search for"
)
async def search(interaction: discord.Interaction, character: str):
  # Clean up the input (make it lowercase and remove extra spaces)
  clean_character = character.strip().lower()

  # 3. Check if the character is in your allowed list
  if clean_character not in ALLOWED_CHARACTERS:
    # If not allowed, send an ephemeral message (only visible to the user who typed it)
    await interaction.response.send_message(
        f"nah, '{character}' is not on the allowed characters list.",
        ephemeral=True,
    )
    return

  # 4. If it IS allowed, generate the wiki link (or fetch data from a wiki API later!)
  wiki_url = f"https://en.wikipedia.org/wiki/{clean_character.capitalize()}"

  await interaction.response.send_message(
      f" here is the wiki page of **{character.capitalize()}**: {wiki_url}"
  )


TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
  print("Error: DISCORD_TOKEN environment variable not found!")
else:
  bot.run(TOKEN)
