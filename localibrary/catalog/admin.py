from django.contrib import admin
from .models import Author, Genre,BookInstance ,Book,Reviews



#admin.site.register(Author)

#admin.site.register(Book)

admin.site.register(Reviews)

class BookInstanceInLine(admin.TabularInline):
    model=BookInstance 
class BookAdmin(admin.ModelAdmin):
    list_display=("book","title","author")
    inlines=[BookInstanceInLine]
admin.site.register(Book)
class BookInLine(admin.TabularInline):
    model=Book
class AuthorAdmin(admin.ModelAdmin):
    list_display=("book","last_name","first_name","data_of_birth","date_of_death")
    fields=["last_name","first_name",("data_of_birth","date_of_death")]
    inlines=[BookInLine]
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookInstance)
"""class BookInstanceAdmin(admin.ModelAdmin):
    list_display=("book","imprint","Lang","status","due_back","id")
    fieldsets=(
        (None,{
            'fields':('book','bookuser','imprint',"Lang",'id')
        }),
        ('Availablity',{
            'fields':('status','due_back')
        }),
    )"""
##admin.site.register(BookInstance,BookInstanceAdmin)
admin.site.register(Genre)

# Register your models here.
