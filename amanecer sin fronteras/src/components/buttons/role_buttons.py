import datetime

import nextcord
from nextcord import Embed, Interaction, Color, ButtonStyle, Guild

from utils.server_actions import Actions
from utils.server_utils import ServerUtils

class RolesButtonsDelete(nextcord.ui.View):
    
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild):
        super().__init__()
        self.value = None
        self.guild = guild
        
    @nextcord.ui.button(label = "Iniciar", emoji = "🚀", style=ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, ctx: Interaction):
        
        load_embed = Embed(
            title = "⏳| Eliminando roles...",
            color = Color.yellow(),
            timestamp = datetime.datetime.now())
        
        message = ctx.message
        await message.edit(view = None, embed = load_embed)
        
        roles_count = await self.actions.delete_all_roles(self.guild)
            
        if roles_count != 0:
            roles_deleted_embed = Embed(
                title = f"✅| El bot eliminó {roles_count} roles.",
                color = Color.green(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = roles_deleted_embed)
                        
        else:
            no_roles_deleted = Embed(
                title = f"❌| El bot no pudo eliminar ningún rol :/.",
                color = Color.red(),
                timestamp = datetime.datetime.now())
                
            await message.edit(embed = no_roles_deleted)
        
    @nextcord.ui.button(label = "Cancelar", emoji = "❎", style=ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, ctx: Interaction):
        
        cancel_embed = Embed(
            title = "❌| Se ha cancelado está acción.",
            timestamp = datetime.datetime.now(),
            color = Color.red())

        message = ctx.message
        await message.edit(view = None, embed = cancel_embed)
        
class RolesButtonsCreate(nextcord.ui.View):
    
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild, color: int, quantity: int, names: list):
        super().__init__()
        self.value = None
        self.guild = guild
        self.color = color
        self.names = names
        self.quantity = quantity
        
    @nextcord.ui.button(label = "Iniciar", emoji = "🚀", style=ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, ctx: Interaction):

        load_embed = Embed(
            title = "⏳| Creando roles...",
            color = Color.yellow(),
            timestamp = datetime.datetime.now())
        
        message = ctx.message
        await message.edit(view = None, embed = load_embed)
        
        roles_count = await self.actions.create_many_roles(self.guild,
                                                           self.quantity,
                                                           self.color,
                                                           self.names)
            
        if roles_count != 0:
            roles_created_embed = Embed(
                title = f"✅| El bot creó {roles_count} roles.",
                color = Color.green(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = roles_created_embed)
                        
        else:
            no_roles_created = Embed(
                title = f"❌| El bot no pudo crear ningún rol :/.",
                color = Color.red(),
                timestamp = datetime.datetime.now())
                
            await message.edit(embed = no_roles_created)
        
    @nextcord.ui.button(label = "Cancelar", emoji = "❎", style=ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, ctx: Interaction):
        
        cancel_embed = Embed(
            title = "❌| Se ha cancelado está acción.",
            timestamp = datetime.datetime.now(),
            color = Color.red())
        
        message = ctx.message
        await message.edit(view = None, embed = cancel_embed)