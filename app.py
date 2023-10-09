from lib.database_connection import DatabaseConnection
from lib.recipes_repository import Recipes_Repository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes.sql")

# Retrieve all artists
recipes_repository = Recipes_Repository(connection)
recipes = recipes_repository.all()

# List them out
for recipe in recipes:
    print(recipe)

