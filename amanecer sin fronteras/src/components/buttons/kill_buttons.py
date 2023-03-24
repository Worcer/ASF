import datetime

import nextcord
from nextcord.ext import commands
from nextcord import Embed, Interaction, Color, ButtonStyle, Guild

from utils.server_actions import Actions
from utils.server_utils import ServerUtils

class KillButtons(nextcord.ui.View):
    
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self,
                 bot : commands.Bot,
                 guild: Guild,
                 message: str,
                 channels_names: list, 
                 quantity_channels: int,
                 quantity_messages: int):
        
        super().__init__()
        self.bot = bot
        self.value = None
        self.guild = guild
        self.message = message
        self.channels_names = channels_names
        self.quantity_channels = quantity_channels
        self.quantity_messages = quantity_messages
        
    @nextcord.ui.button(label = "Iniciar", emoji = "🚀", style=ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, ctx: Interaction):
        
        title = "⏳| Eliminando canales..."
        
        load_embed = Embed(
            title = title,
            description = "",
            color = Color.yellow(),
            timestamp = datetime.datetime.now())
        
        message = ctx.message
        await message.edit(view = None, embed = load_embed)
        
        channels_deleted_count = await self.actions.delete_all_chanells(self.guild)
            
        if channels_deleted_count != 0:
            
            title = f"✅| El bot eliminó {channels_deleted_count} canales."
            channels_deleted_embed = Embed(
                title = title,
                description = "⏳| Creando canales...",
                color = Color.green(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = channels_deleted_embed)
                        
        else:
            title = f"❌| El bot no pudo eliminar ningún canal :/."
            no_channels_delted_embed = Embed(
                title = title,
                description = "⏳| Creando canales...",
                color = Color.blurple(),
                timestamp = datetime.datetime.now())
                
            await message.edit(embed = no_channels_delted_embed)
            
        channels_created_count = await self.actions.create_many_channels(self.bot,
                                                                         self.guild,
                                                                         self.message,
                                                                         self.channels_names,
                                                                         self.quantity_channels,
                                                                         self.quantity_messages)
        
        if channels_created_count != 0:
            channels_created_embed = Embed(
                title = title,
                description = f"✅| El bot creó {channels_created_count} canales de spam.",
                color = Color.green(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = channels_created_embed)
            
                        
        else:
            await message.fetch()
            no_channels_created_embed = Embed(
                title = title,
                description = f"❌| El bot no pudo crear ningún canal :/.",
                color = Color.blurple(),
                timestamp = datetime.datetime.now())
                        
            await message.edit(embed = no_channels_created_embed)
            
        
    @nextcord.ui.button(label = "Cancelar", emoji = "❎", style=ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, ctx: Interaction):

        cancel_embed = Embed(
            title = "❌| Se ha cancelado está acción.",
            timestamp = datetime.datetime.now(),
            color = Color.red())
        
        message = ctx.message
        await message.edit(view = None, embed = cancel_embed)