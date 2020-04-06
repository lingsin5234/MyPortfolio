# navbar menu
from menu import Menu, MenuItem
from django.urls import reverse
from . import views as resume_vw


# add items to the main menu
Menu.add_item("main", MenuItem("Home", reverse(resume_vw.show_resume), weight=10))
Menu.add_item("main", MenuItem("My Projects", reverse(resume_vw.projects_list), weight=10))
Menu.add_item("main", MenuItem("Portfolio Project", reverse(resume_vw.project_markdown), weight=10))
Menu.add_item("main", MenuItem("About Me", reverse(resume_vw.about_me), weight=10))
Menu.add_item("main", MenuItem("Contact Me", reverse(resume_vw.contact_me), weight=10))
