from nextcord import Embed, Color
from config.config_handler import ConfigHandler

config_handler = ConfigHandler()

def CreateNukeEmbed(embed: Embed, status: int, new_data: str):
    
    """
    status 1: Emoji deleting compled
    status 2: Channels deleting compled
    status 3: Channels creating compled
    status 4: Roles deleting compled
    status 5: Roles creating compled
    status 6: Finished!
    """
    
    old_status_embed = {
        1: "⏳| Eliminando emojis...",
        2: "⏳| Eliminando canales...",
        3: "⏳| Creando canales...",
        4: "⏳| Eliminando roles...",
        5: "⏳| Creando roles...",
        6: "⏲️| Raid concluida en..."}
    
    new_status_embed = {
        1: "✅| El bot eliminó {} emojis. \n ⏳| Eliminando canales...",
        2: "✅| El bot eliminó {} canales. \n ⏳| Creando canales...",
        3: "✅| El bot creó {} canales de spam. \n ⏳| Eliminando roles...",
        4: "✅| El bot eliminó {} roles. \n ⏳| Creando roles...",
        5: "✅| El bot creó {} roles de spam. \n ⏲️| Raid concluida en...",
        6: "⏲️| Raid concluida en {} segundos."}
    
    new_status_error_embed = {
        1: "❌| El bot no pudo eliminar emojis. \n ⏳| Eliminando canales...",
        2: "❌| El bot no pudo eliminar canales. \n ⏳| Creando canales...",
        3: "❌| El bot no pudo crear canales. \n ⏳| Eliminando roles...",
        4: "❌| El bot no pudo eliminar roles. \n ⏳| Creando roles...",
        5: "❌| El bot no pudo crear roles. \n ⏲️| Raid concluida en ..."}
    
    if status > 6 or status < 1: 
        raise ValueError
    
    if status == 6:
        embed.color = Color.blurple()
    
    if new_data != 0:
        new_status = new_status_embed[status].format(new_data)
        
    else:
        new_status = new_status_error_embed[status]
        
    old_status = old_status_embed[status]
    
    embed.description = embed.description.replace(old_status, new_status)

    return embed