from lib.recipes import Recipes

def test_recipes_initialised():
    recipes = Recipes (1, "test recipe_name", "test cooking_time", "test rating")
    assert recipes.id == 1
    assert recipes.recipe_name == "test recipe_name"
    assert recipes.cooking_time == "test cooking_time"
    assert recipes.rating == "test rating"

def test_recipes_is_equal():
    recipes1 = Recipes(1, "test recipe_name", "test cooking_time", "test rating")
    recipes2 = Recipes(1, "test recipe_name", "test cooking_time", "test rating")
    assert recipes1 == recipes2
    
def test_recipes_format():
    recipes = Recipes(1, "test recipe_name", "test cooking_time", "test rating")
    assert str(recipes) == "Recipes(1, test recipe_name, test cooking_time, test rating)"
