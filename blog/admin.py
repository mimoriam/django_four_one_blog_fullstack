from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Ability to show these fields in admin panel
    list_display = ['title', 'slug', 'author', 'publish', 'status']

    prepopulated_fields = {'slug': ('title',)}  # Fills the slug with title automatically

    # Ability to filter by these fields in the right sidebar
    list_filter = ['status', 'created', 'publish', 'author']

    # Adds a new search bar to search by these fields
    search_fields = ['title', 'body']

    # Changes author names into integers
    raw_id_fields = ['author']

    # Adds a date at the bottom of the search bar
    date_hierarchy = 'publish'

    # Adds ability to order by choices below
    ordering = ['status', 'publish']
