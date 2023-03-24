import datetime

import nextcord
from nextcord import Embed, Interaction, Color, ButtonStyle, Guild

from utils.server_actions import Actions
from utils.server_utils import ServerUtils

class EmojisButtons(nextcord.ui.View):
    
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild):
        super().__init__()
        self.value = None
        self.guild = guild
        
    @nextcord.ui.button(label = "Iniciar", emoji = "🚀", style=ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, ctx: Interaction):

        load_embed = Embed(
            title = "⏳| Eliminando emojis...",
            color = Color.yellow(),
            timestamp = datetime.datetime.now())
        
        message = ctx.message
        await message.edit(view = None, embed = load_embed)
        
        emojis_count = await self.actions.delete_all_emojis(self.guild)
            
        if emojis_count != 0:
            emojis_deleted_embed = Embed(
                title = f"✅| El bot eliminó {emojis_count} emojis.",
                color = Color.green(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = emojis_deleted_embed)
                        
        else:
            no_emojis_deleted = Embed(
                title = f"❌| El bot no pudo eliminar emoji :/.",
                color = Color.red(),
                timestamp = datetime.datetime.now())
                
            await message.edit(embed = no_emojis_deleted)
        
    @nextcord.ui.button(label = "Cancelar", emoji = "❎", style=ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, ctx: Interaction):

        cancel_embed = Embed(
            title = "❌| Se ha cancelado está acción.",
            timestamp = datetime.datetime.now(),
            color = Color.red())
        
        message = ctx.message
        await message.edit(view = None, embed = cancel_embed)