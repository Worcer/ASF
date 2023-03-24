import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from config.config_handler import ConfigHandler
from components.buttons.servers_buttons import ServersButtons

class Servers(commands.Cog):

    config_handler = ConfigHandler()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "servers",
        description = "Obten una lista de los servidores en los que estoy.",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    async def serevers_command(self, ctx: Interaction):
        
        servers = self.bot.guilds
        view = ServersButtons(servers, 0)
        await ctx.response.send_message(embed = view.embed, view=view)
        
def setup(client):
    client.add_cog(Servers(client))