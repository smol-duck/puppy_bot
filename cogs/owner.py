import discord
from discord.ext import commands
from utilities.config.bot_config import bot_setup
from discord.ext.commands.cooldowns import BucketType


class Owner(commands.Cog):
    """Commands for the owner of the server only."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Shutdown', aliases=['die', 'terminate'])
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Shutdown the bot and close all connections."""
        await ctx.channel.send("Shutting down...")
        await self.bot.logout()  # Logs the bot out properly

    @commands.command(name="Setup")
    @commands.is_owner()
    @commands.guild_only()
    @commands.max_concurrency(1, per=BucketType.default, wait=False)
    async def setup(self, ctx):
        """Setup and change the bot's settings such as prefix and logs channel."""
        bot = self.bot
        await bot_setup(ctx, bot)

    @commands.command(name="Test")
    @commands.is_owner()
    async def test(self, ctx):
        for invite in await ctx.guild.invites():
          print(invite.uses)
          a = await self.bot.fetch_invite(invite)
          print(a.approximate_member_count)
