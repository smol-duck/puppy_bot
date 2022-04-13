import discord
from math import ceil, floor
from datetime import datetime
from utilities.utilities import Utilities


async def profile(self, ctx, member):
    if member == None:
        member = ctx.author

    permissions = Utilities.permissions(member)
    roles = Utilities.roles(member)

    today = datetime.today()
    date = today.date()

    created_at = member.created_at
    c_date = created_at.date()
    c_difference = ((date - c_date).days)
    c_years = floor(c_difference // 365.25)
    c_months = floor((c_difference - c_years * 365.25) // 30)
    c_days = ceil(c_difference - c_years * 365.25 - c_months * 30)
    if c_years == 0:
        if c_months == 0:
            c = f"{c_date}\n{c_days} days ago"

        else:
            c = f"{c_date}\n{c_months} months, {c_days} days ago"

    elif c_years != 0:
        c = f"{c_date}\n{c_years} years, {c_months} months, {c_days} days ago"

    joined_at = member.joined_at
    j = joined_at.date()

    em = discord.Embed(title=f"{member}'s Profile", color=0xffd1dc)
    em.add_field(name="Account Created", value=c)
    em.add_field(name="Member Joined", value=j)
    em.add_field(name="Permissions", value=permissions, inline=False)
    em.add_field(name="Roles", value=roles, inline=False)
    em.set_thumbnail(url=member.avatar_url)

    await ctx.send(embed=em, delete_after=30)
