import datetime

import nextcord
from nextcord import Embed, Interaction, Color, ButtonStyle, Guild

from utils.server_actions import Actions
from utils.server_utils import ServerUtils

class BanButtons(nextcord.ui.View):
    
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild):
        super().__init__()
        self.value = None
        self.guild = guild
        
    @nextcord.ui.button(label = "Iniciar", emoji = "🚀", style=ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, ctx: Interaction):
        
        load_embed = Embed(
            title = "⏳| Baneando miembros...",
            color = Color.yellow(),
            timestamp = datetime.datetime.now())
        
        message = ctx.message
        await message.edit(view = None, embed = load_embed)
        
        bans_count = await self.actions.ban_all_users(self.guild)
            
        if bans_count != 0:
            members_baned_embed = Embed(
                title = f"✅| El bot baneó a {bans_count} miembros.",
                color = Color.green(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = members_baned_embed)
                        
        else:
            no_members_baned = Embed(
                title = f"❌| El bot no pudo banear a nadie :/.",
                color = Color.red(),
                timestamp = datetime.datetime.now())
                
            await message.edit(embed = no_members_baned)
            
        
        
    @nextcord.ui.button(label = "Cancelar", emoji = "❎", style=ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, ctx: Interaction):

        cancel_embed = Embed(
            title = "❌| Se ha cancelado está acción.",
            timestamp = datetime.datetime.now(),
            color = Color.red())
        
        message = ctx.message
        await message.edit(view = None, embed = cancel_embed)