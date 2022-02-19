import json
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import time
import os
import asyncio
import random

from _classes.BotData import BotData
from cogs.GameManager import GameManagerCog
from cogs.Spellbook import SpellbookCog
from cogs.NameGen import NameGenCog
from cogs.CharacterGen import CharacterGenCog
from cogs.DiceRoller import DiceRollerCog
from cogs.wordle import WordleCog
# from cogs.TicTacToe import TicTacToeCog

botdata = BotData()

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

client.add_cog(GameManagerCog(client))
client.add_cog(SpellbookCog(client, botdata)) # Spellbook
client.add_cog(NameGenCog(client))
client.add_cog(CharacterGenCog(client))
client.add_cog(DiceRollerCog(client))
client.add_cog(WordleCog(client))
# client.add_cog(TicTacToeCog(client))

@client.command(brief="Gets you the current ping of the bot.")
async def ping(ctx):
    await ctx.send('pong! {0}'.format(round(client.latency, 1)))
        
@client.command(aliases=['Headpat', 'pat', 'Pat'],pass_context=True, brief="Allows you to headpat the good froggy.", description="/headpat\n\nAll of the headpats for the best boy.")
async def headpat(ctx):
    id = ctx.message.author.id
    random_int = random.randint(1, 1000)
    if random_int != 1000:
        await ctx.send("thankies! "+ '<@'+str(id)+'>')
    else:
        await ctx.send("I'm poisonous... " + '<@'+str(id)+'>')
    
@client.command(aliases=['Say', 'speak', 'Speak'],brief="Allows you to make the good boy repeat after you.", description="/say [arg1] [arg2]\n\n- arg1 = What Hopscotch will repeat\n- arg2 = Where Hopscotch will repeat your message. (optional)\n\nAllows you to make the good boy repeat after you.")
@commands.has_role("Mod")
async def say(ctx, arg1=None, arg2=None):
    if(arg2 != None):
        channel = discord.utils.get(ctx.guild.channels, name=arg2)
        await channel.send(arg1)
    else:
        await ctx.send(str(arg1))

@client.command(aliases=['DMball', 'DMBall'],brief="You may ask a question to the DM ball for spiritual guidance.", description="/dmball [arg]\n\n- arg = Your question to the DM Ball\n\nYou may ask a question to the DM ball for spiritual guidance.")
async def dmball(ctx, arg1):
    choices = ["Try again later", "It is certain", "Most likely", "It is decidely so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say so", "Outlook not so good", "Very doubtful"]
    await ctx.send(random.choice(choices))

#Bot command to delete all messages the bot has made.        
# @bot.command(pass_context=True,description='Deletes all messages the bot has made')
# @asyncio.coroutine
# def purge(ctx):
#     channel = ctx.message.channel
#     deleted = yield from bot.purge_from(channel, limit=100, check=is_me)
#     yield from bot.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))

# TO-DO
# Command that will add the role for a game to the desired user. Can be used by either the game master of the game, or the mods/staff
# Command that will make a timer to give a ping/notification to the players and game master of the game session being near
# Tic-Tac-Toe Game

client.run(str(data["token"]))