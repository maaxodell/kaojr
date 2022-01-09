from discord.ext import commands
from datetime import datetime
import pytz

class StatsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="display your personal stats within the server and its text channels")
    async def stats(self, ctx):
        with ctx.channel.typing():
            
            messageCounter = 0

            tz = pytz.timezone('Australia/Queensland')
            joinedDate = ctx.author.joined_at.astimezone(tz)
            now = datetime.now(tz)
            delta = now - joinedDate

            async for message in ctx.channel.history(limit=None):
                if message.author == ctx.author:
                    messageCounter += 1

            await ctx.reply("__**Your stats, {}:**__\n:clock10: A member of {} for `{} days`\n:pencil: {} messages sent to the channel `{}`"
            .format(ctx.author.name, ctx.guild.name, delta.days, messageCounter, ctx.channel))

def setup(bot):
    bot.add_cog(StatsCommands(bot))