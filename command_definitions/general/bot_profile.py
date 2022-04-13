import discord


async def self_info(self, ctx):
    em = discord.Embed(title="Puppy Bot", color=0xffd1dc)
    em.add_field(name="Developed By", value="<@!654401308392161291>", inline=False)
    em.add_field(name="For:", value="<@!608640525612089346>", inline=False)
    em.add_field(name="Release Date:", value="2022/04/xx", inline=False)
    em.add_field(name="Lines:", value="2,529", inline=False)
    await ctx.send(embed=em)
