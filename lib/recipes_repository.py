from lib.recipes import Recipes

class Recipes_Repository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipes(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
            recipes.append(item)
        print(type(Recipes))
        return recipes 
    
    """def find(self, id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [id])
        row = rows[0]
        return Recipes(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])"""
        