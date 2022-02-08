import json
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import time
import os

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")
    
@client.command()
async def ping(ctx):
    await ctx.send('pong! {0}'.format(round(client.latency, 1)))
     

# Official Format:
# Test (category channel)
# t-session-planning (text channel)
# t-notes (text-channel)
# t-stars-and-wishes (text channel)
# t-pc-basics (text channel)
# t-pc-sheets (text channel)
# t-pc-visuals (text channel)
# t-music (text channel)
# t-dice-rolls (text channel)
# t-voice-chat (text channel)
# T Sessions (voice channel)
        
# Makes a game (category, channel, role, etc) in the server
@client.command()
@commands.has_role("Staff")
async def creategame(ctx, arg1=None, arg2=None, member: discord.Member = None):
    if(arg1 != None and arg2 != None and member != None):
        # Stuff
        guild = ctx.guild
        progress_msg = await ctx.send("Making...")
        
        pos = discord.utils.get(ctx.guild.roles, name="⊱ ───── {⭒|PERSONAL|⭒} ───── ⊰").position +2
        
        role = await guild.create_role(name=str(arg1), mentionable=True)
        await role.edit(position=pos)
        
        await member.add_roles(role)
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(add_reactions=False, administrator=False, attach_files=False,ban_members=False,change_nickname=False,connect=False,create_instant_invite=False,deafen_members=False,embed_links=False,external_emojis=False,kick_members=False,manage_channels=False,manage_emojis=False,manage_guild=False,manage_messages=False,manage_nicknames=False,manage_permissions=False,manage_roles=False,manage_webhooks=False,mention_everyone=False,move_members=False,mute_members=False,priority_speaker=False,read_message_history=False,read_messages=False,request_to_speak=False,send_messages=False,send_tts_messages=False,speak=False,stream=False,use_external_emojis=False,use_slash_commands=False,use_voice_activation=False,view_audit_log=False,view_channel=False,view_guild_insights=False),
            role: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=None,move_members=None,mute_members=None,priority_speaker=None,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=None,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None),
            member: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=True,move_members=None,mute_members=True,priority_speaker=True,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=True,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None)
        }
        
        category = await guild.create_category_channel(str(arg1))
        await category.create_text_channel(str(arg2) + " session planning", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " notes", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " star and wishes", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " pc basics", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " pc sheets", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " pc visuals", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " music", overwrites=overwrites)
        await category.create_text_channel(str(arg2) + " dice rolls", overwrites=overwrites)
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(add_reactions=False, administrator=False, attach_files=False,ban_members=False,change_nickname=False,connect=True,create_instant_invite=False,deafen_members=False,embed_links=False,external_emojis=False,kick_members=False,manage_channels=False,manage_emojis=False,manage_guild=False,manage_messages=False,manage_nicknames=False,manage_permissions=False,manage_roles=False,manage_webhooks=False,mention_everyone=False,move_members=False,mute_members=False,priority_speaker=False,read_message_history=True,read_messages=True,request_to_speak=False,send_messages=True,send_tts_messages=False,speak=False,stream=False,use_external_emojis=False,use_slash_commands=False,use_voice_activation=False,view_audit_log=False,view_channel=True,view_guild_insights=False),
            role: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=None,move_members=None,mute_members=None,priority_speaker=None,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=None,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None),
            member: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=True,move_members=None,mute_members=True,priority_speaker=True,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=True,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None)
        }
        
        await category.create_text_channel(str(arg2) + " voice chat", overwrites=overwrites)
        await category.create_voice_channel(str(arg2).upper() + " Sessions", overwrites=overwrites)
        
        await progress_msg.delete()
        await ctx.send("Done!")
    else:
        await ctx.send("Missing arguments!")
        
@client.command()
@commands.has_role("Staff")
async def deletegame(ctx, arg1=None):
    if(arg1 != None):
        # Stuff
        channel = discord.utils.get(ctx.guild.channels, name=str(arg1))
        role = discord.utils.get(ctx.guild.roles, name=str(arg1))
        await role.delete()
        category = client.get_channel(channel.id)
        for channel in category.channels:
            await channel.delete()
        await category.delete()
        await ctx.send("Successfully deleted!")
    else:
        await ctx.send("Missing arguments!")

client.run(str(data["token"]))
