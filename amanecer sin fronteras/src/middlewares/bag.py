import json

class Bag():
    
    def add(self, id: int):
        
        with open("../config/bag.json", "r") as file:
            config = json.load(file)
            bag = config["Bag"]
            
        bag[id] = True
        config["Bag"] = bag
        
        with open("../config/bag.json", "w") as file:
            json.dump(config, file, indent = 4)
    
    def delete(self, id: int):
        
         with open("../config/bag.json", "r") as file:
            config = json.load(file)
            bag = config["Bag"]
            
            try:
                del bag[str(id)]
                
            except Exception as e: print(e)
            
            config["Bag"] = bag
        
            with open("../config/bag.json", "w") as file:
                json.dump(config, file, indent = 4)
    
    def check(self, id: int):
        
        config = json.load(open("../config/bag.json"))
        bag = config["Bag"]
        
        if str(id) in bag:
            return True
        
        return False
    
    def clear(self):
        
        with open("../config/bag.json", "r") as file:
            config = json.load(file)
            config["Bag"] = {}
        
        with open("../config/bag.json", "w") as file:
            json.dump(config, file, indent = 4)