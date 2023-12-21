import threading

import discord
import discord.ext.commands as commands
import main as m


TOKEN = ''
PREFIX = '+'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

spamming = False
lock = threading.Lock()

@bot.event
async  def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name='enc')
async def encode(ctx, *, message: str):

    encoded_message = m.encoding(message)
    await ctx.channel.send(f'`{ctx.message.author}`: {encoded_message}')
    await ctx.message.delete()

@bot.command(name='dec')
async def decode(ctx, *, message):

    decoded_message = m.decoding(message)
    dm = await bot.create_dm(ctx.message.author)

    await dm.send(f'`{ctx.message.author}`: {decoded_message}')
    await ctx.message.delete()

    # if argh in bot.users:
    #     user_dm = await bot.create_dm(bot.user)
    # await user_dm.send(f'Decoded Message:-\nFrom: {ctx.message.author}\nOriginal Message: {message}' + decoded_message)

@bot.command(name='del_all')
async def delete_all(ctx, argh: int):

    all_messages = ctx.channel.history(limit=argh)
    async  for message in all_messages:
        await message.delete()

    # dm = await bot.create_dm(ctx.message.author)
    # dm_messages = dm.history(limit=argh)
    #
    # async for message in dm_messages:
    #     await message.delete()

user_who_spam = ''

@bot.command(name='spam')
async def spam(ctx, user, *, argh):
    global spamming
    global user_who_spam
    with lock:
        spamming = True

    user_who_spam = ctx.message.author
    while spamming:
        await ctx.channel.send(f'{user}: {argh}')

@bot.command(name='stop_spam')
async def stop_spam(ctx):
    global spamming

    if user_who_spam == ctx.message.author:
        with lock:
            spamming = False

        await ctx.channel.send(f'I stop spamming 😈')

    elif user_who_spam == '':
        await ctx.channel.send('No spam is going on')

    else:
        await ctx.channel.send(f"{ctx.message.author.mention}You can't stop this, Your too week 🤣")

bot.run(TOKEN)

