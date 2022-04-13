import json


async def prefix_setup(ctx, bot):
    def check(m):
        if m.author == ctx.author and m.guild == ctx.guild and m.channel == ctx.channel:
            return True

    with open('utilities/settings.json', 'r') as f:
        settings = json.load(f)

    for i in range(6):
        await ctx.send(
            "**Please send your new prefix**\nType cancel to cancel setup\nType skip to skip this step",
            delete_after=20)

        msg = await bot.wait_for('message', check=check, timeout=20)

        new_prefix = msg.content

        if new_prefix.lower() == "cancel":
            await ctx.send("Setup cancelled", delete_after=20)
            return False

        elif new_prefix.lower() == "skip":
            await ctx.send("Prefix skipped", delete_after=20)
            return True

        elif ' ' in new_prefix:
            await ctx.send("Prefix cannot contain a space", delete_after=20)
            continue

        else:
            settings['prefix'] = (str(new_prefix))
            with open('utilities/settings.json', 'w') as f:
                json.dump(settings, f, indent=3)
            await ctx.send(f"Prefix has been updated to {new_prefix}",
                           delete_after=60)
            return True
