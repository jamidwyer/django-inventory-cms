from django.contrib import admin
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from .models import Recipe, Ingredient

admin.site.register(Ingredient)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Recipe",
            {
                "fields": (
                    "name",
                    "instructions",
                    "cook_time",
                    "prep_time",
                    "estimated_cost",
                    "user"
                ),
            },
        ),
    )

    list_display = ("name", "display_ingredients", "instructions", "cook_time", "prep_time", "estimated_cost", "user")

    def display_ingredients(self, obj):
        links = format_html_join(
            mark_safe('<br>'),
            '<a href="{}">{}</a>',
            [(admin.reverse("admin:appname_ingredient_change", args=[ingredient.id]), ingredient.name)
             for ingredient in obj.ingredients.all()]
        )
        return links or mark_safe('<span>No ingredients</span>')
    
    display_ingredients.short_description = 'Ingredients'
