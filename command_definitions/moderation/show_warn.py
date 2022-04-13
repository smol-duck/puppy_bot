import discord
from datetime import datetime
import json
from utilities.utilities import Utilities


async def show_warning(self, ctx, member):
    tz = Utilities.timezone()

    with open('utilities/warns.json', 'r') as f:
        members = json.load(f)

    em = discord.Embed(title=f"{member}'s Warn History",
                       colour=0xffd1dc,
                       timestamp=datetime.now(tz))

    if str(member.id) not in members:
        em = discord.Embed(
            title=f"{member}'s Warn History",
            description=f"{member.mention} has not recived any warnings",
            colour=0xffd1dc,
            timestamp=datetime.now(tz))

    else:
        n = 1
        for warning in members[str(member.id)]:
            date = members[str(member.id)][warning]['date']
            time = members[str(member.id)][warning]['time']
            reason = members[str(member.id)][warning]['reason']
            warner_id = members[str(member.id)][warning]['warner']
            warner = await ctx.guild.fetch_member(warner_id)
            em.add_field(
                name=f"Warning {n}",
                value=
                f"Date: {date}\nTime: {time}\nReason: {reason}\nIssued by: {warner.mention}",
                inline=False)
            n += 1

    await ctx.send(embed=em)
