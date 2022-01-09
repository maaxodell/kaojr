from discord.ext import commands
import discord
from datetime import datetime
from resources import devChannelID

activity = discord.Activity(type=discord.ActivityType.listening, name="!helpme")

client = commands.Bot(command_prefix="!", activity=activity, help_command=None)

@client.event
async def on_ready():
    time = datetime.now().strftime("%I:%M:%S %p")
    await client.get_channel(devChannelID).send("`Connected at {}`".format(time))

client.load_extension('commandCogs.HelpCommands')
client.load_extension('commandCogs.StatsCommands')