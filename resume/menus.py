# navbar menu
from menu import Menu, MenuItem
from django.urls import reverse
from . import views as resume_vw


# add items to the main menu
Menu.add_item("main", MenuItem("Home", reverse(resume_vw.homepage), weight=10))
