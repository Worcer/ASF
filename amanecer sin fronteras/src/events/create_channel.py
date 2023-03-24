from nextcord import TextChannel
from nextcord.ext import commands

from config.config_handler import ConfigHandler

class CreateChannel(commands.Cog):
    
    config_handler = ConfigHandler()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_guild_channel_create(self,
                                      channel: TextChannel,
                                      message: str = None,
                                      quantity_messages: int = None,
                                      channels_names: list = None):
        
        
        try:
            if channel.name in channels_names:
                for x in range(quantity_messages):
                    try:
                        await channel.send(message)
                        
                    except: continue
                    
        except: pass
                
def setup(client):
    client.add_cog(CreateChannel(client))