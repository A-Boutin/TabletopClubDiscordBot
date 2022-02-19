import discord
from discord.ext import commands
import random
import asyncio

class GameManager():
    def __init__(self):
        self.setup()
        
    def setup(self):
        print("GameManager: Loaded")

class GameManagerCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.initiatives = {}
        self.gamemanager = GameManager()
        
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
    @commands.command(aliases=['Creategame','CreateGame','cg','Cg','cG','CG','gamecreate','Gamecreate','GameCreate','gc','Gc','gC','GC'],brief="Makes the necessary channels and roles for a game.", description="/creategame [arg1] [arg2] @member\n\n- arg1   = Game Name/Campaign\n- arg2   = Game Name Abbreviation\n- @member = Game Master\n\nMakes the necessary channels and roles for a game.")
    @commands.has_role("Mod")
    async def creategame(self, ctx, arg1=None, arg2=None, gm: discord.Member = None):
        if(arg1 != None and arg2 != None and gm != None):
            # Stuff
            guild = ctx.guild
            progress_msg = await ctx.send("Making...")
            
            pos = discord.utils.get(ctx.guild.roles, name="⊱ ───── {⭒|PERSONAL|⭒} ───── ⊰").position +2
            
            member = discord.utils.get(ctx.guild.roles, name="Member")
            
            role = await guild.create_role(name=str(arg1), mentionable=True)
            await role.edit(position=pos)
            
            await gm.add_roles(role)
            
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(add_reactions=False, administrator=False, attach_files=False,ban_members=False,change_nickname=False,connect=False,create_instant_invite=False,deafen_members=False,embed_links=False,external_emojis=False,kick_members=False,manage_channels=False,manage_emojis=False,manage_guild=False,manage_messages=False,manage_nicknames=False,manage_permissions=False,manage_roles=False,manage_webhooks=False,mention_everyone=False,move_members=False,mute_members=False,priority_speaker=False,read_message_history=False,read_messages=False,request_to_speak=False,send_messages=False,send_tts_messages=False,speak=False,stream=False,use_external_emojis=False,use_slash_commands=False,use_voice_activation=False,view_audit_log=False,view_channel=False,view_guild_insights=False),
                role: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=None,move_members=None,mute_members=None,priority_speaker=None,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=None,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None),
                member: discord.PermissionOverwrite(add_reactions=True, administrator=None, attach_files=True,ban_members=None,change_nickname=None,connect=True,create_instant_invite=None,deafen_members=None,embed_links=True,external_emojis=True,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=None,move_members=None,mute_members=None,priority_speaker=None,read_message_history=True,read_messages=True,request_to_speak=None,send_messages=True,send_tts_messages=None,speak=None,stream=None,use_external_emojis=None,use_slash_commands=None,use_voice_activation=None,view_audit_log=None,view_channel=None,view_guild_insights=None),
                gm: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=True,move_members=None,mute_members=True,priority_speaker=True,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=True,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None)
            }
            
            category = await guild.create_category_channel(str(arg1))
            await category.create_text_channel(str(arg2) + " session planning", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " notes", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " star and wishes", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " house rules", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " pc basics", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " pc sheets", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " pc visuals", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " music", overwrites=overwrites)
            await category.create_text_channel(str(arg2) + " dice rolls", overwrites=overwrites)
            
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(add_reactions=False, administrator=False, attach_files=False,ban_members=False,change_nickname=False,connect=False,create_instant_invite=False,deafen_members=False,embed_links=False,external_emojis=False,kick_members=False,manage_channels=False,manage_emojis=False,manage_guild=False,manage_messages=False,manage_nicknames=False,manage_permissions=False,manage_roles=False,manage_webhooks=False,mention_everyone=False,move_members=False,mute_members=False,priority_speaker=False,read_message_history=False,read_messages=False,request_to_speak=False,send_messages=False,send_tts_messages=False,speak=False,stream=False,use_external_emojis=False,use_slash_commands=False,use_voice_activation=False,view_audit_log=False,view_channel=False,view_guild_insights=False),
                role: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=None,move_members=None,mute_members=None,priority_speaker=None,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=None,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None),
                member: discord.PermissionOverwrite(add_reactions=True, administrator=None, attach_files=True,ban_members=None,change_nickname=None,connect=True,create_instant_invite=None,deafen_members=None,embed_links=True,external_emojis=True,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=None,move_members=None,mute_members=None,priority_speaker=None,read_message_history=True,read_messages=True,request_to_speak=None,send_messages=True,send_tts_messages=None,speak=None,stream=None,use_external_emojis=None,use_slash_commands=None,use_voice_activation=None,view_audit_log=None,view_channel=True,view_guild_insights=None),
                gm: discord.PermissionOverwrite(add_reactions=None, administrator=None, attach_files=None,ban_members=None,change_nickname=None,connect=None,create_instant_invite=None,deafen_members=None,embed_links=None,external_emojis=None,kick_members=None,manage_channels=None,manage_emojis=None,manage_guild=None,manage_messages=None,manage_nicknames=None,manage_permissions=None,manage_roles=None,manage_webhooks=None,mention_everyone=True,move_members=None,mute_members=True,priority_speaker=True,read_message_history=None,read_messages=None,request_to_speak=None,send_messages=None,send_tts_messages=None,speak=True,stream=None,use_external_emojis=None,use_slash_commands=True,use_voice_activation=True,view_audit_log=None,view_channel=True,view_guild_insights=None)
            }
            
            await category.create_text_channel(str(arg2) + " voice chat", overwrites=overwrites)
            await category.create_voice_channel(str(arg2).upper() + " Sessions", overwrites=overwrites)
            
            await progress_msg.delete()
            await ctx.send("Done!")
        else:
            await ctx.send("Missing arguments!")
            
    @commands.command(aliases=['Deletegame','DeleteGame','dg','Dg','dG','DG','gamedelete','Gamedelete','GameDelete','gd','Gd','gD','GD'],brief="Deletes the appropriate channels and roles for a game.", description="/deletegame [arg]\n\n- arg = Game Name/Campaign\n\nDeletes the appropriate channels and roles for a game.")
    @commands.has_role("Mod")
    async def deletegame(self, ctx, arg1=None):
        if(arg1 != None):
            # Stuff
            msg = await ctx.send("Are you sure you want to delete " + str(arg1) + "?")
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
            
            def check(reaction, user):
                return user == ctx.author
            
            try:
                reaction = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
                if(str(reaction[0]) == '✅'):
                    # Stuff
                    channel = discord.utils.get(ctx.guild.channels, name=str(arg1))
                    role = discord.utils.get(ctx.guild.roles, name=str(arg1))
                    await role.delete()
                    category = self.client.get_channel(channel.id)
                    for channel in category.channels:
                        await channel.delete()
                    await category.delete()
                    await msg.delete()
                    await ctx.send("Successfully deleted!")
                elif(str(reaction[0]) == '❌'):
                    #More Stuff
                    await msg.delete()
                    await ctx.send("Deletion Aborted!")
                else:
                    await ctx.send("That isn't right...")
            except asyncio.TimeoutError:
                await msg.delete()
                await ctx.send("Timed out!")
        else:
            await ctx.send("Missing arguments!")

    @commands.command(aliases=['Initiative','init','Init','i','I','initiate','Initiate'],brief="Allows you to set the current initiative for a game that can be used as a reminder.", description="/initiative [args]\n\n- args = Names separated by spaces to indicate order of initiative\n\nAllows you to set the current initiative for a game that can be used as a reminder.")
    async def initiative(self, ctx, *args):
        if(len(args) != 0):
            if(str(args).isdecimal()):
                await ctx.send("You can't have just a number for a name, sorry :(")
            else:
                game = ctx.channel.category_id
                self.initiatives[game] = [arg for arg in args]
                await ctx.send("Initiative saved!")
        else:
            game = ctx.channel.category_id
            msg = "```Initiative:\n"
            counter = 1
            for arg in self.initiatives[game]:
                msg += "{}) {}\n".format(counter, arg)
                counter+=1
            msg += "```"
            # print(self.initiatives[game])
            await ctx.send(msg)
    
    @commands.command(aliases=['Addplayer','AddPlayer','initadd','Initadd','InitAdd'],brief='Adds a player to the initiative.', description='/addplayer [name] [idx]\n\n- name = The name of the player you are adding to the initiative\n- idx = Where in the list the player will go (optional).\n\nAdds a player to the initiative.')
    async def addplayer(self, ctx, name:str, idx=None):
        game = ctx.channel.category_id
        if(idx != None):
            if(not name.isdecimal()):
                self.initiatives[game].insert(int(idx)-1, name)
                await ctx.send("Successfully added player!")
            else:
                await ctx.send("No number for name >:T")
        else:
            if(not name.isdecimal()):
                self.initiatives[game].append(name)
                await ctx.send("Successfully added player!")
            else:
                await ctx.send("No number for name! >:T")
        
    @commands.command(aliases=['Removeplayer','RemovePlayer','initdel','Initdel','InitDel'],brief='Removes a player from the initiative.', description="/removeplayer [arg]\n\n- arg = The index or name of the player you'd like to remove from initiative.\n\nRemoves a player from the initiative.")
    async def removeplayer(self, ctx, arg):
        game = ctx.channel.category_id
        if(str(arg).isdecimal()):
            del self.initiatives[game][int(arg)-1]
            await ctx.send("Successfully removed player!")
        else:
            del self.initiatives[game][self.initiatives[game].index(str(arg))]
            await ctx.send("Successfully removed player!")
        
def setup(client):
    client.add_cog(GameManager(client))