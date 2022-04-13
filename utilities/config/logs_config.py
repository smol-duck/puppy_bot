import json


async def logs_setup(ctx, bot):
    def check(m):
        if m.author == ctx.author and m.guild == ctx.guild and m.channel == ctx.channel:
            return True

    with open('utilities/settings.json', 'r') as f:
        settings = json.load(f)

    for i in range(6):
        await ctx.send(
            "**Please mention your logs channel by using the # method**\nType cancel to cancel setup\nType skip to skip this step",
            delete_after=20)

        msg = await bot.wait_for('message', check=check, timeout=20.0)

        if msg.content.lower() == 'cancel':
            await ctx.send("Setup cancelled", delete_after=20)
            return False

        elif msg.content.lower() == 'skip':
            await ctx.send("Logs channel skipped", delete_after=20)
            return True

        try:
            new_id = msg.channel_mentions[0].id
        except IndexError:
            await ctx.send(
                f"I cannot find that channel.\nPlease mention a channel using the #. E.g {ctx.channel.mention}",
                delete_after=20)
            continue

        channel_check = bot.get_channel(int(new_id))

        if channel_check != None:
            await ctx.send(
                f"Logs channel has been updated to {channel_check.mention}!",
                delete_after=60)
            settings['logs_channel'] = (str(new_id))
            with open('utilities/settings.json', 'w') as f:
                json.dump(settings, f, indent=3)
            break

        elif channel_check == None:
            await ctx.send(
                "I cannot find that channel. Please make sure I have access to that channel",
                delete_after=20)
            continue
