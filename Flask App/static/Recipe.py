
class Recipe:
    # should be global
    the_recipe = []

    # store data submitted by the user
    title = form.title.data
    ingredients = form.ingredients.data
    steps = form.steps.data

    # add the data to the_recipe
    the_recipe.append({
        'title': title,
        'ingredients': ingredients,
        'steps': steps,
        'created_by': ,
    })