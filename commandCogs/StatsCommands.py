from discord.ext import commands
from datetime import datetime

devChannelID = "770480715279761414"

class StatsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        with ctx.channel.typing():
            
            messageCounter = 0
            joinedDate = ctx.author.joined_at
            now = datetime.now()
            delta = now - joinedDate

            async for message in ctx.channel.history(limit=None):
                if message.author == ctx.author:
                    messageCounter += 1

            await ctx.reply("__**Your stats, {}:**__\n:clock10: A member of {} for `{} days`\n:pencil: {} messages sent to the channel `{}`"
            .format(ctx.author.name, ctx.guild.name, delta.days, messageCounter, ctx.channel))

def setup(bot):
    bot.add_cog(StatsCommands(bot))