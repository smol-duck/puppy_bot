import discord
import datetime
from utilities.utilities import Utilities


async def kick_member(self, ctx, member, reason):
    try:
        channel = self.bot.get_channel(int(Utilities.channel('logs_channel')))
    except ValueError:
        print("No logs channel to send to")
        channel = None
    tz = Utilities.timezone()

    em = discord.Embed(title="<:p_exclamation03:964883207600345098> __Member Kicked__",
                       color=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
    em.add_field(name="User:", value=member, inline=False)
    em.add_field(name="Moderator:", value=ctx.author.mention, inline=False)
    em.add_field(name="Reason:", value=reason, inline=False)

    if await Utilities.permission_check(ctx, member, 'kick') is True:
        await member.kick(reason=reason)
        if channel != None:
            await channel.send(embed=em)
        await ctx.send(f"Kicked **{member}**.")
        try:
            await member.send(
                f"You were kicked from {ctx.guild.name} for ''{reason}''")
        except:
            pass
