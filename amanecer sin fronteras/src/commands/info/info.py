import datetime

import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, Color, SlashOption

from utils.dates import Dates
from utils.server_utils import ServerUtils
from config.config_handler import ConfigHandler

class ServerInfo(commands.Cog):
    
    date = Dates()
    utils = ServerUtils()
    config_handler = ConfigHandler()
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(
        name = "info",
        description = "Información sobre un servidor",
        guild_ids = config_handler.get_CaC_server_id()
    )
    
    async def info_command(self, ctx: Interaction,
                    id: str = SlashOption(required = True, description = "ID del servidor objetivo")):

        guild = self.utils.get_server(int(id), self.bot)
        
        day, month, year, week_day = self.date.get_server_creation_date(guild)
        created_at = f"{week_day}, {day} de {month} de {year}."
        
        description = f"👑|Owner: {guild.owner} \n \
                        ⚔️|Roles: {len(guild.roles)} \n \
                        🏜️|Emojis: {len(guild.emojis)} \n \
                        💬|Canales: {len(guild.channels)} \n \
                        👥|Miembros: {guild.member_count} \n \
                        🆔|Server ID: {guild.id} \n \
                        📆|Fecha de creación: {created_at} \n"
        
        info = Embed(
            title = f"{guild.name}",
            description = description,
            color = Color.blurple(),
            timestamp = datetime.datetime.now()
        )
        
        if guild.icon != None:
            info.set_thumbnail(guild.icon)
            
        await ctx.response.send_message(embed = info)
        
def setup(client):
    client.add_cog(ServerInfo(client))