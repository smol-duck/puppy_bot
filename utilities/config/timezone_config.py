import json

async def timezone_setup(ctx, bot):
  def check(m):
    if m.author == ctx.author and m.guild == ctx.guild and m.channel == ctx.channel:
      return True

  with open('utilities/settings.json', 'r') as f:
    settings = json.load(f)

  tz_file = open('utilities/tz_list.txt', 'r')
  tz_lines = tz_file.read()
  tz_list = tz_lines.split('\n')
  
  for i in range(6):
    await ctx.send("**Please choose a timezone from this list**\nTo cancel please type cancel\n\nType skip to skip this step\nhttps://github.com/smol-duck/pytz_tz_list/blob/main/timezone_list.txt", delete_after=120)

    msg = await bot.wait_for('message', check=check, timeout=120)

    new_tz = msg.content.lower()

    if new_tz == 'cancel':
      await ctx.send("Setup cancelled", delete_after=20)
      return False

    elif new_tz == 'skip':
      await ctx.send("Timezone skipped", delete_after=20)
      return True

    elif new_tz in tz_list:
      settings['timezone'] = (str(new_tz))
      await ctx.send(f"Timezone has been updated to {new_tz}!", delete_after=60)
      with open('utilities/settings.json', 'w') as f:
        json.dump(settings, f, indent=3)
      break

    else:
      await ctx.send("Timezone not found. Please make sure it is exactly as displayed in the list", delete_after=20)
      continue