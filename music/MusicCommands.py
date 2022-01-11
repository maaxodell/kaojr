import discord
from discord.ext import commands
import youtube_dl
from resources import musicChannelID
from datetime import timedelta

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    songMessage = None
    pauseReaction = "\u23F8"

    async def checkMessage(self, ctx):
        # Check if user in a voice channel to join
        if ctx.author.voice is None:
            await ctx.reply("It doesn't look like you're in a voice channel!")
            return False

        # Check for music channel
        if not ctx.channel.id == musicChannelID:
            await ctx.reply("Please use {} for music commands.".format(self.bot.get_channel(musicChannelID).mention))
            return False

        return True

    @commands.command(help="")
    async def join(self, ctx):
        if not await self.checkMessage(ctx):
            return

        vc = ctx.author.voice.channel
        if ctx.voice_client is None:
            await vc.connect()
        else:
            await ctx.voice_client.move_to(vc)

    @commands.command(aliases=['dc', 'leave'], help="")
    async def disconnect(self, ctx):
        if not await self.checkMessage(ctx):
            return

        await ctx.voice_client.disconnect()

    @commands.command(help="")
    async def play(self, ctx, url=None):
        with ctx.channel.typing():
            if not await self.checkMessage(ctx):
                return
            
            # Check for different voice channel
            if ctx.voice_client is None or not ctx.author.voice.channel == ctx.voice_client.channel:
                await ctx.reply("Looks like we're not in the same voice channel - use `{}join`.".format(self.bot.command_prefix))
                return

            #Check for missing URL
            if url is None:
                await ctx.reply("Missing URL!")
                return

            # Delete original command message
            await ctx.message.delete()

            FFMOPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': 'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                title = info.get('title', None)
                duration = str(timedelta(seconds=info.get('duration', None))) 
                source = await discord.FFmpegOpusAudio.from_probe(url2,
                **FFMOPTIONS)
                vc.play(source)
        
        self.songMessage = await ctx.send(":loud_sound: `{} [{}]` - {}".format(title, duration, ctx.author.name))

    @commands.command(help="")
    async def pause(self, ctx):
        if not await self.checkMessage(ctx):
            return

        ctx.voice_client.pause()
        await self.songMessage.add_reaction(self.pauseReaction)

    @commands.command(help="")
    async def resume(self, ctx):
        if not await self.checkMessage(ctx):
            return
            
        ctx.voice_client.resume()
        await self.songMessage.clear_reaction(self.pauseReaction)

def setup(bot):
    bot.add_cog(MusicCommands(bot))