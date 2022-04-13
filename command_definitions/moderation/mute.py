import discord
import datetime
import requests
from utilities.utilities import Utilities


async def mute_member(self, ctx, member, duration, reason):
    tz = Utilities.timezone()
    headers = {"Authorization": f"Bot {self.bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{ctx.guild.id}/members/{member.id}"
    timeout = (datetime.datetime.utcnow() +
               datetime.timedelta(minutes=duration)).isoformat()
    json_data = {'communication_disabled_until': timeout}

    if await Utilities.permission_check(ctx, member, 'mute') is True:
        r = requests.patch(url=url, json=json_data, headers=headers)

        try:
            channel = self.bot.get_channel(
                int(Utilities.channel('logs_channel')))
        except ValueError:
            print("No logs channel to send to")
            channel = None

        if reason == None:
            reason = "No reason provided"

        now = datetime.datetime.now(tz)
        timechange = datetime.timedelta(minutes=duration)
        new = now + timechange
        new_day = new.date()
        new_time = new.time()
        time = new_time.strftime("%H:%M:%S")
        if new_day == now.date():
            until = f"{time}"
        else:
            until = f"{time}\n{new_day}"

        if r.status_code in range(200, 299):

            em = discord.Embed(title="<:p_exclamation03:960875871256862731> __Member Muted__",
                       color=0xffd1dc,
                       timestamp=datetime.datetime.now(tz))
            em.add_field(name="User:", value=member, inline=False)
            em.add_field(name="Moderator:", value=ctx.author.mention, inline=False)
            em.add_field(name="Until:", value=until, inline=False)
            em.add_field(name="Reason:", value=reason, inline=False)

            await ctx.send(
                f"Muted **{member}** for {duration}."
            )
            if channel != None:
                try:
                    await channel.send(embed=em)  # Sends ban embed
                except:
                    pass
            await member.send(
                f"You were muted in {ctx.guild.name} for ''{reason}''"
            )
            return
        else:
            return await ctx.send("Something went wrong!")
