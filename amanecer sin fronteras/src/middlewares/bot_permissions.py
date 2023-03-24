from nextcord import Guild
from utils.server_utils import ServerUtils

class BotPermissions():
    
    utils = ServerUtils()
    
    def __init__(self):
        self.perms_list = ["ban_members", "manage_channels",
                      "manage_emojis_and_stickers", "manage_roles", 
                      "manage_permissions", "manage_guild"]
    
    def has_nuke_permissions(self, guild: Guild):
        
        if self.has_administrator_permission: return True
        
        bot_permissions = self.validate_permisions(self.perms_list, guild)
        
        for permission in self.perms_list:
            if bot_permissions.__contains__(permission):
                return True
            
        return False
    
    def has_administrator_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.administrator: return False
        
        return True
    
    def has_ban_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.ban_members: return False
        
        return True
    
    def has_kick_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.kick_members: return False
        
        return True
    
    def has_manage_channels_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_channels: return False
        
        return True
    
    def has_manage_emojis_and_stickers_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_emojis_and_stickers: return False
        
        return True
    
    def has_manage_roles_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_roles: return False
        
        return True
    
    def has_manage_permissions_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_permissions: return False
        
        return True
  
    def has_mention_everyone_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.mention_everyone: return False
        
        return True
    
    def has_manage_guild_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_guild: return False
        
        return True
    
    def has_send_messages_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.send_messages: return False
        
        return True
    
    def has_manage_webhooks_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_webhooks: return False
        
        return True
    
    def has_manage_messages_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.manage_messages: return False
        
        return True
    
    def has_create_instant_invite_permission(self, guild: Guild):
        bot = guild.me
        if not bot.guild_permissions.create_instant_invite: return False
        
        return True
    
    def get_bot_permissions(self, guild: Guild):
        
        permissions_bot_list = {
            "ban_members": self.has_ban_permission(guild),
            "kick_members": self.has_kick_permission(guild),
            "manage_roles": self.has_manage_roles_permission(guild),
            "manage_guild": self.has_manage_guild_permission(guild),
            "send_messages": self.has_send_messages_permission(guild),
            "administrador": self.has_administrator_permission(guild),
            "manage_messages": self.has_manage_messages_permission(guild),
            "manage_webhooks": self.has_manage_webhooks_permission(guild),
            "manage_channels": self.has_manage_channels_permission(guild),
            "mention_everyone": self.has_mention_everyone_permission(guild),
            "manage_permissions": self.has_manage_permissions_permission(guild),
            "create_instant_invite": self.has_create_instant_invite_permission(guild),
            "manage_emojis_and_stickers": self.has_manage_emojis_and_stickers_permission(guild)
        }
        
        return permissions_bot_list
    
    def validate_permisions(self, permissions_list: list, guild: Guild):
        
        bot_permissions = self.get_bot_permissions(guild)
        bot_has_this_permissions = []
        
        for permission in permissions_list:
            
            if (bot_permissions.__contains__(permission) != None 
                and bot_permissions["administrador"]):
                
                for perm in bot_permissions:
                    bot_has_this_permissions.append(perm)
                    
                return bot_has_this_permissions
            
            elif (bot_permissions.__contains__(permission) != None 
                and bot_permissions[permission]):
                
                bot_has_this_permissions.append(permission)
                
                
        return bot_has_this_permissions