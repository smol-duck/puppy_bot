import discord
import json
from datetime import datetime
from utilities.utilities import Utilities


async def remove_warn(self, ctx, member, warning):
    tz = Utilities.timezone()

    with open('utilities/warns.json', 'r') as f:
        members = json.load(f)

    try:
        channel = self.bot.get_channel(int(Utilities.channel('logs_channel')))
    except ValueError:
        print("No logs channel to send to")
        channel = None

    if str(member.id) not in members:
        await ctx.send(f"{member.name} has no warning to remove")

    try:
        warning = int(warning)
    except ValueError:
        await ctx.send("Please use an integer")
        return
    else:
        max_value = len(members[str(member.id)])

        if warning > max_value:
            await ctx.send(
                f"{member.name} has only recieved {max_value} warnings")
            return
        if warning <= 0:
            await ctx.send("Please use an integer above 0")
            return

        else:
            n = 1
            if await Utilities.permission_check(ctx, member,
                                                'warn remove') is True:
                for entry in members[str(member.id)]:
                    if n == warning:
                        reason = (members[str(member.id)][entry]['reason'])
                        del members[str(member.id)][entry]
                        break
                    else:
                        n += 1

            with open('utilities/warns.json', 'w') as f:
                json.dump(members, f, indent=3)

            em = discord.Embed(
                title="<:p_exclamation03:964883207600345098> Warning Removed",
                description=
                f"{member.mention}'s warning has been removed",
                colour=0xffd1dc,
                timestamp=datetime.now(tz))
            em.add_field(name="Moderator:",
                         value=ctx.author,
                         inline=True)
            em.add_field(name="Original Reason:", value=reason, inline=True)

            if channel != None:
                await channel.send(embed=em)

            await ctx.send(
                f"Warning {warning} has been removed from **{member}**")
