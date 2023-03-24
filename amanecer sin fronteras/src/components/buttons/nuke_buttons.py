import time
import datetime

import nextcord
from nextcord import Embed, Interaction, Color, ButtonStyle, Guild
from nextcord.ext.commands import Bot

from utils.server_actions import Actions
from components.embeds.nuke_embed import CreateNukeEmbed
from utils.server_utils import ServerUtils

class NukeButtons(nextcord.ui.View):
    
    actions = Actions()
    utils = ServerUtils()
    
    def __init__(self,
                 bot: Bot,
                 color: int,
                 guild: Guild,
                 message: str,
                 roles_names: list,
                 quantity_roles: int,
                 channels_names: list,
                 quantity_channels: int,
                 quantity_messages: int):
        
        
        super().__init__()
        self.bot = bot
        self.value = None
        self.guild = guild
        self.color = color
        self.message = message
        self.roles_names = roles_names
        self.channels_names = channels_names
        self.quantity_roles = quantity_roles
        self.quantity_channels = quantity_channels
        self.quantity_messages = quantity_messages
        
    @nextcord.ui.button(label = "Iniciar", emoji = "🚀", style=ButtonStyle.blurple)
    async def confirm(self, button: nextcord.ui.Button, ctx: Interaction):
        
        nuke_embed = Embed(
            title = "🛠️ |Seguimiendo del comando /nuke ",
            description = "⏳| Eliminando emojis...",
            color = Color.yellow(),
            timestamp = datetime.datetime.now())
        
        message = ctx.message
        await message.edit(view = None, embed = nuke_embed)
        
        start_time = time.time()
        
        emojis_count = await self.actions.delete_all_emojis(self.guild)
        nuke_embed = CreateNukeEmbed(nuke_embed, 1, emojis_count)
        await message.edit(embed = nuke_embed)
        
        channels_deleted_count = await self.actions.delete_all_chanells(self.guild)
        nuke_embed = CreateNukeEmbed(nuke_embed, 2, channels_deleted_count)
        await message.edit(embed = nuke_embed)
        
        channels_created_count = await self.actions.create_many_channels(self.bot,
                                                                    self.guild,
                                                                    self.message,
                                                                    self.channels_names,
                                                                    self.quantity_channels,
                                                                    self.quantity_messages)
        
        nuke_embed = CreateNukeEmbed(nuke_embed, 3, channels_created_count)
        await message.edit(embed = nuke_embed)
        
        roles_deleted_count = await self.actions.delete_all_roles(self.guild)
        nuke_embed = CreateNukeEmbed(nuke_embed, 4, roles_deleted_count)
        await message.edit(embed = nuke_embed)
        
        roles_created_count = await self.actions.create_many_roles(self.guild,
                                                             self.quantity_roles,
                                                             self.color,
                                                             self.roles_names)
        
        end_time = time.time()
        
        nuke_embed = CreateNukeEmbed(nuke_embed, 5, roles_created_count)
        await message.edit(embed = nuke_embed)
        
        nuke_embed = CreateNukeEmbed(nuke_embed, 6, abs(int(start_time - end_time)))
        await message.edit(embed = nuke_embed)
        
        
        
    @nextcord.ui.button(label = "Cancelar", emoji = "❎", style=ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, ctx: Interaction):

        message = ctx.message

        cancel_embed = Embed(
            title = "❌| Se ha cancelado está acción.",
            timestamp = datetime.datetime.now(),
            color = Color.red())
        
        await message.edit(embed = cancel_embed, view = None)