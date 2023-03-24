import datetime

from nextcord import Embed, Interaction, Color, Guild, TextInputStyle
from nextcord.ui import Modal, TextInput
from nextcord.ext import commands

from config.config_handler import ConfigHandler
from components.buttons.nuke_buttons import NukeButtons
from utils.server_utils import ServerUtils

class NukeModel(Modal):
    
    config_handler = ConfigHandler()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild, bot: commands.Bot):
        super().__init__(
            title = "Configuración del comando /nuke",
            timeout = 300)
        
        self.guild = guild
        self.bot = bot
        
        self.channel_name = TextInput(
            label = "Nombres de los canales de spam",
            min_length = 1,
            max_length = 100,
            required = True,
            default_value = self.config_handler.get_channels_names()[0],
            placeholder = "Separados por comas, ejemplo: Raid by Pepe, Nuked.")
        
        self.roles_name = TextInput(
            label = "Nombres de los roles de spam",
            min_length = 1,
            max_length = 100,
            required = True,
            default_value = self.config_handler.get_roles_names()[0],
            placeholder = "Separados por comas, ejemplo: Raid by Pepe, Nuked.")
        
        self.quantity_channels = TextInput(
            label = "Cantidad de canales",
            min_length = 2,
            max_length = 3,
            required = True,
            default_value = self.config_handler.get_number_channels(),
            placeholder = "La cantidad de canales que creará el bot (10-250). ")
        
        self.quantity_roles = TextInput(
            label = "Cantidad de roles",
            min_length = 1,
            max_length = 2,
            required = True,
            default_value = self.config_handler.get_number_roles(),
            placeholder = "La cantidad de roles que creará el bot (1-99). ")
        
        self.message = TextInput(
            label = "Mensaje de spam",
            min_length = 1,
            max_length = 200,
            required = True,
            style = TextInputStyle.paragraph,
            default_value = self.config_handler.get_message(),
            placeholder = "El mensaje que spameará el bot.")
        
        self.add_item(self.channel_name)
        self.add_item(self.roles_name)
        self.add_item(self.quantity_channels)
        self.add_item(self.quantity_roles)
        self.add_item(self.message)
        
    async def callback(self, ctx: Interaction) -> None:
        
        spam_message = self.message.value
        channels_names = self.channel_name.value.split(",")
        roles_names = self.roles_name.value.split(",")
        quantity_ch = int(self.quantity_channels.value)
        quantity_mg = int(self.config_handler.get_messages_per_channel())
        quantity_rl = int(self.quantity_roles.value)
        hexadecimal_color = self.utils.convert_hexadeciamal_color_code(self.config_handler.get_color_role_code())
        
        if quantity_ch < 10 or quantity_ch > 250:
            raise ValueError
        
        if quantity_mg < 1 or quantity_mg > 50:
            raise ValueError
        
        if quantity_rl < 1 or quantity_rl > 99:
            raise ValueError
        
        start_embed = Embed(
            title = "✅ |Da clic en el botón con '🚀' para iniciar la acción.",
            timestamp = datetime.datetime.now(),
            color = Color.blurple())

        view = NukeButtons(bot = self.bot,
                           guild = self.guild,
                           message = spam_message,
                           roles_names = roles_names,
                           color = hexadecimal_color,
                           quantity_roles = quantity_rl,
                           channels_names = channels_names,
                           quantity_channels = quantity_ch,
                           quantity_messages = quantity_mg)
        
        await ctx.response.send_message(embed = start_embed, view = view)