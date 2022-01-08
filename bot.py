from discord.ext import commands
import discord
from discord.ext.commands.help import DefaultHelpCommand

activity = discord.Activity(type=discord.ActivityType.listening, name="!helpme")

client = commands.Bot(command_prefix="!", activity=activity, help_command=None)

@client.event
async def on_ready():
    print("Connected")
    await client.get_channel(770480715279761414).send("Connected and ready to go!")

client.load_extension('commandCogs.HelpCommands')
client.load_extension('commandCogs.StatsCommands')