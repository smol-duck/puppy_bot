async def ping(self, ctx):
    latency = (round((self.bot.latency) * 1000))

    await ctx.reply(f"Pong! {latency}ms taken!")
