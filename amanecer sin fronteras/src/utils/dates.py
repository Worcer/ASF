from nextcord import Guild

class Dates():
    
    def __init__(self):
        self.months_names = ["Enero", "Febrero", "Marzo", "Abril",
                        "Mayo", "Junio", "Julio" ,"Agosto",
                        "Septeimbre", "Octubre", "Noviembre", "Diciembre"]
        
        self.week_days_names = ["Lunes", "Martes", "Miercoles",
                           "Jueves", "Viernes", "Sabado", "Domingo"]
    
    def get_server_creation_date(self, guild: Guild):
        
        day = guild.created_at.day
        year = guild.created_at.year
        month = self.months_names[int(guild.created_at.month) -1]
        week_day = self.week_days_names[int(guild.created_at.weekday()) -1]
        
        
        return day, month, year, week_day