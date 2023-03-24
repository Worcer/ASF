import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, Color, SlashOption

from utils.server_actions import Actions
from utils.server_utils import ServerUtils
from config.config_handler import ConfigHandler
from middlewares.bot_permissions import BotPermissions

class Invite(commands.Cog):

    config_handler = ConfigHandler()
    permissions = BotPermissions()
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "invite",
        description = "Invita al bot a algún servidor",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    async def invite_command(self, ctx: Interaction):
        
        invite_embed = Embed(
            title = "__Cliqueame para invitar al bot__",
            color = Color.greyple(),
            url = self.config_handler.get_invite()
        )
            
        await ctx.response.send_message(embed = invite_embed)      
        
    @nextcord.slash_command(
        name = "invitesv",
        description = "Crea una invitación a algún servidor y te lo da.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    async def invitesv_command(self, ctx: Interaction, 
                id: str = SlashOption(required = True, description = "ID del servidor objetivo")):
        
        guild = self.utils.get_server(int(id), self.bot)
        
        if (not self.permissions.has_create_instant_invite_permission(guild)
            and not self.permissions.has_administrator_permission):
                
            raise commands.BotMissingPermissions(["1"])
        
        invite = await self.actions.create_invite(guild)
            
        await ctx.response.send_message(invite.url)
    
def setup(client):
    client.add_cog(Invite(client))