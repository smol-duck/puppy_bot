import discord
import datetime
from utilities.utilities import Utilities


async def purge_messages(self, ctx, limit, member):
    tz = Utilities.timezone()
    msg = []
    try:
        channel = self.bot.get_channel(int(Utilities.channel('logs_channel')))
    except ValueError:
        print("No logs channel to send to")
        channel = None
    try:
        int(limit)
    except ValueError:
        return await ctx.send("Please use an integer for the limit of purge")

    await ctx.message.delete()

    if member == None:
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"{limit} messages deleted in purge", delete_after=10)

    else:
        async for message in ctx.channel.history():
            if len(msg) == limit:
                break
            if message.author == member:
                msg.append(message)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {limit} messages from {member.mention}",
                       delete_after=10)

    em = discord.Embed(title="<:p_exclamation03:964883207600345098> Message Purged",
                       colour=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
    em.add_field(name="Quantity:", value=limit, inline=False)
    em.add_field(name="Moderator:", value=ctx.author.mention, inline=False)
    em.add_field(name="Channel:", value=ctx.channel.mention, inline=False)
    if member:
        em.add_field(name="Target:", value=member.mention, inline=False)

    if channel != None:
        try:
            await channel.send(embed=em)  # Sends ban embed
        except:
            pass
