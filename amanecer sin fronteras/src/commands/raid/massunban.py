import datetime

import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption, Embed, Color

from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification
from components.buttons.unban_buttons import UnBanButtons
from utils.server_utils import ServerUtils

class MassUnBan(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "massunban",
        description = "Revoca el ban a todos los usuarios que pueda.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def massunban_command(self, ctx: Interaction, 
                    id: str = SlashOption(required = True, description = "Id del servidor objtivo.")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        self.verifications.check_bag(guild)
        
        if (not guild.me.guild_permissions.ban_members
            and not guild.me.guild_permissions.administrador):
            
            raise commands.BotMissingPermissions(["4"])
        
        start_embed = Embed(
            title = "✅ |Da clic en el botón con '🚀' para iniciar la acción.",
            timestamp = datetime.datetime.now(),
            color = Color.blurple())
        
        view = UnBanButtons(guild)
        await ctx.response.send_message(embed = start_embed, view = view)
        
def setup(client):
    client.add_cog(MassUnBan(client))