from lib.recipes_repository import *
from lib.recipes import *


"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_recipes(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = Recipes_Repository(db_connection) # Create a new ArtistRepository

    recipe = repository.all() # Get all artists

    # Assert on the results
    assert recipe == [
        Recipes(1, 'Chicken', 120, 4),
        Recipes(2, 'Noodles', 20, 2),
        Recipes(3, 'Bon Bue Hue', 60, 5),
        Recipes(4, 'Pizza', 30, 3),
        Recipes(5, 'Jollof rice', 60, 5)
        
        ]
    print(type(Recipes(1, 'Chicken', 120, 4)))
'''"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = Recipes_Repository(db_connection)

    recipes = repository.find(3)
    assert recipes == Recipes(3, 'Bon Bue Hue', 60, 5)'''

'''''''''
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Lemonade", 2016, 5))

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Here Comes the Sun', 1971, 4),
        Album(10, 'Bossanova', 1990, 1),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Here Comes the Sun', 1971, 4),
        Album(10, 'Bossanova', 1990, 1),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]"""'''
