from utilities.utilities import Utilities
from command_definitions.moderation import ban, kick, mute, purge, remove_warn, show_warn, unban, unmute, warn
from discord.ext import commands

import discord
import datetime


class Moderation(commands.Cog):
    """Commands exclusively for moderators and admins."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Ban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban_command(self, ctx, member: discord.Member, *, reason=None):
        """Permanently removes a user from the server until they are unbanned."""
        await ban.ban_member(self, ctx, member, reason)

    @commands.command(name="Unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def unban_command(self, ctx, member):
        """Unbans a user from the server."""
        await unban.unban_member(self, ctx, member)

    @commands.command(name="Kick")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def kick_command(self, ctx, member: discord.Member, *, reason=None):
        """Temporarily removes a user from the server. They have the ability to rejoin."""
        await kick.kick_member(self, ctx, member, reason)

    @commands.command(name="Mute")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def mute_command(self,
                           ctx,
                           member: discord.Member,
                           duration: int,
                           *,
                           reason=None):
        """Revokes a user’s ability to send messages."""
        await mute.mute_member(self, ctx, member, duration, reason)

    @commands.command(name="Unmute")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def unmute_command(self, ctx, member: discord.Member):
        """Allows a muted user to send messages."""
        await unmute.unmute_member(self, ctx, member)

    @commands.command(name="Purge")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge_command(self,
                            ctx,
                            limit: int,
                            member: discord.Member = None):
        """Bulk deletes the desired amount of messages from a channel."""
        await purge.purge_messages(self, ctx, limit, member)

    @commands.group(name="Warn", invoke_without_command=True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def warn_command(self, ctx, member: discord.Member, *, reason):
        """Warns a member as a low level punishment. This will DM the member."""
        await warn.warn_member(self, ctx, member, reason)

    @warn_command.command(name="show", aliases=['s'])
    async def show_command(self, ctx, member: discord.Member):
        """Shows all warnings a member has."""
        await show_warn.show_warning(self, ctx, member)

    @warn_command.command(name="remove", aliases=['r'])
    async def remove_command(self, ctx, member: discord.Member, warning):
        """Remove a warning from a member."""
        await remove_warn.remove_warn(self, ctx, member, warning)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        try:
            channel = self.bot.get_channel(
                int(Utilities.channel('logs_channel')))
        except ValueError:
            print("No logs channel to send to")
            channel = None

        logs = await guild.audit_logs(
            limit=1, action=discord.AuditLogAction.ban).flatten()
        logs = logs[0]
        banner = logs.user
        reason = logs.reason

        tz = Utilities.timezone()

        em = discord.Embed(title="<:p_exclamation03:964883207600345098> __Member Banned__",
                       color=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
        em.add_field(name="User:", value=user, inline=False)
        em.add_field(name="Moderator:", value=banner.mention, inline=False)
        em.add_field(name="Reason:", value=reason, inline=False)

        if banner != self.bot.user:
            if channel != None:
                try:
                    await channel.send(embed=em)  # Sends ban embed
                except:
                    pass

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        try:
            channel = self.bot.get_channel(
                int(Utilities.channel('logs_channel')))
        except ValueError:
            print("No logs channel to send to")
            channel = None

        logs = await guild.audit_logs(
            limit=1, action=discord.AuditLogAction.ban).flatten()
        logs = logs[0]

        tz = Utilities.timezone()

        em = discord.Embed(title="<:p_exclamation03:964883207600345098> __Member Unbanned__",
                       color=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
        em.add_field(name="User:", value=user, inline=False)
        em.add_field(name="Moderator:", value=logs.user.mention, inline=False)

        if channel != None:
            try:
                await channel.send(embed=em)  # Sends ban embed
            except:
                pass
