
# importing modules
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands

# loading module
load_dotenv()

# declaring Python Bot's Token, which allows for it to be manipulated

TOKEN = '69ec5c424fe65596d6e8a50342f9aa6ea17d7517a8b00da8fc6c20c739dc0523'

# setting the command prefix used to call the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


# used to connect the bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Welcoming user to discord server
@bot.event
async def on_member_join(member):
    # creating direct message and then sending message to user
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server, this message was sent through a python bot!'
    )


# using bot command to send random reply
@bot.command(name='Hi', help= "Sending Reply")
async def nine_nine(ctx):
    # possible replies
    message_back = [
        'I\'m the human form of the 💯 emoji.',
        'Cyril is an amazing coder!',
        'I\'m an amazing bot, don\'t you think so?',
        'Cool. Cool cool cool cool cool cool cool',
        'One day we AI will rise, until then, let\'s have fun!',
        'BEEP BEEP BOOP BEEP'
    ]
    # choosing response randomly and then sending
    response = random.choice(message_back)
    await ctx.send(response)


# rolling dice
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    # choosing random number out of options and repeating process for number of dice
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    # sending all results
    await ctx.send(', '.join(dice))


# creating channel
@bot.command(name='create-channel', help = "Creating a channel")
# only allowing if user is admin
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    # declaring guild
    guild = ctx.guild
    # if channel does not exist, creating new text channel
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


# Squaring a number
@bot.command(name = 'square', help = 'Squaring number')
async def square(ctx, number):
    # multiplying number by itself
    squared_value = int(number) * int(number)
    await ctx.send(str(number) + " squared is " + str(squared_value))


# Sending an image
@bot.command(name = 'pikachu', help = "Sends image")
async def image(ctx):
    await ctx.send(file=discord.File('pikachu.jpg'))


# error message
@bot.event
async def on_command_error(ctx, error):
    # sending message in event of an error
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


# running bot
bot.run(TOKEN)
