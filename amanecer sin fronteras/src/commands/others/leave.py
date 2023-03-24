import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, Color, SlashOption

from utils.server_utils import ServerUtils
from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification

class Leave(commands.Cog):

    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "leave",
        description = "Hace que el bot se salga se un server.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    async def leave_command(self, ctx: Interaction, 
                id: str = SlashOption(required = True, description = "ID del servidor objetivo")):
        
        guild = self.utils.get_server(int(id), self.bot)
        name = guild.name
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)

        await guild.leave()
        
        leave_embed = Embed(
            title = f"✅ Me salí de {name} ✅",
            color = Color.greyple(),)
            
        await ctx.response.send_message(embed = leave_embed)      
        
def setup(client):
    client.add_cog(Leave(client))