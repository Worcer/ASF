from nextcord.ext import commands
from nextcord import Guild
from nextcord.ui import View
from nextcord.ui.button import Button

from middlewares.server_verification import ServerVerification
from config.config_handler import ConfigHandler

class ServerUtils:
     
    server_checker = ServerVerification()
    config_handler = ConfigHandler()
    
    def __init__(self):
        pass
    
    def get_server(self, id: int, bot: commands.Bot):
        self.server_checker.check_existence(id, bot)
        return bot.get_guild(id)
    
    def get_bot(self, guild: Guild):
        aplication_id = self.config_handler.get_bot_id()
        return guild.get_member(aplication_id)
    
    def format_channels_names(self, channels_names: list):
        formatted_names = []
        
        for name in channels_names:
            name = name.strip().replace(" ", "-").lower()
            if name != "": 
                formatted_names.append(name)
            
        print(formatted_names)
        return formatted_names
    
    def disable_all_buttons(self, view: View):
        
        for child in view.children:
            
            if isinstance(child, Button):
                child.disabled = True
                
        return view
    
    def convert_hexadeciamal_color_code(self, hex_code: str):
        self.server_checker.check_hexadecimal_color_code(hex_code)
        hexadecimal_color = int(hex_code.replace("#", ""), 16)
        return hexadecimal_color
    
    