from discord.ext import commands
import time
from command_definitions.nsfw import boobs, hentai, lesbian


class NSFW(commands.Cog):
    """Commands that produce NSFW results. These can only be used in channels that are marked as NSFW."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Boobs")
    @commands.guild_only()
    @commands.is_nsfw()
    async def boobs_command(self, ctx):
        """It's anime boobs... What more do you want?
    This command can only be used in a NSFW tagged channel."""
        await boobs.boobs_member(self, ctx)

    @commands.command(name="Lesbian")
    @commands.guild_only()
    @commands.is_nsfw()
    async def lesbian_command(self, ctx):
        """It's hentai but with only girls in it.
    This command can only be used in NSFW tagged channels."""
        start = time.time()
        await lesbian.lesbian_member(self, ctx)
        end = time.time()
        print(end - start)

    @commands.command(name="Hentai")
    @commands.guild_only()
    @commands.is_nsfw()
    async def hentai_command(self, ctx):
        """It's porn... Cartoon porn... I don't need to explain it more
    This command can only be used in a NSFW tagged channel."""
        await hentai.hentai_member(self, ctx)
