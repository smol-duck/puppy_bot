import discord
import datetime
import requests
from utilities.utilities import Utilities


async def unmute_member(self, ctx, member):
    headers = {"Authorization": f"Bot {self.bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{ctx.guild.id}/members/{member.id}"
    timeout = (datetime.datetime.utcnow() +
               datetime.timedelta(minutes=0)).isoformat()
    json_data = {'communication_disabled_until': timeout}

    if await Utilities.permission_check(ctx, member, 'unmute'):
        r = requests.patch(url=url, json=json_data, headers=headers)

        if r.status_code in range(200, 299):
            return await ctx.send(f"{member.name} has been unmuted!")

        else:
            return await ctx.send("Something went wrong!")
