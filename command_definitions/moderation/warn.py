import discord
import datetime
import json
from utilities.utilities import Utilities


async def warn_member(self, ctx, member, reason):
    a = datetime.datetime.now()
    b = a.strftime("%H:%M:%S")
    today = datetime.datetime.today()
    date = today.date()
    with open('utilities/warns.json', 'r') as f:  # Opens member list JSON file
        members = json.load(f)  # Loads data from file

    try:
        channel = self.bot.get_channel(int(Utilities.channel('logs_channel')))
    except ValueError:
        print("No logs channel to send to")
        channel = None
    tz = Utilities.timezone()

    em = discord.Embed(title="<:p_exclamation03:960875871256862731> __Member Warned__",
                       color=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
    em.add_field(name="User:", value=member, inline=False)
    em.add_field(name="Moderator:", value=ctx.author.mention, inline=False)
    em.add_field(name="Reason:", value=reason, inline=False)

    if await Utilities.permission_check(ctx, member, 'warn') is True:
        if str(member.id) not in members:
            n = 0
            members[str(member.id)] = {}
            members[str(member.id)][f'warning {n+1}'] = {}
            members[str(member.id)][f'warning {n+1}']['date'] = str(date)
            members[str(member.id)][f'warning {n+1}']['time'] = str(b)
            members[str(member.id)][f'warning {n+1}']['warner'] = str(
                ctx.author.id)
            members[str(member.id)][f'warning {n+1}']['reason'] = str(reason)
        else:
            n = len(members[str(member.id)])
            members[str(member.id)][f'warning {n+1}'] = {}
            members[str(member.id)][f'warning {n+1}']['date'] = str(date)
            members[str(member.id)][f'warning {n+1}']['time'] = str(b)
            members[str(member.id)][f'warning {n+1}']['warner'] = str(
                ctx.author.id)
            members[str(member.id)][f'warning {n+1}']['reason'] = str(reason)

        with open('utilities/warns.json',
                  'w') as f:  # Opens JSON file member list
            json.dump(members, f, indent=3)  # Stores member data in JSON file

        try:
            await member.send(
                f"You were warned in {ctx.guild.name} for ''{reason}''"
            )  # DMs banee
        except:
            pass
        if channel != None:
            em.add_field(name="Number of warnings",
                         value=(n + 1),
                         inline=False)
            try:
                await channel.send(embed=em)  # Sends ban embed
            except:
                pass
        await ctx.send(f"Warned **{member}**.")
        return
