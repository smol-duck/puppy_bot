import discord

from discord.ext import commands
from command_definitions.anime import cuddle, hug, kill, kiss, pat, slap, wink, punch, waifu


class Anime(commands.Cog):
    """Cute anime themed commands to express actions or emotions!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Cuddle")
    async def cuddle_command(self, ctx, member: discord.Member):
        """Cuddle up with a friend anime style or get a hug just for yourself."""
        await cuddle.cuddle_member(self, ctx, member)

    @commands.command(name="Hug")
    async def hug_command(self, ctx, member: discord.Member):
        """Give a friend a hug or if you're feeling down give one to yourself."""
        await hug.hug_member(self, ctx, member)

    @commands.command(name="Kill")
    async def kill_command(self, ctx, member: discord.Member):
        """Do it! Execute order 66!"""
        await kill.kill_member(self, ctx, member)

    @commands.command(name="Kiss")
    async def kiss_command(self, ctx, member: discord.Member):
        """Give another cutie a kiss!"""
        await kiss.kiss_member(self, ctx, member)

    @commands.command(name="Pat")
    async def pat_command(self, ctx, member: discord.Member):
        """Head pats are the best!"""
        await pat.pat_member(self, ctx, member)

    @commands.command(name="Slap")
    async def slap_command(self, ctx, member: discord.Member):
        """They probably deserved it right?"""
        await slap.slap_member(self, ctx, member)

    @commands.command(name="Wink")
    async def wink_command(self, ctx, member: discord.Member):
        """If you're using a winking command, it's not subtle..."""
        await wink.wink_member(self, ctx, member)

    @commands.command(name="Punch")
    async def punch_command(self, ctx, member: discord.Member):
        """A more aggressive form of the slap for when you really need to communicate your point."""
        await punch.punch_member(self, ctx, member)

    @commands.command(name="Waifu")
    async def waifu_command(self, ctx, member: discord.Member):
        """Get your anime dream girl here."""
        await waifu.waifu_member(self, ctx, member)
