import datetime

from nextcord import Embed, Color

def CreateServerEmbed(index: int, servers: list):

        start_index = index * 10
        end_index = start_index + 10
            
        embed = Embed(
            title="📋| Lista de Servidores", 
            color = Color.blurple(),
            timestamp = datetime.datetime.now())
        
        for guild in servers[start_index:end_index]:
            embed.add_field(name=guild.name,
                            inline = False,
                            value=f"🆔 |ID: {guild.id} \n 👥 |Miembros: {guild.member_count}")
                
        embed.set_footer(text=f"Página {index+1}/{(len(servers)+9)//10}")
        return embed