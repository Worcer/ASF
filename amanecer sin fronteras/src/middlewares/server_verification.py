import re

from nextcord.ext import commands
from nextcord import Guild

from config.config_handler import ConfigHandler
from errors.custom_exceptions.command_execution import *
from middlewares.bag import Bag

#Generate a exeption if the condition isn't true.
class ServerVerification():
    
    config_handler = ConfigHandler()
    bag = Bag()
    
    def __init__(self):
        pass
    
    def check_existence(self, id: int, bot: commands.Bot):
        guild = bot.get_guild(id)
        
        if guild == None:
            raise BotIsNotInGuild()
        
    def check_bag(self, guild: Guild):
        if self.bag.check(guild.id):
            raise ParallelExecutionCommandsNotAllowed()
        
    def check_hexadecimal_color_code(self, hex_code: str):
        regex = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
        
        if not bool(re.match(regex, hex_code)):
            raise IncorrectHexadecimalColorCode()
            
    def check_command_execution_in_allowed_server(self, guild_id: int):
        if guild_id == self.config_handler.get_CaC_server_id()[0]:
            raise ExecutionCommandInThisGuildNotAllowed()
        