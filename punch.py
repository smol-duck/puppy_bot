import discord
import requests


async def punch_member(self, ctx, member):
    response = requests.get('https://anime-api.hisoka17.repl.co/img/punch')
    json_ = response.json()
    url = json_['url']
    if member != None:
        em = discord.Embed(
            title=f"{ctx.author.display_name} punched {member.display_name}!",
            color=0xffd1dc)
    else:
        em = discord.Embed(title="KAPOW!!", color=0xffd1dc)
    em.set_image(url=url)
    await ctx.send(embed=em)
