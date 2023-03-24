import datetime

from nextcord import Embed, Interaction, Color, Guild
from nextcord.ui import Modal, TextInput

from config.config_handler import ConfigHandler
from components.buttons.role_buttons import RolesButtonsCreate
from utils.server_utils import ServerUtils

class CrolesModal(Modal):
    
    config_handler = ConfigHandler()
    utils = ServerUtils()
    
    def __init__(self, guild: Guild):
        super().__init__(
            title = "Configuración del comando /croles",
            timeout = 300)
        
        self.guild = guild
        
        self.role_name = TextInput(
            label = "Nombres de los roles de spam",
            min_length = 1,
            max_length = 100,
            required = True,
            default_value = self.config_handler.get_roles_names()[0],
            placeholder = "Separados por comas, ejemplo: Raid by Pepe, Nuked.")
        
        self.quantity_roles = TextInput(
            label = "Cantidad de roles",
            min_length = 1,
            max_length = 2,
            required = True,
            default_value = self.config_handler.get_number_roles(),
            placeholder = "La cantidad de roles que creará el bot (1-99). ")
        
        self.roles_color = TextInput(
            label = "Colores de los roles.",
            min_length = 7,
            max_length = 7,
            required = True,
            default_value = self.config_handler.get_color_role_code(),
            placeholder = "Código hexadecimal de colores.")
        
        self.add_item(self.role_name)
        self.add_item(self.quantity_roles)
        self.add_item(self.roles_color)
        
    async def callback(self, ctx: Interaction) -> None:
        
        hexadecimal_color = self.utils.convert_hexadeciamal_color_code(self.roles_color.value)
        roles_names = self.role_name.value.split(",")
        quantity = int(self.quantity_roles.value)
        
        if quantity < 1 or quantity > 99:
            raise ValueError
        
        start_embed = Embed(
            title = "✅ |Da clic en el botón con '🚀' para iniciar la acción.",
            timestamp = datetime.datetime.now(),
            color = Color.blurple())
        
        print(type(self.guild))
        view = RolesButtonsCreate(guild = self.guild,
                                  color = hexadecimal_color,
                                  quantity = quantity, 
                                  names = roles_names)
        
        await ctx.response.send_message(embed = start_embed, view = view)