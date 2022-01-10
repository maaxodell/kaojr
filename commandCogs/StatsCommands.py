# Module imports
from discord.ext import commands
from datetime import datetime
import pytz

class StatsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="display your personal stats within the server and its text channels")
    async def stats(self, ctx):
        with ctx.channel.typing():
            
            # Get time spent in server
            tz = pytz.timezone('Australia/Queensland')
            joinedDate = ctx.author.joined_at.astimezone(tz)
            now = datetime.now(tz)
            delta = now - joinedDate

            # Get messages sent to current channel
            messageCounter = 0
            async for message in ctx.channel.history(limit=None):
                if message.author == ctx.author:
                    messageCounter += 1

            # Send reply containing user's stats  
            await ctx.reply("__**Your stats, {}:**__\n:clock10: A member of {} for `{} days`\n:pencil: {} messages sent to the channel `{}`"
            .format(ctx.author.name, ctx.guild.name, delta.days, messageCounter, ctx.channel))

    @commands.command(help="display your stats across the whole server (WIP)")
    async def globalstats(self, ctx):
        with ctx.channel.typing():
            
            # Get messages sent server-wide
            messageCounter = 0
            for channel in ctx.guild.text_channels:
                async for message in channel.history(limit=None):
                    if message.author == ctx.author:
                        messageCounter += 1
            
            await ctx.reply("{} messages sent globally".format(messageCounter))

def setup(bot):
    bot.add_cog(StatsCommands(bot))