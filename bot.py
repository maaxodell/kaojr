from discord.ext import commands
import discord

activity = discord.Activity(type=discord.ActivityType.listening, name="@kaø")

client = commands.Bot(command_prefix="!", activity=activity)

@client.event
async def on_ready():
    print("Connected")
    await client.get_channel(770480715279761414).send("Connected and ready to go!")

client.load_extension('commandCogs.HelpCommands')