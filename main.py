import os
import discord

from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands

from utilities.utilities import Utilities
from utilities.help_command import HelpCommand
from utilities.error_handling import CommandErrorHandler

from cogs import moderation
from cogs import general
from cogs import anime
from cogs import nsfw
from cogs import owner

ENVFILE = Path(__file__).parent / "secret.env"

# Loading environment variables and checking for secret token presence
if ENVFILE.exists():
    load_dotenv(dotenv_path=ENVFILE)
    token = os.getenv('PUPPY_BOT_TOKEN')
else:
    print("No bot token found!")
    token = input("Enter your bot's token: ")
    with ENVFILE.open('w', encoding='utf-8') as f:
        f.write(f"export PUPPY_BOT_TOKEN=\'{token}\'")


def get_prefix(bot, msg):
    user_id = bot.user.id
    pfx_list = [f'<@!{user_id}> ', f'<@{user_id}> ']
    pfx = Utilities.prefix()
    pfx_list.append(pfx)
    return pfx_list


# Bot Setup
intents = discord.Intents.all()  # Gives bot certain permissions
status = discord.Status.online
bot = commands.Bot(command_prefix=get_prefix,
                   intents=intents,
                   case_insensitive=True)  # Applies prefix and intents
bot.help_command = HelpCommand()

# Add cogs
bot.add_cog(moderation.Moderation(bot))
bot.add_cog(general.General(bot))
bot.add_cog(anime.Anime(bot))
bot.add_cog(nsfw.NSFW(bot))
bot.add_cog(owner.Owner(bot))

bot.add_cog(CommandErrorHandler(bot))


# Make the bot ignore commands until fully initialized
@bot.event
async def on_connect():
    print(f"{bot.user.name} connected, ID is {bot.user.id}. Getting ready...")
    await bot.wait_until_ready()


@bot.event
async def on_ready():
    pfx = Utilities.prefix()
    for guild in bot.guilds:
        print(f"Ready in {guild.name}")
    print("------Bot Ready------")
    command_list = Utilities.disabled_commands()
    for c in command_list:
        command = bot.get_command(c)
        if c == '':
            continue
        else:
            try:
                command.enabled = False
                print(f"{c} disabled")
            except:
                print(f"\n{c} FAILED\n")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'{pfx}help for help | Made by Duckling#0007'))


@bot.event
async def on_member_join(member):
    channelw = bot.get_channel(int(Utilities.channel(
        'welcome_channel')))  # Channel ID for welcome channel
    channela = bot.get_channel(int(Utilities.channel(
        'announcement_channel')))  # Channel ID for announcement channel
    n = len(channelw.guild.members)
    if n % 100 == 0:
        await channela.send(f"{channelw.guild.name} has reached {n} members!!!"
                            )


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(Utilities.channel(
        'leavers_channel')))  # Channel ID for leavers channel
    pass


@bot.event
async def on_message(message):

    pfx = Utilities.prefix()  # Assigns the prefix
    cog_list = ["general", "nsfw", "owner", "anime", "moderation"]
    if not message.author.bot:  # Checks that message was not sent by a bot
        if message.guild == None:  # Checks if the message was sent in DMs
            pass  # Skips the auto reponder if it was sent in DMs

        else:
            pass

        words = message.content.lower().split(' ')
        if len(words) == 2:
          for word in words:
            for cog in cog_list:
              if word == cog:
                message.content = message.content.title()

    await bot.process_commands(message)  # Processes the command


async def auto_responder(message):
    pass


# Run bot token
if __name__ == '__main__':
    try:
        bot.run(token)
    except discord.PrivilegedIntentsRequired:
        print("Privileged Intents are required to use this bot. "
              "Enable them through the Discord Developer Portal.")
    except discord.DiscordException as e:
        print(e)
