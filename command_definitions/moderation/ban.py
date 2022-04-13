import discord
import datetime
from utilities.utilities import Utilities


async def ban_member(self, ctx, member, reason):
    try:
        channel = self.bot.get_channel(int(Utilities.channel('logs_channel')))
    except ValueError:
        print("No logs channel to send to")
        channel = None
    if not reason:
        reason = "No reason given"

    tz = Utilities.timezone()

    em = discord.Embed(title="<:p_exclamation03:960875871256862731> __Member Banned__",
                       color=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
    em.add_field(name="User:", value=member, inline=False)
    em.add_field(name="Moderator:", value=ctx.author.mention, inline=False)
    em.add_field(name="Reason:", value=reason, inline=False)

    if await Utilities.permission_check(ctx, member, 'ban') is True:
        await member.ban(reason=reason, delete_message_days=0)
        if channel != None:
            await channel.send(embed=em)
        await ctx.send(f"Banned **{member}**.")
        try:
            await member.send(
                f"You were banned from {ctx.guild.name} for ''{reason}''")
        except:
            pass
