# navbar menu
from menu import Menu, MenuItem
from django.urls import reverse
from . import views as resume_vw
from djangoapps import settings as st


# add items to the main menu
Menu.add_item("main", MenuItem("Home", reverse(resume_vw.homepage), weight=10))
Menu.add_item("main", MenuItem("Resume", reverse(resume_vw.show_resume), weight=10))
Menu.add_item("main", MenuItem("About Me", reverse(resume_vw.about_me), weight=10))
Menu.add_item("main", MenuItem("Contact Me", reverse(resume_vw.contact_me), weight=10))
