import discord
import requests


async def waifu_member(self, ctx, member):
    response = requests.get('https://anime-api.hisoka17.repl.co/img/pat')
    json_ = response.json()
    url = json_['url']
    if member != None:
        em = discord.Embed(
            title=
            f"{ctx.author.display_name} asked {member.display_name} to be their waifu!",
            color=0xffd1dc)
    else:
        em = discord.Embed(title="Your new anime girlfriend", color=0xffd1dc)
    em.set_image(url=url)
    await ctx.send(embed=em)
