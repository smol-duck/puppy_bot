import discord
from discord.ext import commands
from command_definitions.general import profile, bot_profile, ping, prefix, toggle


class General(commands.Cog):
    """Commands which can be used by all users."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Info", aliases=['profile'])
    @commands.guild_only()
    @commands.cooldown(5, 60, commands.BucketType.user)
    async def profile_command(self, ctx, member: discord.Member = None):
        """Views the desired user’s profile, displaying necessary information."""
        await profile.profile(self, ctx, member)

    @commands.command(name="Bot")
    async def self_profile_command(self, ctx):
        """Displays the bot's information."""
        await bot_profile.self_info(self, ctx)

    @commands.command(name="Ping")
    async def ping_command(self, ctx):
        """Returns the bot latency, a good way to check if the bot is online and functional."""
        await ping.ping(self, ctx)

    @commands.command(name="Prefix")
    async def prefix_command(self, ctx):
        """Display's the bot's available prefixs."""
        await prefix.display_prefix(self, ctx)

    @commands.command(name="Toggle")
    @commands.has_guild_permissions(administrator=True)
    async def toggle_command(self, ctx, *, command):
        """Toggle a command on and off. When you disable a command it will not be available in the server to anyone."""
        await toggle.toggle(self, ctx, command)
