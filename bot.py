from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Connected")

client.load_extension('commandCogs.helpCommands')